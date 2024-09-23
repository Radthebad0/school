passed = False

while passed == False:
    y_n=input('Do you want advice? (y/n)')

    if y_n == "y":
         passed = True
    

    elif y_n == "n":
        print("don't be silly. you definitely need advice!")

        
    else:
        print("Invalid y/n")

print("Don't feed the trolls")
