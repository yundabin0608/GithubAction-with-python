import requests
from bs4 import BeautifulSoup

def get_seoul_weather():
    url = 'https://www.weather.com/weather/today/l/37.57,126.98'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
   
    temperature = soup.find('span', {'data-testid':"TemperatureValue"}).get_text()
    description = soup.find('div', {'data-testid':"wxPhrase"}).get_text()
    humidity = soup.findAll('div', {'data-testid':"wxData"})
    weather_data = {
        'Temperature': temperature,
        'Description': description,
        'Humidity': humidity[2].get_text()
    }
    
    return weather_data

# Example usage
seoul_weather = get_seoul_weather()
print("📍 서울의 날씨 ")
print("🌡️  현재 온도 : ", seoul_weather['Temperature'])
print("🌀 현재 날씨 : ", seoul_weather['Description'])
print("🌫️  현재 습도 : ", seoul_weather['Humidity'])