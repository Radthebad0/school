print("Please enter the following values in cm.")
radius=int(input("Please enter the radius of the circle."))
            
area=3.14*radius*radius

print("The area of the circle is:",area,"square centimetres")

import threading
import time
  
def print_project():
    for i in range(500):

        time.sleep(100)
        print("project")
  
