import random

alpha = ["a","b","c","d","e","f","g","h","i","j","k"] #list of alphabets
respond = True


while respond:
    password = ""
    for i in range(0, 1):
        for j in (alpha):
            capitalisation = random.randint(0, 1)#it can be a capital letter(1), or not(0).
            if (capitalisation == 1):
                j = j.upper()  # just so you can have some capital letters too
            password = str(password) + random.choice(alpha) + j #a combination for the password, i might add some integers too hmm...

    print("Your password is: " + password)
    yon = input("Whould you like to regenerate a new password? (Y for Yes, N for No)") #yes or no variable
    while not(yon == "N" or yon == "Y"):
        yon = input("Please enter a valid value. (Y for Yes, N for No)")
        if(yon == "N"):
            respond = False
            break

        if(yon == "Y"):
            break

    if (yon == "N"):
        respond = False
        break

