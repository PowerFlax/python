import time

respond = 'Y'
cpt = 0;

while(respond == 'Y'):
    cpt += 1
    timer = int(input("select the time to begin the countdown with (in seconds)"))

    while timer < 0:
        timer = int(input("the time should be a positive value"))

    for i in range(timer,0,-1):
        print(i)
        time.sleep(1)

    print("This is it, wanna play it again ?")

    respond = input("Yes or No ?")
    if(respond == "Yes"):
        respond = 'Y'
        print("Alright, preparing the system again...")
        time.sleep(3)
    else:
        respond = 'N'
        print("See you next time !")

        if (cpt == 1):
            print("You played the countdown " + str(cpt) + " single time")
        else:
            print("You played the countdown " + str(cpt) + " times")

"""
name = input("What's your name ?")
age = int(input("What's your age ?"))

if age >= 18:
    print("Since you have " + str(age) + " you should be an adult")

elif age > 0:
    print("Since you have " + str(age) + " you should be a kid")
else:
    while not (age > 0):
        print("Uncorrect number " + name + ", try again")
        age = age = int(input("What's your age ? (age must be at least above 0)"))


experience = input("What experience do you have ? (in less than 15 characters)")
selected = True

length = len(experience)


if(experience.lower() == "none"):
    print("then you're not selected")
    selected = False

while length > 15:
    print(name+", You are not respecting the characters limitations")

if(selected):
    print(name + " have been selected")
else:
    print(name + " have not been selected")
"""""