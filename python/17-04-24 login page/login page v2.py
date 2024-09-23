#authenication v1
from time import sleep
import sys

def calculater():
    num1=int(input("enter first number "))
    num2=int(input("enter secound number "))
    total=num1+num2
    print("the total = " , total)
notifitcation='''
***************************
*Authenitication procedure*
***************************
\n '''
print(notifitcation)
name_user="root"
user_password="admin"
user_name=input("what is your user name? ")
password=input("what is your password? ")

if user_name==name_user and password==user_password:
    sleep(3)
    print("welcome")
    calculater()

else:
    sleep(3)
    print("access denied")

    sleep(1)
    print("Goodbye")
    
    sleep(2)
    
    sys.exit()
print("have a nice day")
