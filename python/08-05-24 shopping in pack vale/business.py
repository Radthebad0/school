import sys
business_name=[]
business_owner=[]
phone_number=[]
email=[]
discount_day=[]
free_delivery=[]
2for1=[]

a="\t"
business_name=input("what is the name of the business? ")
business_owner=input("who is the owner of the business? ")
phone_number=int(input("what is the phone number of the business? "))
email=input("what is the email of the business? ")
discount_day=input("what are the dates of the discount? ")
free_delivery=input("what are the dates of the free delivery? ")
2for1=input("what product are under the offer? ")

file=open("members.txt", "a")
file.write(business_name + business_owner + phone_number + email + discount_day + free_delivery + 2for1)
file.write("\n")
