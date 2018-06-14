import urllib.request
import urllib.parse
import base64
from bs4 import BeautifulSoup

url = "https://www.martindale.com/by-location/new-jersey-lawyers/"
hdr = hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

page = urllib.request.Request(url, headers = hdr)
with urllib.request.urlopen(page) as response:
   the_page = response.read()
soup = BeautifulSoup(the_page, 'html.parser')
#while soup.find('div', attrs={'class': 'flex-small-12 flex-medium-6 no-right-padding'}):

townDivs = soup.find_all("ul", {"class": "abc-panel-list"})

string = "["
for div in townDivs:
	name_box = div.find_all('li')
	for item in name_box:
		name = item.text.strip()		
		string+= '"{}",'.format(name)
string+= "]"
towns = open("NewJerseyTowns.txt", "w")
towns.write(string)
towns.close()
