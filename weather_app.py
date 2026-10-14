
import requests

API_KEY = input("Enter your OpenWeather API key: ").strip()

city = input("Enter city name: ").strip()

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if response.status_code == 200:
        print("\nCity:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
    else:
        print("Error:", data.get("message", "Unable to get weather"))

except requests.RequestException:
    print("Network error. Please check your internet connection.")
