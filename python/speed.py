#
speed=int(input("enter speed "))
distances=int(input("enter distance "))

dist = 0

if speed<=20:
    dist=6
elif speed>=30:
    dist=14
elif speed>=40:
    dist=24
elif speed>=50:
    dist=38
elif speed>=60:
    dist=55
elif speed>=70:
    dist=75

if distances >= dist:
    print("fail")
elif distances <= dist:
    print("pass")
