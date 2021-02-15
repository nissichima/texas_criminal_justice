from requests_html import HTMLSession
import re

#Instantiate html session, and make request to first url
session = HTMLSession()
response = session.get("https://www.tdcj.texas.gov/death_row/dr_offenders_on_dr.html")


#extrapolate link, and use regeular expression to filter for relevant urls which pertain to deathrow innamtes.

links = list(response.html.absolute_links)
pattern = re.compile(r'https:\/\/.+(dr_info)\/\w+\.html')
filtered_links = list(filter(pattern.match, links))


#iteratet through urls, collecting relevant
for url in filtered_links[:2]:
	response = session.get(url)
	name = response.html.find('table')[0].find("tr")[0].text.split('\n')[1]
	print(name)
