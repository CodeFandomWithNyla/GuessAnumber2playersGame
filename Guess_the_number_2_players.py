import random


# baari function randomly selects a number and ask that to guess from player
def baari(x):
    com = random.choice(range(a,b))  
    print(f"\nPLAYER {x} Turn :\n")
    player = 0
    i = 0
    while player != com:
        player = int(input(f"Enter a number between {a} and {b} :\t"))
        if player < com: print("Choose a greater number")
        else: print("Choose a smaller number")
        i+=1
    return i

# Main program starts from here.....
print("*** WELCOME TO THE NUMBER GAME ***")
try:
    a = int(input("Please enter lower bound of the range :\t"))
    b = int(input("Please enter the upper bound of the range :\t"))
    if a > b :
        a, b = b, a
    chances1 = 0
    chances2 = 0    
    while chances1 ==0 or chances2 == 0:              
        chances1 = baari(1)
        print(f"\nPlayer 1 took {chances1} chances to guess the number")
        chances2 = baari(2)
        print(f"\nPlayer 2 took {chances2} chances to guess the number")
        if chances1 < chances2:
            print("\n\n\tPlayer 1 is the WINNER !!!")
            break
        elif chances2 < chances1:
            print("\n\n\tPlayer 2 is the WINNER !!!")
            break
        else:
            print("Both players have lost this game !!!")
   
except Exception as e:
    print("Only numbers are allowed !\n", e)
    
