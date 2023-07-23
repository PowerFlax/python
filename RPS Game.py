import random
import time

rps = ["R","P","S"]
choice = None
rounds = 0
score = 0
respond = True
yes_or_no = ""


print("----------------")
while respond:
    print("Preparing", end="")
    for i in range(0,3):
        print(".",end="")
        time.sleep(1)


    while rounds <3:

        print("\nRound number " + str(rounds+1))
        rand = random.choice(rps)
        choice = input("Rock, Paper or Scissors ? (Rock:R/Paper:P/Scissors:S)")
        while not(choice == "S" or choice == "P" or choice == "R"):
            print("That's not a valid value (R/P/S)")
            choice = input("Rock, Paper or Scissors ? (Rock:R/Paper:P/Scissors:S)")

        #Lose
        if(choice == "P" and rand == "S"  or (choice == "R" and rand == "P") or (choice == "S" and rand == "R")):
            print("Stats:")
            print(choice+" VS " + rand)
            print("You lost this round.")
        #Win
        elif(choice == "S" and rand == "P"  or (choice == "P" and rand == "R") or (choice == "R" and rand == "S")):
            print("Stats:")
            print(choice + " VS " + rand)
            print("You Won this round.")
            score += 1
        #Draw
        else:
            print("Stats:")
            print(choice + " VS " + rand)
            print("This is a draw.")

        print("----------------\n")
        rounds += 1


    print("Your current score: "+str(score))

    yes_or_no = input("Do you want to play again ?(respond by Y or N (Yes:Y // No:N)")
    if(yes_or_no == "Y"):
        respond = True
        rounds = 0
        print("----------")
    elif(yes_or_no == "N"):
        print("See you soon :)")
        break
    else:
        print("What do you mean by that ?")
        while not(yes_or_no == "Y" or yes_or_no == "N"):
            print("Please enter a valid value (Y/N)")
            yes_or_no = input("Do you want to play again ?(respond by Y or N (Yes:Y // No:N)")
            if (yes_or_no == "Y"):
                respond = True
                rounds = 0
                print("----------")
            elif (yes_or_no == "N"):
                print("See you soon :)")
                break

print("Your final score: "+str(score))