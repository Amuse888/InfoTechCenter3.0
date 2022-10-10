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
    weatherForecast = ["Rain","Snow","Sunny","Windy","Foggy","Storming","Icy"]
    weatherCondition = random.choice(weatherForecast)
    return weatherCondition

weatherAlert = weather()
print(weatherAlert)
def vrs(): #vrs means vehicle response system
    if weatherAlert == "Icy":
        print("\033[1;36m VRS has changed your alarm 30 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 50 MPH")
    elif weatherAlert == "Snow":
        print("\033[1;35m VRS has changed your alarm 15 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 70 MPH")
    elif weatherAlert == "Rain":
        print("\033[1;34m VRS has changed your alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 90 MPH")
    elif weatherAlert == "Windy":
        print("\033[1;37m VRS has changed your alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 80 MPH")
    elif weatherAlert == "Foggy":
        print("\033[1;38m VRS has changed your alarm 10 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 60 MPH")
    elif weatherAlert == "Storming":
        print("\033[1;30m VRS has changed your alarm 20 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 65 MPH")
    else:
        print("\033[1;33m VRS has changed your alarm 1 minute earlier based on the NWS forcast of", weatherAlert)
        print("VRS will allow your car to go 100 MPH")


vrs()