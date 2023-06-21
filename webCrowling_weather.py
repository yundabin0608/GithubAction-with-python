from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

if html == None : raise Exception("html err")
soup = bs(html.text,'html.parser')
if soup == None : raise Exception("bs err")
data1 = soup.find('div', {'class': "title_area _area_panel"})
find_address = data1.find('h2', {'class': "title"}).text
pprint("📍 현 위치 : " + find_address)

data2 = soup.find('div',{'class':"temperature_text"})
temp_now = data2.find('strong').get_text()
temp_now = temp_now[5:]
pprint("🌡️  현재 온도 : "+temp_now)

data3 = soup.find('span', {'class':"weather before_slash"})
weather = data3.get_text()
pprint("🌀 현재 날씨 : "+weather)

data4 = soup.find('ul', {'class':"today_chart_list"})
dust = data4.find_all('li', {'class':"item_today level2"})
dust1 = dust[0].find('span', {'class':"txt"}).get_text()
dust2 = dust[1].find('span', {'class':"txt"}).get_text()
pprint("🌫️  오늘의 미세먼지 : "+ dust1 + " | 오늘의 초미세먼지 : "+dust2)

data5 = data4.find('li', {'class':"item_today type_sun"})
sunrise = data5.find('span', {'class':"txt"}).get_text()
pprint("🔆 일출 시간 : "+sunrise)