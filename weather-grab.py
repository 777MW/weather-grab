import requests
import json

latitude = float(input("Enter the latitude: "))
longitude = float(input("Enter the longitude: "))

#API URL
api_url = "https://api.open-meteo.com/v1/forecast"
#NYC latitude and longitude
params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m",
    "current_weather": True
}
# Fetch weather data
try:
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    weather_data = response.json()
    
    # Write weather data to a file
    with open("weather_data.txt", "w") as file:
        file.write("Weather Data:\n")
        file.write(json.dumps(weather_data, indent=4))
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")