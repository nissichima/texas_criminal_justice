from requests_html import HTMLSession
import re
import sys
import pandas as pd
import argparse


#Create argument parser
parser =argparse.ArgumentParser()
parser.add_argument("-f","--filepath",required=True)
args = parser.parse_args()
destination_path = args.filepath


#Instantiate html session, and make request to first url
session = HTMLSession()
response = session.get("https://www.tdcj.texas.gov/death_row/dr_offenders_on_dr.html")


#extrapolate link, and use regeular expression to filter for relevant urls which pertain to deathrow innamtes.

links = list(response.html.absolute_links)
pattern = re.compile(r'https:\/\/.+(dr_info)\/\w+\.html')
filtered_links = list(filter(pattern.match, links))


#iterate through urls, collecting relevant
data_arr = []
for url in filtered_links:
    info_dict ={}
    try:

        response = session.get(url)
        name = response.html.find('table')[0].find("tr")[0].text.split('\n')[1]
        tdcj = response.html.find('table')[0].find("tr")[1].text.split('\n')[1]
        dob = response.html.find('table')[0].find("tr")[2].text.split('\n')[1]
        received_date = response.html.find('table')[0].find("tr")[3].text.split('\n')[1]
        received_age = response.html.find('table')[0].find("tr")[4].text.split('\n')[1]
        education_level = response.html.find('table')[0].find("tr")[5].text.split('\n')[1]
        offense_date = response.html.find('table')[0].find("tr")[6].text.split('\n')[1]
        age = response.html.find('table')[0].find("tr")[7].text.split('\n')[1]
        county = response.html.find('table')[0].find("tr")[8].text.split('\n')[1]
        race = response.html.find('table')[0].find("tr")[9].text.split('\n')[1]
        gender = response.html.find('table')[0].find("tr")[10].text.split('\n')[1]
        hair = response.html.find('table')[0].find("tr")[11].text.split('\n')[1]
        height = response.html.find('table')[0].find("tr")[12].text.split('\n')[1]
        weight = response.html.find('table')[0].find("tr")[13].text.split('\n')[1]
        eyes = response.html.find('table')[0].find("tr")[14].text.split('\n')[1]
        native_county = response.html.find('table')[0].find("tr")[15].text.split('\n')[1]
        native_state = response.html.find('table')[0].find("tr")[16].text.split('\n')[1]

        occupation = response.html.find("p")[0].text
        record = response.html.find("p")[1].text
        incident = response.html.find("p")[2].text
        co_defendants = response.html.find("p")[3].text
        victim_race_gender = response.html.find("p")[4].text
    except:
        education_level=None

    info_dict['Name'] = name
    info_dict['TDCJ #'] = tdcj
    info_dict['DOB'] = dob
    info_dict['Received Date'] = received_date
    info_dict['Received Age'] = received_age
    info_dict['Education Level'] = education_level
    info_dict['Offense Date'] = offense_date
    info_dict['Age'] = age
    info_dict['County'] = county
    info_dict['Race'] = race
    info_dict['Gender'] = gender
    info_dict['Hair'] = hair
    info_dict['Height'] = height
    info_dict['Weight'] = weight
    info_dict['Eyes'] = eyes
    info_dict['Native County'] = native_county
    info_dict['Native State'] = native_state
    info_dict['Occupation'] = occupation
    info_dict['Record'] = record
    info_dict['Incident'] = incident
    info_dict['Co_defendants'] = co_defendants
    info_dict['Victim_race_gender'] = victim_race_gender
    data_arr.append(info_dict)

#Put information into pandas data frame, and write it out to a csv file.
df= pd.DataFrame(data_arr)
df.to_csv(destination_path)

