temp=int(input("what is the temperture "))
gas=100
liquid=1
solid=0
if temp >= gas:
    print ("at",temp,"degrees centigrade,","water will be a gas")
elif temp > 0 and temp < 100:
    print ("at",temp,"degrees centigrade,","water will be liquid")
else:
    print ("at",temp,"degrees centigrade,","water will be solid")
