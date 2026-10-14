
import requests

def get_weather():
    city = input("Enter city name: ").strip()

    try:
        # Find city coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_response = requests.get(
            geo_url,
            params={"name": city, "count": 1},
            timeout=10
        )
        geo_response.raise_for_status()
        places = geo_response.json().get("results", [])

        if not places:
            print("City not found.")
            return

        place = places[0]
        latitude = place["latitude"]
        longitude = place["longitude"]

        # Get current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"
        response = requests.get(
            weather_url,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,weather_code"
            },
            timeout=10
        )
        response.raise_for_status()
        weather = response.json()["current"]

        print("\n--- Current Weather ---")
        print("City:", place["name"])
        print("Temperature:", weather["temperature_2m"], "°C")
        print("Humidity:", weather["relative_humidity_2m"], "%")
        print("Weather code:", weather["weather_code"])

    except requests.RequestException as error:
        print("Network error:", error)

if __name__ == "__main__":
    get_weather()
