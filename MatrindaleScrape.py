import urllib.request
import urllib.parse
import base64
from bs4 import BeautifulSoup
import math

crap = ["Navigation", "About Us", "Featured Services", "Digital Network", "About Practice Area Searches", "About Location Searches", "Back", "Search Tools", "Ratings & Reviews", "Attorney Products & Services", "About Martindale-Hubbell®", "Start Comparing", "categories", "filters"]
towns = ["Aberdeen","Absecon","Allendale","Allenhurst","Allentown","Allenwood","Alloway","Alpine","Andover","Annandale","Asbury","Asbury Park","Atco","Atlantic City","Atlantic Highlands","Audubon","Avalon","Avenel","Avon-By-The-Sea","Barnegat","Barnegat Light","Barrington","Basking Ridge","Bay Head","Bayonne","Bayville","Beach Haven","Beachwood","Bedminster","Belford","Belle Mead","Belleville","Bellmawr","Belmar","Belvidere","Bergenfield","Berkeley Heights","Berlin","Bernardsville","Blackwood","Blairstown","Blawenburg","Bloomfield","Bloomingdale","Bloomsbury","Bogota","Boonton","Bordentown","Bound Brook","Bradley Beach","Branchburg Township","Branchville","Brant Beach","Brick","Bridgeton","Bridgewater","Brielle","Brigantine","Brookside","Browns Mills","Budd Lake","Burlington","Burlington Township","Butler","Caldwell","Califon","Camden","Cape May","Cape May Court House","Cape May Point","Carlstadt","Carneys Point","Carteret","Cedar Grove","Cedar Knolls","Chatham","Cherry Hill","Chester","Cinnaminson","Clark","Clarksboro","Clarksburg","Clayton","Clementon","Cliffside Park","Cliffwood","Clifton","Clinton","Closter","Collingswood","Colonia","Colts Neck","Columbus","Convent Station","Cranbury","Cranford","Cream Ridge","Cresskill","Crosswicks","Dayton","Del Haven","Delran","Demarest","Denville","Deptford","Dover","Dumont","Dunellen","East Brunswick","East Hanover","East Millstone","East Orange","East Rutherford","East Windsor","Eastampton","Eatontown","Edgewater","Edison","Egg Harbor City","Egg Harbor Township","Elizabeth","Elmer","Elmwood Park","Emerson","Englewood","Englewood Cliffs","Englishtown","Evesham","Ewing","Fair Haven","Fair Lawn","Fairfield","Fairton","Fairview","Fanwood","Far Hills","Farmingdale","Flanders","Flemington","Florence","Florham Park","Fords","Forked River","Fort Dix","Fort Lee","Franklin","Franklin Lakes","Franklin Park","Franklinville","Freehold","Frenchtown","Galloway","Garfield","Garwood","Gibbsboro","Gibbstown","Gillette","Gladstone","Glassboro","Glen Gardner","Glen Ridge","Glen Rock","Glendora","Gloucester City","Great Meadows","Green Brook","Guttenberg","Hackensack","Hackettstown","Haddon Heights","Haddon Township","Haddonfield","Hainesport","Haledon","Hamburg","Hamilton","Hamilton Square","Hamilton Township","Hammonton","Hampton","Hardwick","Harrington Park","Harrison","Harvey Cedars","Hasbrouck Heights","Haworth","Hawthorne","Hazlet","Helmetta","Hewitt","High Bridge","Highland Lakes","Highland Park","Highlands","Hightstown","Hillsborough","Hillsdale","Hillside","Ho-Ho-Kus","Hoboken","Holmdel","Hopatcong","Hope","Hopewell","Howell","Imlaystown","Interlaken","Ironia","Irvington","Iselin","Island Heights","Jackson","Jamesburg","Jersey City","Keansburg","Kearny","Keasbey","Kendall Park","Kenilworth","Kenvil","Keyport","Kingston","Kinnelon","Lafayette","Lake Hiawatha","Lake Hopatcong","Lakehurst","Lakewood","Lambertville","Landing","Laurel Springs","Lavallette","Lawnside","Lawrenceville","Lebanon","Ledgewood","Leonardo","Leonia","Liberty Corner","Lincoln Park","Lincroft","Linden","Lindenwold","Linwood","Little Egg Harbor","Little Falls","Little Ferry","Little Silver","Livingston","Lodi","Long Beach Township","Long Branch","Long Valley","Lumberton","Lyndhurst","Madison","Magnolia","Mahwah","Manahawkin","Manalapan","Manasquan","Manchester","Mantoloking","Mantua","Manville","Maple Shade","Maplewood","Margate City","Marlboro","Marlton","Marmora","Martinsville","Matawan","Mays Landing","Maywood","Mc Afee","Mc Guire Afb","Medford","Medford Lakes","Mendham","Mercerville","Merchantville","Metuchen","Mickleton","Middlesex","Middletown","Midland Park","Milford","Millburn","Millington","Millstone","Millstone Township","Milltown","Millville","Milmay","Mine Hill","Monmouth Beach","Monmouth Junction","Monroe Township","Montague Township","Montclair","Montvale","Montville","Moonachie","Moorestown","Morganville","Morris Plains","Morristown","Mount Arlington","Mount Ephraim","Mount Freedom","Mount Holly","Mount Laurel","Mount Olive","Mount Tabor","Mountain Lakes","Mountainside","Mullica Hill","Murray Hill","Neptune","Neptune City","Neshanic Station","New Brunswick","New Milford","New Providence","New Vernon","Newark","Newfoundland","Newton","Normandy Beach","North Arlington","North Bergen","North Brunswick","North Caldwell","North Haledon","North Plainfield","North Wildwood","Northfield","Northvale","Norwood","Nutley","Oak Ridge","Oakhurst","Oakland","Oaklyn","Ocean","Ocean City","Ocean Gate","Ocean Grove","Ocean Township","Oceanport","Old Bridge","Old Tappan","Oldwick","Oradell","Orange","Oxford","Palisades Park","Palmyra","Paramus","Park Ridge","Parlin","Parsippany","Passaic","Paterson","Peapack","Pennington","Penns Grove","Pennsauken","Pennsville","Pequannock","Perth Amboy","Phillipsburg","Picatinny Arsenal","Pine Beach","Pine Brook","Piscataway","Pitman","Pittstown","Plainfield","Plainsboro","Pleasantville","Pluckemin","Point Pleasant","Point Pleasant Beach","Point Pleasant Boro","Pompton Lakes","Pompton Plains","Pottersville","Princeton","Princeton Junction","Rahway","Ramsey","Randolph","Raritan","Red Bank","Ridgefield","Ridgefield Park","Ridgewood","Ringoes","Ringwood","Rio Grande","River Edge","River Vale","Riverdale","Riverside","Riverton","Robbinsville","Rochelle Park","Rockaway","Rockleigh","Roosevelt","Roseland","Roselle","Roselle Park","Rumson","Runnemede","Rutherford","Saddle Brook","Saddle River","Salem","Sayreville","Scotch Plains","Sea Bright","Sea Girt","Sea Isle City","Seaside Heights","Seaside Park","Secaucus","Sewaren","Sewell","Shamong","Ship Bottom","Short Hills","Shrewsbury","Sicklerville","Skillman","Smithville","Somerdale","Somers Point","Somerset","Somerville","South Amboy","South Bound Brook","South Brunswick","South Dennis","South Hackensack","South Orange","South Plainfield","South River","South Seaville","Southampton","Sparta","Spotswood","Spring Lake","Spring Lake Heights","Springfield","Stanhope","Stanton","Stewartsville","Stirling","Stockton","Stone Harbor","Stratford","Succasunna","Summit","Surf City","Sussex","Swedesboro","Tansboro","Teaneck","Tenafly","Tennent","Teterboro","Thorofare","Three Bridges","Tinton Falls","Titusville","Toms River","Totowa","Towaco","Township Of Washington","Trenton","Tuckahoe","Tuckerton","Turnersville","Union","Union City","Upper Montclair","Upper Saddle River","Vauxhall","Ventnor City","Vernon","Verona","Villas","Vincentown","Vineland","Voorhees","Waldwick","Wall","Wall Township","Wallington","Wanaque","Waretown","Warren","Washington","Washington Township, Bergen County","Watchung","Wayne","Weehawken","Wenonah","West Atlantic City","West Berlin","West Caldwell","West Cape May","West Collingswood","West Deal","West Deptford","West End","West Keansburg","West Long Branch","West Milford","West New York","West Orange","West Paterson","West Trenton","West Windsor","Westampton","Westfield","Westmont","Westville","Westwood","Wharton","Whippany","Whitehouse","Whitehouse Station","Whiting","Wildwood","Wildwood Crest","Williamstown","Willingboro","Winslow","Wood Ridge","Woodbine","Woodbridge","Woodbury","Woodbury Heights","Woodcliff Lake","Woodland Park","Woodstown","Woolwich Township","Wyckoff","Yardville","Aberdeen","Absecon","Allendale","Allenhurst","Allentown","Allenwood","Alloway","Alpine","Andover","Annandale","Asbury","Asbury Park","Atco","Atlantic City","Atlantic Highlands","Audubon","Avalon","Avenel","Avon-By-The-Sea","Barnegat","Barnegat Light","Barrington","Basking Ridge","Bay Head","Bayonne","Bayville","Beach Haven","Beachwood","Bedminster","Belford","Belle Mead","Belleville","Bellmawr","Belmar","Belvidere","Bergenfield","Berkeley Heights","Berlin","Bernardsville","Blackwood","Blairstown","Blawenburg","Bloomfield","Bloomingdale","Bloomsbury","Bogota","Boonton","Bordentown","Bound Brook","Bradley Beach","Branchburg Township","Branchville","Brant Beach","Brick","Bridgeton","Bridgewater","Brielle","Brigantine","Brookside","Browns Mills","Budd Lake","Burlington","Burlington Township","Butler","Caldwell","Califon","Camden","Cape May","Cape May Court House","Cape May Point","Carlstadt","Carneys Point","Carteret","Cedar Grove","Cedar Knolls","Chatham","Cherry Hill","Chester","Cinnaminson","Clark","Clarksboro","Clarksburg","Clayton","Clementon","Cliffside Park","Cliffwood","Clifton","Clinton","Closter","Collingswood","Colonia","Colts Neck","Columbus","Convent Station","Cranbury","Cranford","Cream Ridge","Cresskill","Crosswicks","Dayton","Del Haven","Delran","Demarest","Denville","Deptford","Dover","Dumont","Dunellen","East Brunswick","East Hanover","East Millstone","East Orange","East Rutherford","East Windsor","Eastampton","Eatontown","Edgewater","Edison","Egg Harbor City","Egg Harbor Township","Elizabeth","Elmer","Elmwood Park","Emerson","Englewood","Englewood Cliffs","Englishtown","Evesham","Ewing","Fair Haven","Fair Lawn","Fairfield","Fairton","Fairview","Fanwood","Far Hills","Farmingdale","Flanders","Flemington","Florence","Florham Park","Fords","Forked River","Fort Dix","Fort Lee","Franklin","Franklin Lakes","Franklin Park","Franklinville","Freehold","Frenchtown","Galloway","Garfield","Garwood","Gibbsboro","Gibbstown","Gillette","Gladstone","Glassboro","Glen Gardner","Glen Ridge","Glen Rock","Glendora","Gloucester City","Great Meadows","Green Brook","Guttenberg","Hackensack","Hackettstown","Haddon Heights","Haddon Township","Haddonfield","Hainesport","Haledon","Hamburg","Hamilton","Hamilton Square","Hamilton Township","Hammonton","Hampton","Hardwick","Harrington Park","Harrison","Harvey Cedars","Hasbrouck Heights","Haworth","Hawthorne","Hazlet","Helmetta","Hewitt","High Bridge","Highland Lakes","Highland Park","Highlands","Hightstown","Hillsborough","Hillsdale","Hillside","Ho-Ho-Kus","Hoboken","Holmdel","Hopatcong","Hope","Hopewell","Howell","Imlaystown","Interlaken","Ironia","Irvington","Iselin","Island Heights","Jackson","Jamesburg","Jersey City","Keansburg","Kearny","Keasbey","Kendall Park","Kenilworth","Kenvil","Keyport","Kingston","Kinnelon","Lafayette","Lake Hiawatha","Lake Hopatcong","Lakehurst","Lakewood","Lambertville","Landing","Laurel Springs","Lavallette","Lawnside","Lawrenceville","Lebanon","Ledgewood","Leonardo","Leonia","Liberty Corner","Lincoln Park","Lincroft","Linden","Lindenwold","Linwood","Little Egg Harbor","Little Falls","Little Ferry","Little Silver","Livingston","Lodi","Long Beach Township","Long Branch","Long Valley","Lumberton","Lyndhurst","Madison","Magnolia","Mahwah","Manahawkin","Manalapan","Manasquan","Manchester","Mantoloking","Mantua","Manville","Maple Shade","Maplewood","Margate City","Marlboro","Marlton","Marmora","Martinsville","Matawan","Mays Landing","Maywood","Mc Afee","Mc Guire Afb","Medford","Medford Lakes","Mendham","Mercerville","Merchantville","Metuchen","Mickleton","Middlesex","Middletown","Midland Park","Milford","Millburn","Millington","Millstone","Millstone Township","Milltown","Millville","Milmay","Mine Hill","Monmouth Beach","Monmouth Junction","Monroe Township","Montague Township","Montclair","Montvale","Montville","Moonachie","Moorestown","Morganville","Morris Plains","Morristown","Mount Arlington","Mount Ephraim","Mount Freedom","Mount Holly","Mount Laurel","Mount Olive","Mount Tabor","Mountain Lakes","Mountainside","Mullica Hill","Murray Hill","Neptune","Neptune City","Neshanic Station","New Brunswick","New Milford","New Providence","New Vernon","Newark","Newfoundland","Newton","Normandy Beach","North Arlington","North Bergen","North Brunswick","North Caldwell","North Haledon","North Plainfield","North Wildwood","Northfield","Northvale","Norwood","Nutley","Oak Ridge","Oakhurst","Oakland","Oaklyn","Ocean","Ocean City","Ocean Gate","Ocean Grove","Ocean Township","Oceanport","Old Bridge","Old Tappan","Oldwick","Oradell","Orange","Oxford","Palisades Park","Palmyra","Paramus","Park Ridge","Parlin","Parsippany","Passaic","Paterson","Peapack","Pennington","Penns Grove","Pennsauken","Pennsville","Pequannock","Perth Amboy","Phillipsburg","Picatinny Arsenal","Pine Beach","Pine Brook","Piscataway","Pitman","Pittstown","Plainfield","Plainsboro","Pleasantville","Pluckemin","Point Pleasant","Point Pleasant Beach","Point Pleasant Boro","Pompton Lakes","Pompton Plains","Pottersville","Princeton","Princeton Junction","Rahway","Ramsey","Randolph","Raritan","Red Bank","Ridgefield","Ridgefield Park","Ridgewood","Ringoes","Ringwood","Rio Grande","River Edge","River Vale","Riverdale","Riverside","Riverton","Robbinsville","Rochelle Park","Rockaway","Rockleigh","Roosevelt","Roseland","Roselle","Roselle Park","Rumson","Runnemede","Rutherford","Saddle Brook","Saddle River","Salem","Sayreville","Scotch Plains","Sea Bright","Sea Girt","Sea Isle City","Seaside Heights","Seaside Park","Secaucus","Sewaren","Sewell","Shamong","Ship Bottom","Short Hills","Shrewsbury","Sicklerville","Skillman","Smithville","Somerdale","Somers Point","Somerset","Somerville","South Amboy","South Bound Brook","South Brunswick","South Dennis","South Hackensack","South Orange","South Plainfield","South River","South Seaville","Southampton","Sparta","Spotswood","Spring Lake","Spring Lake Heights","Springfield","Stanhope","Stanton","Stewartsville","Stirling","Stockton","Stone Harbor","Stratford","Succasunna","Summit","Surf City","Sussex","Swedesboro","Tansboro","Teaneck","Tenafly","Tennent","Teterboro","Thorofare","Three Bridges","Tinton Falls","Titusville","Toms River","Totowa","Towaco","Township Of Washington","Trenton","Tuckahoe","Tuckerton","Turnersville","Union","Union City","Upper Montclair","Upper Saddle River","Vauxhall","Ventnor City","Vernon","Verona","Villas","Vincentown","Vineland","Voorhees","Waldwick","Wall","Wall Township","Wallington","Wanaque","Waretown","Warren","Washington","Washington Township, Bergen County","Watchung","Wayne","Weehawken","Wenonah","West Atlantic City","West Berlin","West Caldwell","West Cape May","West Collingswood","West Deal","West Deptford","West End","West Keansburg","West Long Branch","West Milford","West New York","West Orange","West Paterson","West Trenton","West Windsor","Westampton","Westfield","Westmont","Westville","Westwood","Wharton","Whippany","Whitehouse","Whitehouse Station","Whiting","Wildwood","Wildwood Crest","Williamstown","Willingboro","Winslow","Wood Ridge","Woodbine","Woodbridge","Woodbury","Woodbury Heights","Woodcliff Lake","Woodland Park","Woodstown","Woolwich Township","Wyckoff","Yardville"]
csv = open("NJLawFirms2.csv", "w") 
count = 0
totalfirms = 0 
for town in towns:
	if town == towns[0] and count > 1: 
		break 
	print("Currently on town: {}".format(town))
	url = "https://www.martindale.com/accountants-liability-law-firms/newark/new-jersey/?params="
	json = """{"type":"lawfirm","pageTitle":"l:Aberdeen|a:Commercial Law","practiceAreasRecents":["Commercial Law"],"geoLocationFacet":["%s, NJ"],"geoLocationFacetRecents":["%s, NJ"],"page":1,"limit":25,"offset":0,"sort":"","sortType":"","clearParams":false,"keyword":""}""" % (town, town) 
	json = json.encode()
	json = base64.b64encode(json)
	json= json.decode()
	url = url + str(json)
	hdr = hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
	page = urllib.request.Request(url, headers = hdr)
	with urllib.request.urlopen(page) as response:
		the_page = response.read()
	soup = BeautifulSoup(the_page, 'html.parser')
	resultDiv = soup.find("div", {"class":"results-bar-inner"})
	result_box = resultDiv.find('strong')
	results = result_box.text 
	results = results.split()
	print(results)
	number = results[0]
	number = number.replace(",", "")
	number = int(number)
	totalfirms += number
	rangenum = math.ceil(number / 25) + 1
	
	
	for page in range(1, rangenum):
		if page == 1: 
			url = "https://www.martindale.com/accountants-liability-law-firms/newark/new-jersey/?params="
		else: 
			url = "https://www.martindale.com/accountants-liability-law-firms/newark/new-jersey/?page={}&params=".format(str(page))
		json = """{"type":"lawfirm","pageTitle":"l:Aberdeen|a:Commercial Law","practiceAreasRecents":["Commercial Law"],"geoLocationFacet":["%s, NJ"],"geoLocationFacetRecents":["%s, NJ"],"page":1,"limit":25,"offset":0,"sort":"","sortType":"","clearParams":false,"keyword":""}""" % (town, town) 
		json = json.encode()
		json = base64.b64encode(json)
		json= json.decode()
		url = url + str(json)
		hdr = hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

		#print(url)

		page = urllib.request.Request(url, headers = hdr)

		with urllib.request.urlopen(page) as response:
		   the_page = response.read()
		soup = BeautifulSoup(the_page, 'html.parser')
		#while soup.find('div', attrs={'class': 'flex-small-12 flex-medium-6 no-right-padding'}):

		lawFirmDivs = soup.find_all("div", {"class": "medium-12 columns firm-info srr-area "})

		for div in lawFirmDivs:
			name_box = div.find_all('strong')
			if div.find_all('a', attrs={'class': 'button webstats-website-click navigable'}) != None:
				websites = div.find_all('a', attrs={'class': 'button webstats-website-click navigable'})
				for item in name_box:
					name = item.text.strip()		
					if name not in crap and "Results:" not in name:
						FirmName = name
				for website in websites: 
					website = website['href']
					FirmSite = website
					#print("{}, {}".format(FirmName, FirmSite))
					csv.write("{}, {}\r\n".format(FirmName.replace(",", ''), FirmSite))
					
	count += 1				
csv.close()
print(totalfirms)
				
	



'''
name_box = soup.find_all('strong')
websites = soup.find_all('a', attrs={'class': 'button webstats-website-click navigable'})
for item in name_box:
	name = item.text.strip()		
	if name not in crap and "Results:" not in name:
		print(name)
for website in websites: 
	website = website['href']
	print(website)
'''