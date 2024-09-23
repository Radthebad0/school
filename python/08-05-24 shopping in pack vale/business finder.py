date=[]
data=str(input("search by firsts name or surname"))
userFile=open("buniess.txt", "r")
filefound=False

for line in userFile:
    if data in line:
        fileFound=true
        printline
else:
    if fileFound==False:
        print("not in file")
