from colorama import Fore, Back, Style
i, j, seq, seq2 = 0, 6, [], []

#Display Fo-Hi
f = open("yinyang.txt", "r")
print(f.read())
f.close()

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

#Present Hexagram
print("Present Hexagram:")
for x in seq:
    if x == 9:
        h = (" ________________\n/________________/")
    elif x == 8:
        h = (" _______   _______\n/_______/ /_______/")    
    elif x == 7:
         h = (" ________________\n/________________/")
    else:
        h = (" _______   _______\n/_______/ /_______/")
    print(h)
print("")
#Future Hexagram
print("Future Hexagram:")
for x in seq:
    if x == 9:
        h = (" _______   _______\n/_______/ /_______/")
    elif x == 8:
        h = (" _______   _______\n/_______/ /_______/")
    elif x == 7:
         h = (" ________________\n/________________/")
    else:
        h = (" ________________\n/________________/")
    print(h)
