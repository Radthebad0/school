print('the following program will display odd numbers.')
one=int(input('Enter the first number in the list '))
two=int(input('Enter the last number in the list '))

start, end = one, two
 
# iterating each number in list
for num in range(start, end + 1):
     
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")
