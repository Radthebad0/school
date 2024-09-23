one=int(input("Please enter the first amount raised. "))
two=int(input("Please enter the secound amount raised. "))
three=int(input("Please enter the third amount raised. "))

total=one+two+three
print ("A total of",total,"was raised")

if total > 1000:
    total_1=total+100
else:
    total_1=total

if total_1 <= 2000:
    total_2=total_1*2
else:
    total_2=total_1

if total_2 > 2000:
    total_last=total_2+2000
else:
    total_last=total_2

print("With the company bonus, this is",total_last)
