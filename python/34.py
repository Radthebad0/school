
total = 0
presents = []

while total <= 200:
    price=int(input("enter the price of the presents "))
    total += price
    presents.append(price)

    if total >= 200:
        print("limit Exeeded")
        print("can't include the",price) 

print("total spent: £", total)
print("presents bought;", presents)

