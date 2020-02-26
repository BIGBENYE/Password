import random
password = []

lowercaselist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
capitallist = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numberlist = ["0","1","2","3","4","5","6","7","8","9"]
symbollist = ["!","@","#","$","%","&","*"]


def print():
    length = input("How long do you want your password to be?")
    passlength = int(length)
    caps = input("How many capitals do you want it to have?")
    passcaps = int(caps)
    numbers = input("How many numbers do you want it to have?")
    passnumbs = int(numbers)
    symbols = input("How many symbols do you want it to have?")
    passsym = int(symbols)
    for I in range(int(caps)):
        randcap = random.choice(capitallist)
        password.append(randcap)
    for I in range(int(numbers)):
        randnum = random.choice(numberlist)
        password.append(randnum)
    for I in range(int(symbols)):
        randsym = random.choice(symbollist)
        password.append(randsym)

