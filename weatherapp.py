#This is a simple Python program to print the weather at the user's location using their input city. 
#Also writes the data onto a file called weatherInfo.txt
#Written by Suryanarayan Menon A (github.com/SuryaNMenon) for project submission for Shape-AI's free bootcamp.

import requests
import sys
from datetime import datetime


my_api_key = '0635eb506ca1dcd1cf426726521f8a04' #API Key from OpenWeather
my_location = input("Enter city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+my_location+"&appid="+my_api_key
api_link = requests.get(complete_api_link)
api_data_json = api_link.json()

city_temp = ((api_data_json['main']['temp']) - 273.15)
weather_desc = api_data_json['weather'][0]['description']
humid = api_data_json['main']['humidity']
wind_spd = api_data_json['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I %M %S %p" )

print("Welcome to the Simple Weather App!")
print("Weather Statistics for - {} || {}".format(my_location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current Temperature: {:.2f} degree Celcius".format(city_temp))
print("Description about the weather: ", weather_desc)
print("Humidity: ", humid)
print("Wind speed: ", wind_spd, 'kmph')

#Saving weather info to a text file - using example of Trivandrum
original_stdout = sys.stdout
sys.stdout = open("weatherInfo.txt", "w")
print("Welcome to the Simple Weather App!")
print("Weather Statistics for - {} || {}".format(my_location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current Temperature: {:.2f} degree Celcius".format(city_temp))
print("Description about the weather: ", weather_desc)
print("Humidity: ", humid)
print("Wind speed: ", wind_spd, 'kmph')
sys.stdout.close()
sys.stdout = original_stdout