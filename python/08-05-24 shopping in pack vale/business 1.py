import sys
business_number=[]
business_name=[]
business_owner=[]
phone_number=[]
email=[]
discount_day=[]
free_delivery=[]
product_for_1=[]

a="\t"
business_number=input("what is the business number? ")
business_name=input("what is the name of the business? ")# asking for the name
business_owner=input("who is the owner of the business? ")# asking for the owner
phone_number=int(input("what is the phone number of the business? "))# asking for the phone number
email=input("what is the email of the business? ")# asking for the email
discount_day=input("what are the dates of the discount? ")# what days are under the offer
free_delivery=input("what are the dates of the free delivery? ")# what date have free delivery
product_for_1=input("what product are under the offer? ")# asking what product are under the offer

file=open("business.txt", "a") #opeing the main file buniess.txt
file.write(business_name + a + business_owner + a + str(phone_number) + a + email + a + discount_day + a + free_delivery + a + product_for_1) # writing to the main storage file buniess.txt
file.write("\n") # adding a blank line to the file
file.close() # closing the file
