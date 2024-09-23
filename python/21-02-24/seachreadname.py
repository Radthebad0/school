data=[]
data=str(input("Search by first name or surname "))
userFile=open("names.txt","r")
filefound=False

for line in userFile:
    if data in line:
        filefound=True
        print(line)
        
if filefound==False:
    print("not in file")

        
