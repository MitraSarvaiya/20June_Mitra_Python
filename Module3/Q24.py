#Write a Python class named Circle constructed by a radius and two 
# methods which will compute the area and the perimeter of a circle

from math import pi
class Circle:
    a=int(input("Enter radius: "))

    def Area(self):
      print("Area of circle: ",pi*self.a**2)

    def parameter(self):
      print("Parameter of circle: ",2*pi*self.a)

c=Circle()
c.Area()
c.parameter()