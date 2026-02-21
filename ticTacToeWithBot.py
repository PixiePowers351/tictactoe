import time
import os
import keyboard
import random

userScore = 0
compScore = 0

token = ['🧡', '💛', '💚', '💙', '💜' ]

seed = random.randint(0,len(token)-1)
userToken = token[seed]
token.pop(seed)
seed = random.randint(0,len(token)-1)
compToken = token[seed]

def view(timeS):
    os.system('cls')
    try:
        if userScore / (userScore+compScore) > (0.9):
            print(f"{userToken}{userToken}{userToken}")
        elif userScore / (userScore+compScore) >= (0.5):
            print(f"{userToken}{userToken}{compToken}")
        elif userScore / (userScore+compScore) > (1/3):
            print(f"{userToken}{compToken}{compToken}")
        else:
            print(f"{compToken}{compToken}{compToken}")
    except:
        print("🖤🖤🖤")
    for x in range(0,3):
        display = ''
        for y in range(0,3):
            if x == userX and y == userY:
                if board[x][y] == 0:
                    display = display + '🔳'
                elif board[x][y] == 1:
                    display = display + '❎'
                elif board[x][y] == 2:
                    display = display + '🟢'
            else:
                if board[x][y] == 0:
                    display = display + '⬛'
                elif board[x][y] == 1:
                    display = display + '❌'
                elif board[x][y] == 2:
                    display = display + '⭕'
        print(display)
    time.sleep(timeS)

diagonal = ((0,2),(1,1),(2,0))

