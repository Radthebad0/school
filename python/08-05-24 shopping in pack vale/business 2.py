import sys

business_name=[]
business_owner=[]
phone_number=[]
email=[]
discount_day=[]
free_delivery=[]
product_for_1=[]
find2=1
create1=2
test=[]
postcode=[]
address=[]
yes_no=[]

def find():

    test=str(input("Please type the name of the business or the id code of the business "))

    with open(r"business.txt", 'r') as fp:
        for l_no, line in enumerate(fp):
            # search string
            if test in line:
                print('Line Number:', l_no)
                print('Line:', line)
                # don't look for next lines
                


def create():

    import random

    for i in range(1):
            y = random.uniform(0000000000000, 999999999999)
            New_Number = int(y)

	


    
    a="\t"
    business_name=input("what is the name of the business? ")# asking for the name
    business_owner=input("who is the owner of the business? ")# asking for the owner
    phone_number=int(input("what is the phone number of the business? "))# asking for the phone number
    email=input("what is the email of the business? ")# asking for the email
    discount_day=input("what are the dates of the discount? ")# what days are under the offer
    free_delivery=input("what are the dates of the free delivery? ")# what date have free delivery
    product_for_1=input("what product are under the offer 2 for 1? ")# asking what product are under the offer
    postcode=input("what is the post code of the business? ")#asking for the postcode of the business
    address=input("what is the address of the buiness? ")#asking for the address of the buiness

    file=open("business.txt", "a") #opeing the main file buniess.txt
    file.write("business id" + a + str(New_Number) + a + "business name" + a + business_name + a + "business owner" + a + business_owner + a + "phone number" + a + str(phone_number) + a + "email" + a + email + a + "discount day" + a + discount_day + a + "free delivery" + a +  free_delivery + a +  "2for1" + a + product_for_1 + a + "postcode" + a + postcode + a + "address" + a + address) # writing to the main storage file buniess.txt
    file.write("\n") # adding a blank line to the file
    file.close()
    print("the save was successful")
    print("the id number is" + a + str(New_Number) )
    
    
for x in range(99999):
    choise=input("what are you trying to do find/create type 1/2 ")
    if choise == "1":
        find()

        break
    if choise == "2":
        create()
        break
       
    
