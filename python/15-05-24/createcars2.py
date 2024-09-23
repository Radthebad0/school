import sys
title=[]
fname=[]
a="\t"


def create():
    make=input("enter the make ")
    model=input("enter the model ")
    price=input("enter the price ")
    fuel=input("enter the fuel ")
    transission=input("enter the transission ")
    milage=input("enter the milage ")
    year=input("enter the year ")
    colour=input("enter the colour ")
    
    
    
    file=open("datacars.txt","a")
    file.write(make + " " + model + " " + price + " " + fuel + " " + transission + " " + milage + " " + year + " " + colour)
    file.write("\n")
    file.close()

    print("done ")

def find():

    data=[]

    data=input("Please type the make of the car ")
    userfile=open("datacars.txt","r")
    filefound=false

    for line in userfile:
        if data in line:
            filefound=true

            
              

for x in range(99999):
    choise=input("what are you trying to do find/create type 1/2 ")
    if choise == "1":
        find()
        break
    if choise == "2":
        create()
        break


