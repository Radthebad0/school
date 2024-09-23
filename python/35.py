#Average Temperature
print("please enter the seven temperatures.")
one=int(input())
two=int(input())
three=int(input())
four=int(input())
five=int(input())
six=int(input())
seven=int(input())

temp=one+two+three+four+five+six+seven
temperatures=temp/7

print("this week's average")
print("rounder to 0 decimal places was:")
print(round(temperatures, 0),"degrees centigrade")
