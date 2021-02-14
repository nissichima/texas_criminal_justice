from requests_html HTMLSession
import re


session = HTMLSession()
response = session.get("")

links = list(response.html.absolute_links)
pattern = re.compile(r'https:\/\/.+(dr_info)\/\w+\.html')
filtered_links = list(filter(pattern.match, links))





for url in filtered_links:
	#do something for each link