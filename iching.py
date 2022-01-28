i, j, coin, seq = 0, 6, 0, []
print("Grab a coin that is on your wallet for more than 2 weeks and throw it six times, answering the head or tails question." )
while i < j and coin < 2:
    coin = int(input("Head[0] or Tails[1]: "))
    if coin == 0:
        seq.append(0)
    elif coin == 1:
        seq.append(1)
    else:
        print("Only 1 or 0.")
        i -= 1
        coin = 0
    i += 1

#1st Trigram
if seq[0] == 0:
    print("___")
    if seq[1] == 0:
        print("___")
        if seq[2] == 0:
            print("___")
            t1 = "Qian (Heaven)"
        else:
            print("_ _")
            t1 = "Xun (Wind)"
    else:
        print("_ _")
        if seq[2] == 0:
            print("___")
            t1 = "Li (Fire)"
        else:
            print("_ _")
            t1 = "Gen (Mountain)"
else:
    print("_ _")
    if seq[1] == 0:
        print("___")
        if seq[2] == 0:
            print("___")
            t1 = "Dui (Lake)"
        else:
            print("_ _")
            t1 = "Kan (Water)"
    else:
        print("_ _")
        if seq[2] == 0:
            print("___")
            t1 = "Zhen (Thunder)"
        else:
            print("_ _")
            t1 = "Kun (Earth)"
print(t1)
print("")

#2nd Trigram
if seq[3] == 0:
    print("___")
    if seq[4] == 0:
        print("___")
        if seq[5] == 0:
            print("___")
            t2 = "Qian (Heaven)"
        else:
            print("_ _")
            t2 = "Xun (Wind)"
    else:
        print("_ _")
        if seq[5] == 0:
            print("___")
            t2 = "Li (Fire)"
        else:
            print("_ _")
            t2 = "Gen (Mountain)"
else:
    print("_ _")
    if seq[4] == 0:
        print("___")
        if seq[5] == 0:
            print("___")
            t2 = "Dui (Lake)"
        else:
            print("_ _")
            t2 = "Kan (Water)"
    else:
        print("_ _")
        if seq[5] == 0:
            print("___")
            t2 = "Zhen (Thunder)"
        else:
            print("_ _")
            t2 = "Kun (Earth)"
print(t2)
print("")
