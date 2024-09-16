import requests  # Library to make HTTP requests
import json  # Library to handle JSON data

# Function to fetch weather data using latitude and longitude
def get_weather_data(lat, lon):
    # API URL for the Open-Meteo weather service
    api_url = "https://api.open-meteo.com/v1/forecast"
    
    # Parameters to be sent in the API request (latitude, longitude, hourly temperature, and current weather)
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",  # Requesting hourly temperature data
        "current_weather": True  # Requesting current weather data
    }
    
    try:
        # Send GET request to the API with specified parameters
        response = requests.get(api_url, params=params)
        
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        
        # Return the JSON data from the API response
        return response.json()
    
    # Handle any request exceptions (e.g., connection errors or invalid responses)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None  # Return None if an error occurs

# Function to save the retrieved weather data to a file
def save_weather_data_to_file(data, filename="weather_data.txt"):
    # Open the file in write mode
    with open(filename, "w") as file:
        # Write a header to the file
        file.write("Weather Data:\n")
        
        # Write the JSON data in a formatted style with indentation
        file.write(json.dumps(data, indent=4))
    
    # Notify the user that the weather data has been saved
    print(f"Weather data saved to {filename}")

# Main function to interact with the user
def main():
    try:
        # Ask the user for the latitude and longitude
        latitude = float(input("Enter the latitude: "))  # Convert input to float
        longitude = float(input("Enter the longitude: "))  # Convert input to float
        
        print("Fetching weather data...")
        
        # Call the function to get the weather data
        weather_data = get_weather_data(latitude, longitude)
        
        # If weather data is successfully retrieved, save it to a file
        if weather_data:
            save_weather_data_to_file(weather_data)
        else:
            print("Failed to retrieve weather data.")
    
    # Handle invalid input (e.g., non-numeric latitude or longitude)
    except ValueError:
        print("Invalid input. Please enter numeric values for latitude and longitude.")

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to start the program