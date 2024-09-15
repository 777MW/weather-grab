import requests

#open meteo URL
api_url = "https://api.open-meteo.com/v1/forecast"

# Placeholder weather data
response = requests.get(api_url)

print(f"Response status: {response.status_code}")