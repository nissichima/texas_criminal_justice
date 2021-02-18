from requests_html import HTMLSession
import re
import pandas as pd

#Instantiate html session, and make request to first url
session = HTMLSession()
response = session.get("https://www.tdcj.texas.gov/death_row/dr_offenders_on_dr.html")


#extrapolate link, and use regeular expression to filter for relevant urls which pertain to deathrow innamtes.

links = list(response.html.absolute_links)
pattern = re.compile(r'https:\/\/.+(dr_info)\/\w+\.html')
filtered_links = list(filter(pattern.match, links))


#iterate through urls, collecting relevant
data_arr = []
for url in filtered_links[:2]:
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
    data_arr.append(info_dict)
    
#Put information into pandas data frame, and write it out to a csv file.
df= pd.DataFrame(data_arr)
df.to_csv("~/Desktop/innmates_on_deathrow.csv")

