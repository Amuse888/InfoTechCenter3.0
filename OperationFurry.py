#Welcome Screen
#Developer: Gabriel Westra
#Version: 1.0

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is Loading
"""

#Import Libraries Here
from time import sleep #We imported the Sleep function from the Time library

print("\033[1;36m  \n\nWelcome to Operation Furry InfoTech Center \n")
sleep(2)
print("\nOperation Furry's Operation System Is Booting Up\n")
sleep(1)

for i in range(3):
    print("\033[1;31m  OS Booting Up")
    sleep(1)