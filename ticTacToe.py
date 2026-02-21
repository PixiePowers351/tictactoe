print("My first actual program in Python:")
print("Tic-Tac-Toe")
print("Developed by Numa Bashaar in 2 days.")
print("31/3/2021")
print("---------------------------------------")

i = "y"

a1 = "a1"
a2 = "a2"
a3 = "a3"
b1 = "b1"
b2 = "b2"
b3 = "b3"
c1 = "c1"
c2 = "c2"
c3 = "c3"

userS = 0
USERs = 0

print()
print("Hi! What is your name?")
userN = input()

print()        
print("Hi", userN,"! Enter x or o.")
userc = input()

while userc != "x" and userc != "o":
    print()
    print("Enter either x or o.")
    userc = input()


if userc == "x":
    USERc = "o"
else:
    USERc = "x"

usert = ""
USERt = ""

winner = ""

print()
print("Pass the device to player 2.")
input("Press enter")

print()
print("Hi! What is your name?")
USErN = input()
print("Hi", USErN,"!")

while i == "y":
    print()
    print("---------------------------")
    print("Are you ready? Let's begin!")

    while a1 == "a1"  or a2 == "a2" or a3 == "a3" or b1 == "b1" or  b2 == "b2" or b3 == "b3" or c1 == "c1" or c2=="c2" or c3=="c3":

        print()
        print(a1, "/", a2, "/", a3)
        print("-------------")
        print(b1, "/", b2, "/", b3)
        print("-------------")
        print(c1, "/", c2, "/", c3)
        print()

        print("Enter a position,", userN,".")
        usert = input()
        
        while (usert != "a1" and usert != "a2" and usert != "a3" and usert != "b1" and usert != "b2" and usert != "b3" and usert != "c1" and usert != "c2" and usert != "c3") or (usert == "a1" and (a1 == USERc or a1 == userc)) and (usert == "b1" and (b1 == USERc or b1 == userc)) and (usert == "c1" and (c1 == USERc or c1 == userc)) and (usert == "a2" and (a2 == USERc or a2 == userc)) and (usert == "b2" and (b2 == USERc or b2 == userc)) and (usert == "c2" and (c2 == USERc or c2 == userc)) and (usert == "a3" and (a3 == USERc or a3 == userc)) and (usert == "b3" and (b3 == USERc or b3 == userc)) and (usert == "c3" and (c3 == USERc or c3 == userc)):
            print()
            print("Enter a valid position displayed above.")
            usert = input()

        if usert == "a1":
            a1 = userc
        elif usert == "a2":
            a2 = userc
        elif usert == "a3":
            a3 = userc
        elif usert == "b1":
            b1 = userc
        elif usert == "b2":
            b2 = userc
        elif usert == "b3":
            b3 = userc
        elif usert == "c1":
            c1 = userc
        elif usert == "c2":
            c2 = userc
        elif usert == "c3":
            c3 = userc

        
        print()
        print(a1, "/", a2, "/", a3)
        print("-------------")
        print(b1, "/", b2, "/", b3)
        print("-------------")
        print(c1, "/", c2, "/", c3)
        print()
        
        if a1 == userc == b1  == c1:
            winner = userN
        elif a2 == userc == b2  == c2:
            winner = userN
        elif a3 == userc  == b3  == c3:
            winner = userN
        elif a1 == userc == a2 == a3:
            winner = userN
        elif b1 == userc == b2 == b3:
            winner = userN
        elif c1 == userc == c2 == c3:
            winner = userN
        elif a1 == userc == b2 == c3:
            winner = userN 
        elif a3 == userc == b2 == c1:
            winner = userN
        
        if winner == userN:
            userS = userS + 1
            break
        
        print("Enter a position,", USErN)
        USERt = input()

        while USERt != "a1" and USERt != "a2" and USERt != "a3" and USERt != "b1" and USERt != "b2" and USERt != "b3" and USERt != "c1" and USERt != "c2" and USERt != "c3":         
            print()
            print("Enter a valid position displayed above.")
            USERt = input()

        if USERt == "a1":
            a1 = USERc
        elif USERt == "a2":
            a2 = USERc
        elif USERt == "a3":
            a3 = USERc
        elif USERt == "b1":
            b1 = USERc
        elif USERt == "b2":
            b2 = USERc
        elif USERt == "b3":
            b3 = USERc
        elif USERt == "c1":
            c1 = USERc
        elif USERt == "c2":
            c2 = USERc
        elif USERt == "c3":
            c3 = USERc
        
        if a1 == USERc == b1 == c1:
            winner = USErN
        elif a2 == USERc == b2 == c2:
            winner = USErN
        elif a3 == b3 == c3 == USERc:
            winner = USErN
        elif a1 == USERc == a2 == a3:
            winner = USErN
        elif b1 == USERc == b2 == b3:
            winner = USErN
        elif c1 == USERc == c2 == c3:
            winner = USErN
        elif a1 == USERc == b2 == c3:
            winner = USErN
        elif a3 == USERc == b2 == c1:
            winner = USErN
        
        if winner == USErN:
            USERs = USERs + 1
            break
        
    print()
    print(a1, "/", a2, "/", a3)
    print("-------------")
    print(b1, "/", b2, "/", b3)
    print("-------------")
    print(c1, "/", c2, "/", c3)
    print()

    if winner == "":
        print("It's a tie!")
    else:
        print(winner, "wins!")
        print()
        print(userN,":", userS,",", USErN,":", USERs)
    

    print()
    print("Would you like to play again? (y/n)")
    i = input()

    while i  != "y" and i != "n":
        print()
        print("Enter either y for yes or n for no")
        i = input()

    if i == "y":
        a1 = "a1"
        a2 = "a2"
        a3 = "a3"
        b1 = "b1"
        b2 = "b2"
        b3 = "b3"
        c1 = "c1"
        c2 = "c2"
        c3 = "c3"
        winner = ""
    
    if i == "n":
        break

print()
input("press enter to exit")
