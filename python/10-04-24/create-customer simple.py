import sys
title= []
fname= []
sname= []
housestreet= []
town= []
phone= []
email= []
membership= []
age= []
firstname= "firstname"
lastname= "lastname"
a="\t"
title=input("please enter your title Mr Mrs Ms Dr Other ")
fname=input("enter your first name ")
sname=input("enter your surname ")
housestreet=input("please enter your house street ")
town=input("please enter your postcode ")
phone=input("please enter your phone number ")
email=input("please enter your email ")
membership=input("please enter your type of membership Child personal family OAP ")
age=input("please enter your age ")
file=open("members.txt", "a")
file.write(firstname + a + fname + a + lastname + a + sname)
file.write("\n")
file.close()
