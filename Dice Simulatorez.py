# import random module
import random

# import time module
import time



con = "Y"

while con == "Y":
   # pick a random number between 1 to 6 cause dice has number from 1 to 6 only
   a = random.randint(1, 7)
   if a == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
   elif a == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
   elif a == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
   elif a == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
   elif a == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
   elif a == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
   print("")
   # make the code below this command execute only after some seconds inputed
   time.sleep(0.75)

   # This code will only execute after the inputed seconds
   con = str.upper(input("--------Do you wanna roll again? ( Y / N ) \n >>"))
