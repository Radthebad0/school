print("rectangle 1")
length_1=int(input("please enter the length:"))
width_1=int(input("please enter the width:"))

rectangle_1=length_1*width_1

print("rectangle 2")
length_2=int(input("please enter the length:"))
width_2=int(input("please enter the width:"))

rectangle_2=length_2*width_2

if rectangle_1 >= rectangle_2:
    print("rectangle 1 has the largest area")
else:
    print("rectangle 2 has the largest area")
