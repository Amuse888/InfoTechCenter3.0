#Weather
#Developer: Gabriel Westra
#Version 1.0

"""
Create a function for our current weather using the
random.choice function to determine what the weather is
picking from a list - using an If, Elif, and Else statements
to check the condition and print a specific print line
"""

#Import libraries here
import random

#Weather condition list using the random.choice library
#To randomly choose a condition and storing it in its brain
def weather():
    weatherForecast = ["Rain","Snow","Sunny","Cloudy","Foggy","Storming","Icy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

weatherAlert = weather()
print(weatherAlert)
def vrs(): #vrs means vehicle response system
    if weatherAlert == "Icy":
        print("\nVRS has changed your alarm 30 minutes earlier based on the NWS forcast of",weatherAlert)


vrs()