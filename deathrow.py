from requests_html import HTMLSession
import re


session = HTMLSession()
response = session.get("https://www.tdcj.texas.gov/death_row/dr_offenders_on_dr.html")

links = list(response.html.absolute_links)
pattern = re.compile(r'https:\/\/.+(dr_info)\/\w+\.html')
filtered_links = list(filter(pattern.match, links))





for url in filtered_links[:2]:
	response = session.get(url)
	name = response.html.find('table')[0].find("tr")[0].text.split('\n')[1]
	print(name)
