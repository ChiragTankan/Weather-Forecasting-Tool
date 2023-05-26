import requests
import json
import os
def get_weather_forecast(city):
    """Gets the current weather forecast for a city.

    Args:
        city: The name of the city to get the weather forecast for.

    Returns:
        A dictionary containing the weather forecast for the city.
    """

    # Get the API key from the environment.
    api_key = os.environ["OPENWEATHERMAP_API_KEY"]

    # Make a request to the OpenWeatherMap API.
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
    )

    # Check the response status code.
    if response.status_code != 200:
        raise ValueError("Error getting weather forecast: {}".format(response.status_code))

    # Parse the JSON response.
    weather_data = json.loads(response.content)

    # Return the weather forecast.
    return weather_data

def main():
    # Get the city name from the user.
    city = input("Enter a city name: ")

    # Get the weather forecast for the city.
    weather_forecast = get_weather_forecast(city)

    # Print the weather forecast.
    print("The weather forecast for {} is:".format(city))
    print("* Temperature: {}°C".format(weather_forecast["main"]["temp"]))
    print("* Humidity: {}%".format(weather_forecast["main"]["humidity"]))
    print("* Pressure: {}hPa".format(weather_forecast["main"]["pressure"]))
    print("* Wind speed: {}m/s".format(weather_forecast["wind"]["speed"]))
    print("* Cloud cover: {}%".format(weather_forecast["clouds"]["all"]))

if __name__ == "__main__":
    main()
