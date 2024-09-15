import requests
#API URL
api_url = "https://api.open-meteo.com/v1/forecast"
#NYC latitude and longitude
params = {
    "latitude": 40.7128,
    "longitude": -74.0060
}
# Fetch weather data
response = requests.get(api_url, params=params)

#check for successful response
if response.status_code == 200:
    weather_data = response.json()
    print(weather_data)  # Print the raw JSON data
else:
    print(f"Failed to retrieve weather data. Status code: {response.status_code}")