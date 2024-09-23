raisers=int(input('how many charity were there? '))
print('Enter the total raised by each: ')



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
