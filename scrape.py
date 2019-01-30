import csv
import requests
from bs4 import BeautifulSoup
#------------------
item = 'none'
url = 'none'
price = 'none'


with open('craigslist.csv', 'w') as f:
	csv_writer = csv.writer(f)
	csv_writer.writerow(['Description','Price','URL'])
	data = requests.get("https://juneau.craigslist.org/d/boats/search/boo")
	soup = BeautifulSoup(data.text , "html.parser")

	i = 0
	for rows in soup.find_all("ul", class_= "rows"):
		for result_row in rows.find_all('li', class_= 'result-row'):
			for result_info in result_row.find_all('p', class_= 'result-info'):
				link = result_info.find('a')
				print(link.text)
				item = link.text
				print(link.get('href'))
				url = link.get('href')
				if(result_info.find('span', class_='result-meta').find('span', class_='result-price')) != None:
					price = result_info.find('span', class_='result-meta').find('span', class_='result-price').text
					print(result_info.find('span', class_='result-meta').find('span', class_='result-price').text)
				else:
					price = 'None Stated'
				print('\n')
				csv_writer.writerow([item,price,url])
				i = i + 1
print('total item count: {}'.format(i))





