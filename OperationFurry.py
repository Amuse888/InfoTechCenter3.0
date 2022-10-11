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

def gaslevelalert():
    if gaslevelindicator == "Empty":
        print("* * *WARNING! YOU ARE ON EMPTY!* * *")
        sleep(1.5)
        print("Calling Emergency Contact")

gaslevelalert()