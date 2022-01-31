i, j, seq, seq2 = 0, 6, [], []
print("Toss three coins at the same time six times, answering the head or tails question." )
while i < j:
    head = int(input("Number of coins that turned head: "))
    tails = int(input("Number of coins that turned tails: "))
    if head + tails == 3:
        head = head*3
        tails = tails*2
        line = head + tails
        seq.append(line)
        i = i +1
    else:
        print("You need to toss THREE coins.")
    print("")

#Present Hexagram
print("Present Hexagram:")
for x in seq:
    if x == 9:
        h = ("___")
    elif x == 8:
        h = ("_ _")    
    elif x == 7:
         h = ("___")
    else:
        h = ("_ _")
    print(h)
print("")
#Future Hexagram
print("Future Hexagram:")
for x in seq:
    if x == 9:
        h = ("_ _")
    elif x == 8:
        h = ("_ _")
    elif x == 7:
         h = ("___")
    else:
        h = ("___")
    print(h)
