#authenication v1
from time import sleep

name_user="root"
user_password="admin"
user_name=input("what is your user name? ")
password=input("what is your password? ")

if user_name==name_user and password==user_password:
    sleep(3)
    print("welcome")
    

else:
    sleep(3)
    print("access denied")
