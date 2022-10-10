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

#Gas level function
def gaslevelgauge():
    gaslevellist = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    currentgaslevel = random.choice(gaslevellist)
    return currentgaslevel
