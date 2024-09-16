import math


def areaOfCircle(radius):

    area = (radius*radius) * 3.141592653

    simplifyOne = (area*100)/100

    return simplifyOne




def totalDue(money, tax):

    simplifyTwo = money + (money * (tax/100))

    return simplifyTwo





def differTemp(fahrenheit):

    newTemp = (fahrenheit - 32) * (5 / 9)

    simplifyThree= (newTemp * 100)/100

    return simplifyThree




inputOne = int(input("Please enter a radius: "))

print(areaOfCircle(inputOne))


inputTwo = int(input("Please enter your money: "))
inputThree = int(input("Please enter your tax amount"))

print(totalDue(inputTwo, inputThree))


inputFour = int(input("What's the Farenheit: "))

print(differTemp(inputFour))








