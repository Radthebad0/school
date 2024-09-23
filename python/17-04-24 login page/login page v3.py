        #authenication v1
from time import sleep
import sys


def authentication():
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

    sleep(5)

    sys.exit()

authentication()
