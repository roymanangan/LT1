#Roy Jose T. Manangan
#8-Camia

#CIRCULAR GARDEN
import math

#Inputs
radius = float(input("Enter radius in meters: "))

#Solution
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
area_sqrt = math.sqrt(area)
area_rnddowm = math.floor(area)
area_rndup = math.ceil(area)

#Output
print("The area of the circular garden is", area)
print("The circumference of the circular garden is", circumference)
print(f"The square root of the area of the circular garden is {area_sqrt: 2f}")
print("Area rounded down", area_rnddown)
print("Area rounded up", area_rndup)
