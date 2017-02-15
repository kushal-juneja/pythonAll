'''
Objective
1. Area calculate class for area of square and circle
2. Pass a json string with radius for cirxle and side for square
'''

import os

#ast module helps in coverting string to dictionary
import ast

class area():
    dimensions=1
#initialises the dimension
    def __init__(self,dimension):
        self.dimensions=dimension

#area of circle
    def areaCircle(self):
       try:
            radius=int(ast.literal_eval(self.dimensions).get('radius'))
            area=3.14*radius*radius
            print('Area of Square is:'+str(area))
       except:
            print('Error')

    def areaSquare(self):
       try:
            side=int(ast.literal_eval(self.dimensions).get('side'))
            area=side*side
            print('Area of Square is:'+str(area))
       except:
            print('Error')

#if there is key error, except section is  reached, which calculates the area of circle
    def operation(self):
        try:
            side=int(ast.literal_eval(self.dimensions).get('side'))
            self.areaSquare()
        except:
            self.areaCircle()

#create json string
dimension="{'side':'23'}"

#Create class
areCalc= area(dimension)

#call the operation
areCalc.operation()
