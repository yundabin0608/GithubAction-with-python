from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text,'html.parser')
data1 = soup.find('div', attrs={'class': "title_area _area_panel"})
pprint(data1)
if data1 != None:
    find_address = data1.find('h2', attrs={'class': "title"}).text
    pprint("📍 현 위치 : " + find_address)

data2 = soup.find('div',attrs={'class':"temperature_text"})
if data2 != None:
    temp_now = data2.find('strong').get_text()
    pprint("🌡️  현재 온도 : "+temp_now[5:])

data3 = soup.find('span', attrs={'class':"weather before_slash"})
if data3 != None:
    weather = data3.get_text()
    pprint("🌀 현재 날씨 : "+weather)

data4 = soup.find('ul', attrs={'class':"today_chart_list"})
if data4 != None:
    dust = data4.find_all('li', attrs={'class':"item_today level2"})
    dust1 = dust[0].find('span', attrs={'class':"txt"}).get_text()
    dust2 = dust[1].find('span', attrs={'class':"txt"}).get_text()
    pprint("🌫️  오늘의 미세먼지 : "+ dust1 + " | 오늘의 초미세먼지 : "+dust2)

data5 = data4.find('li', attrs={'class':"item_today type_sun"})
if data5 != None:
    sunrise = data5.find('span', attrs={'class':"txt"}).get_text()
    pprint("🔆 일출 시간 : "+sunrise)