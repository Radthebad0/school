print('house floor plan area calculator')
amount = []
amount = int(input('please enter the number of rooms '))
i=1
max_area = 0
min_area = 99999999999999999999999999999
totalarea = 0
while i <= amount:
    length = int(input('Please enter the length(m) of room ' + str(i) + ' '))
    width = int(input('please enter the width(m) of room ' + str(i) + ' ')) 

    area = length * width
    
    i = i + 1
    totalarea = totalarea + area
    if area > max_area:
        
        max_area = area
    if area<min_area:
        min_area = area
    print("the output would be")
    print("the total are is calculated as")
    print('room',i)
    print(area,length,'x',width)
print('biggest area is',max_area)
print('the smallest area',min_area)

print('total area is',area)
