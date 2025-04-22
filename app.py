import requests
import os

API_KEY = os.getenv('WEATHER_API_KEY')

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url)
    data = r.json()
    if r.status_code == 200:
        print(f"🌤️ Weather in {city}: {data['main']['temp']}°C")
    else:
        print("Error:", data.get("message", "Something went wrong"))

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)