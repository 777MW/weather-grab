import requests

#API URL
api_url = "https://api.open-meteo.com/v1/forecast"

# Added parameters for NYC
params = {
    "latitude": 40.7128,
    "longitude": -74.0060
}

# Fetch weather data
response = requests.get(api_url, params=params)

print(f"Response status code: {response.status_code}")