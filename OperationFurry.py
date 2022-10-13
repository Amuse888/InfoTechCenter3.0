#***********************************************************************************
#Import Libraries Here
from time import sleep #We imported the Sleep function from the Time library

import random
#***********************************************************************************


#Welcome Screen
#Developer: Gabriel Westra
#Version: 1.0

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is Loading
"""

print("\033[1;36m  \n\nWelcome to Operation Furry InfoTech Center \n")
sleep(2)
print("\nOperation Furry's Operation System Is Booting Up\n")
sleep(1)

for i in range(3):
    print("\033[1;31m  OS Booting Up") #Adds OS Booting Up message that plays multiple times in the color red
    sleep(1)

print("\033[1;36m  \nOs has booted up!\n\n")
sleep(1.5)

#Weather
#Developer: Gabriel Westra
#Version 1.0

"""
Create a function for our current weather using the
random.choice function to determine what the weather is
picking from a list - using an If, Elif, and Else statements
to check the condition and print a specific print line
"""

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


#Gasoline
#Programer: Gabe Westra
#Version 1.0

"""
Define a function to check our gas gauge and determine how far
we have until we need gasoline based on an if, elif, else
condition
"""


#Gas level function
def gaslevelgauge():
    gaslevellist = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentgaslevel = random.choice(gaslevellist)
    return currentgaslevel

#Variable calling the gaslevelgauge function to store value once
gaslevelindicator = gaslevelgauge()

def listofgasstations():
    gasstation = ["Shell", "Circle K", "Marathon", "Speedway", "Meijer", "Bp", "Citgo"]
    gasstationnearby = random.choice(gasstation)
    return gasstationnearby

def gaslevelalert():
    milestogasstation = round (random.uniform(1,25),1)
    milestogasstationquartertank = round(random.uniform(26,50),1)
    if gaslevelindicator == "Empty":
        print("\n* * *WARNING! YOU ARE ON EMPTY!* * *")
        sleep(1.5)
        print("Calling Emergency Contact")
    elif gaslevelindicator == "Low":
        print("\n* *Warning!* *")
        sleep(1)
        print ("You are low on gas; Checking google Maps for the closest gas station")
        sleep(2)
        print("The closest gas station is", listofgasstations(), "which is", milestogasstation, "miles away.")
    elif gaslevelindicator == "Quarter Tank":
        print("\nYour gas tank is only a quarter full. Checking Google Maps for a close gas station")
        sleep(1.5)
        print("A close gas station is", listofgasstations(), "which is", milestogasstationquartertank, "miles away.")
    elif gaslevelindicator == "Half Tank":
        print("\nYour gas tank is half full.")
        sleep(1)
        print("You still have plenty of gas.")
    elif gaslevelindicator == "Three Quarter Tank":
        print("\nYour gas tank is three quarters full.")
        sleep(1.5)
        print("You still have lots of gas.")
    else:
        print("\nYour gas tank is full. Have a safe drive.")


#***********************************************************************************

#Call functions here...
vrs()
gaslevelalert()
