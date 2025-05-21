print("Welcome to treasure island. Your mission is to find the treasure")
a = input("left or right? ").lower()
if a == "left":
    b = input("Swim or wait? ").lower()
    if b == "wait":
        c = input("Which door? ").lower()
        if c == "red":
            print("Burned by fire. Game over.")
        elif c == "blue":
            print("Eaten by beasts. Game over.")
        elif c == "yellow":
            print("You win!")
        else:
            print("Game over!")
    else:
        print("Attacked by trout. Game over.")
else:
        print("fall into a hole. Game over. ")
