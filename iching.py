from colorama import Fore, Back, Style
import random
i, j, seq, seq2 = 0, 6, [], []

def name_trigram(seq2):
    if seq2[0] == 1:
        if seq2[1] == 1:
            if seq2[2] == 1:
                phname = "Qián (Heaven)"
            else:
                phname = "Xùn (Wind)"
        else:
            if seq2[2] == 1:
                phname = "Lí (Fire)"
            else:
                phname = "Gèn (Mountain)"
    else:
        if seq2[1] == 1:
            if seq2[2] == 1:
                phname = "Dui (Lake)"
            else:
                phname = "Kǎn (Water)"
        else:
            if seq2[2] == 1:
                phname = "Zhèn (Thunder)"
            else:
                phname = "Kūn (Earth)"
    seq2 = []
    print(phname)

#Display Fo-Hi
f = open("yinyang.txt", "r")
print(f.read())
f.close()

choose = int(input("Wich method do you want to use?\nThe coins [0] or Random fortune [1]?"))
if choose == 0:
    print("Toss three coins at the same time six times, answering the head or tails question." )
    while i < j:
        print("Throw #", (i+1))
        head = int(input("Number of coins that turned head: "))
        tails = int(input("Number of coins that turned tails: "))
        if head + tails == 3:
            head = head*3
            tails = tails*2
            line = head + tails
            seq.append(line)
            i = i +1
        else:
            print(Fore.RED + " '\033[1m' You need to toss THREE coins. '\033[1m'")
            print(Style.RESET_ALL)
        print("")
else:
    for n in range(6):
        head, tails, line = 0, 0, 0
        for m in range(3):
            coin = random.randint(0,1)
            if coin == 1:
                head = head + 3
            else:
                tails = tails + 2
        line = head + tails
        seq.append(line)

#Present Hexagram
print("Present Hexagram:")
loop = 0
for x in seq:
    if x == 9:
        h = (" ________________\n/________________/")
        seq2.append(1)
    elif x == 8:
        h = (" _______   _______\n/_______/ /_______/")
        seq2.append(0)
    elif x == 7:
         h = (" ________________\n/________________/")
         seq2.append(1)
    else:
        h = (" _______   _______\n/_______/ /_______/")
        seq2.append(0)
    print(h)
    if loop == 2 or loop == 5:
        name_trigram(seq2)
        seq2 = []
    loop = loop + 1
print("")
#Future Hexagram
print("Future Hexagram:")
loop = 0
for x in seq:
    if x == 9:
        h = (" _______   _______\n/_______/ /_______/")
        seq2.append(0)
    elif x == 8:
        h = (" _______   _______\n/_______/ /_______/")
        seq2.append(0)
    elif x == 7:
         h = (" ________________\n/________________/")
         seq2.append(1)
    else:
        h = (" ________________\n/________________/")
        seq2.append(1)
    print(h)
    if loop == 2 or loop == 5:
        name_trigram(seq2)
        seq2 = []
    loop = loop + 1
