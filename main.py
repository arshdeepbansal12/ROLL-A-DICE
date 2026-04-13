from dice import dice
from exit import exit

print("""===== WELCOME TO THE GAME OF LUCK =======
 ===== WANNA TRY YOUR LUCK ?? ======""")
print("""\n===== PRESS THE NUMBER TO CONTINUE ======\n""")
print("GO :[1]")
print("EXIT :[2]")

while True:
    a = int(input("\n>>>"))
    if a == 1:
        print(dice())
        print(""" ===== WANNA TRY YOUR LUCK AGAIN ?? ======""")
    elif a == 2:
        exit()
    else:
       print("INVALID INPUT")
       print("GO :[1]")
       print("EXIT :[2]\n")
       continue