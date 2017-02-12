'''
Objectives
----------
#1. even or odd
#2. Sum two numbers
#3. Even odd count in a list
#4. Reverse String
'''

import os
def activity(num1):
#even odd
    if(num1%2==0):
        print('Even Number')
    else:
        print('Odd Number')


def activity01(num1,num2):
#Sum
    print(int(num1)+int(num2))


def activity02(numLst):
#Even odd count
    odd= 0
    even=0
    for num in numLst:
        if(num%2==0):
            even+=1
        else:
            odd+=1

    print(str(odd)+' '+str(even))

def activity03(str):
#String Rev
    str1=[]
    for char in str:

        str1.append(char)
    str1.reverse()
    print(''.join(str1))

# Another method to reverse a string

def activity04(str):
#String Rev
    print(str[::-1])


activity(23)
activity01(1,2)
activity02([1,2,3,4,34,12,34,12])
activity03('James The Elephant')
activity04('James The Elephant')

