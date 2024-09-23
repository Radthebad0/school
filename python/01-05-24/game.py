import sys


def left():
    print("you have chosen left. unfortunetly you have walked in to the beast.")
    sys.exit()

def right():
    print("you have chosen right. you have enconted some building and you enter the building to try and hid from the beast.")
    sys.exit()
    
menu='''There is a mosnster loose in a wood. you come to a crossing. do you take the
a - left turning.
b - right turing.'''
print(menu)
crossing=input("which direction do you take? ")
if crossing=="a":
    left()
else:
    right()
