#Write a program that calculates the cost per square cm of a circular pizza, given its diameter and price.
#The formula for area of a circle 
# A = πr2


#ALGORITHM
#
#
#
#

#Indicate the price/square 
#Ask the user for his diamter and divide it by 2.
#Tell him the prize of his pizza based on his size

import math

def main():
    d = float(input("What is the diameter of your pizza: "))
    r = d//2
    a = math.pi * r**2
    shareprice = 1.2
    price = a * shareprice 
    print("Share Price is",shareprice)
    print("The Price of pizza is",price)

main()

    