while userScore < 100 and compScore < 100:
    done = False
    userX = 0
    userY = 0 
    userC = random.randint(1,2)
    if userC == 1:
        compC = 2
    else:
        compC = 1
    board = [[0,0,0],[0,0,0],[0,0,0]]
    view(0.1)

    while done == False:
        if keyboard.is_pressed('up arrow') and userX - 1 >= 0:
            userX = userX - 1
            view(0.175)
        if keyboard.is_pressed('down arrow') and userX + 1 < 3:
            userX = userX + 1
            view(0.175)
        if keyboard.is_pressed('right arrow') and userY + 1 < 3:
            userY = userY + 1
            view(0.175)
        if keyboard.is_pressed('left arrow') and userY - 1 >= 0:
            userY = userY - 1
            view(0.175)

        if keyboard.is_pressed('space') and board[userX][userY] == 0:
            board[userX][userY] = userC
            view(0.175)
            move = False

            #check if the user won
            for x in range(0,3):
                c = 0
                for y in range(0,3):
                    if board[x][y] == userC:
                        c = c + 1
                if c == 3:
                    done = True
                    userX = -1
                    userY = -1
                    userScore = userScore + 1
                    view(0.1)
                    print("You win!!")
                    break

            for y in range(0,3):
                c = 0
                for x in range(0,3):
                    if board[x][y] == userC:
                        c = c + 1
                if c == 3:
                    userX = -1
                    userY = -1
                    userScore = userScore + 1
                    view(0.1)
                    print("You win!!")
                    done = True
                    break

            c = 0
            for x in range(0,3):
                if board[x][x] == userC:
                    c = c + 1
            if c == 3:
                userX = -1
                userY = -1
                userScore = userScore + 1
                view(0.1)
                print("You win!!")
                done = True
                break          
            
            c = 0
            for x in range(0,3):
                if board[diagonal[x][0]][diagonal[x][1]] == userC:
                    c = c + 1
            if c == 3:
                userX = -1
                userY = -1
                userScore = userScore + 1
                view(0.1)
                print("You win!!")
                done = True
                break    

            if done == True:
                break
            
            c = 0
            #check a winning move
            for x in range(0,3):
                if move:
                    break
                c = 0
                for y in range(0,3):
                    if board[x][y] == compC:
                        c = c + 1
                if c == 2:
                    for y in range(0,3):
                        if board[x][y] == 0:
                            board[x][y] = compC
                            move = True
                            break

            for y in range(0,3):
                if move:
                    break
                c = 0
                for x in range(0,3):
                    if board[x][y] == compC:
                        c = c + 1
                if c == 2:
                    for x in range(0,3):
                        if board[x][y] == 0:
                            board[x][y] = compC
                            move = True
                            break
            
            c = 0
            for x in range(0,3):
                if move:
                    break
                if board[x][x] == compC:
                    c = c + 1
            if c == 2:
                for x in range(0,3):
                    if board[x][x] == 0:
                        board[x][x] = compC
                        move = True
                        break
            
            c = 0
            for x in range(0,3):
                if move:
                    break
                if board[diagonal[x][0]][diagonal[x][1]] == compC:
                    c = c + 1
            if c == 2:
                for x in range(0,3):
                    if board[diagonal[x][0]][diagonal[x][1]] == 0:
                        board[diagonal[x][0]][diagonal[x][1]] = compC
                        move = True
                        break

            if move:
                view(0.175)

            #block move
            for x in range(0,3):
                if move:
                    break
                c = 0
                for y in range(0,3):
                    if board[x][y] == userC:
                        c = c + 1
                if c == 2:
                    for y in range(0,3):
                        if board[x][y] == 0:
                            board[x][y] = compC
                            move = True
                            break

            for y in range(0,3):
                if move:
                    break
                c = 0
                for x in range(0,3):
                    if board[x][y] == userC:
                        c = c + 1
                if c == 2:
                    for x in range(0,3):
                        if board[x][y] == 0:
                            board[x][y] = compC
                            move = True
                            break
            
            c = 0
            for x in range(0,3):
                if move:
                    break
                if board[x][x] == userC:
                    c = c + 1
            if c == 2:
                for x in range(0,3):
                    if board[x][x] == 0:
                        board[x][x] = compC
                        move = True
                        break

            c = 0
            for x in range(0,3):
                if move:
                    break
                if board[diagonal[x][0]][diagonal[x][1]] == userC:
                    c = c + 1
            if c == 2:
                for x in range(0,3):
                    if board[diagonal[x][0]][diagonal[x][1]] == 0:
                        board[diagonal[x][0]][diagonal[x][1]] = compC
                        move = True
                        break              
            if move:
                view(0.175)

            #check if all tiles are full
            draw = True
            for x in range(0,3):
                for y in range(0,3):
                    if board[x][y] == 0:
                        draw = False
                        break
            if draw:
                userX = -1
                userY = -1
                userScore = userScore + 0.5
                compScore = compScore + 0.5
                view(0.1)
                print("Draw!!")
                done = True
                break

            #random //if no optimal move
            while move == False:
                seed = (random.randint(0,2), random.randint(0,2))
                if board[seed[0]][seed[1]] == 0:
                    board[seed[0]][seed[1]] = compC
                    move = True
                    view(0.175)
                    break
            
            #check if the computer won
            for x in range(0,3):
                c = 0
                for y in range(0,3):
                    if board[x][y] == compC:
                        c = c + 1
                if c == 3:
                    userX = -1
                    userY = -1
                    compScore = compScore + 1
                    view(0.1)
                    print("You lose!!")
                    done = True
                    break

            for y in range(0,3):
                c = 0
                for x in range(0,3):
                    if board[x][y] == compC:
                        c = c + 1
                if c == 3:
                    userX = -1
                    userY = -1
                    compScore = compScore + 1
                    view(0.1)
                    print("You lose!!")
                    done = True
                    break

            c = 0
            for x in range(0,3):
                if board[x][x] == compC:
                    c = c + 1
            if c == 3:
                userX = -1
                userY = -1
                compScore = compScore + 1
                view(0.1)
                print("You lose!!")
                done = True
                break          
            
            c = 0
            for x in range(0,3):
                if board[diagonal[x][0]][diagonal[x][1]] == compC:
                    c = c + 1 
            if c == 3:
                userX = -1
                userY = -1
                compScore = compScore + 1
                view(0.1)
                print("You lose!!")
                done = True
                break
    time.sleep(0.1)
    input()


        

        



