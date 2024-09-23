import sys
fname=[]
sname=[]
year=[]
wclass=[]
age=[]
a="\t"
fname=input("Enter your name ")
sname=input("Enter your surname ")
year=input("Enter your school year ")
wclass=input("Enter your class ")
age=input("Enter you age ")

file=open("name.txt","a")
file.write(fname + a + sname + a + year +a+ wclass +a+ age)
file.write("\n")
file.close()
/
