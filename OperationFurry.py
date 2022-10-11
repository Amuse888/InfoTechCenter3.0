#Gasoline
#Programer: Gabe Westra
#Version 1.0

"""
Define a function to check our gas gauge and determine how far
we have until we need gasoline based on an if, elif, else
condition
"""

#import library here
import random
from time import sleep

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
    if gaslevelindicator == "Empty":
        print("* * *WARNING! YOU ARE ON EMPTY!* * *")
        sleep(1.5)
        print("Calling Emergency Contact")
    elif gaslevelindicator == "Low":
        print("* *Warning!* *")
        sleep(1)
        print ("You are low on gas; Checking google Maps for the closest gas station")
        sleep(2)
        print("The closest gas station is", listofgasstations())

gaslevelalert()