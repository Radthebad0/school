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

print("this week's average was:")
print(round(temperatures, 2),"degrees centigrade")
