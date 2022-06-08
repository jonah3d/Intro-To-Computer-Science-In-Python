#Write a program to calculate the volume and surface area of a sphere from its radius,given as input.
#Useful formulas

#V = 4/3πr3 
#A = 4πr2

#Algorithm

#.
#.
#.
#.

# We ask th the user to provide the radius of the sphere.
# Then we apply the formula

import math

def main():
    r = int(input("Input the radius of the sphere: "))
    v = (4/3) * math.pi * r**3
    a = (4*math.pi)*r**2 
    print("The volume of the sphere is",v) 
    print("The area of the sphere is",a)

main()
 
