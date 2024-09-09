from PIL import Image
import random
end=100

def show_board():
    img=Image.open('s&L.jpg')
    img.show()

def check_snake(points):
    if(points==17):
        print("Snake")
        return 7
    elif(points==62):
        print("Snake")
        return 19
    elif(points==54):
        print("Snake")
        return 32
    elif(points==87):
        print("Snake")
        return 36
    elif(points==64):
        print("Snake")
        return 60
    elif(points==93):
        print("Snake")
        return 73
    elif(points==95):
        print("Snake")
        return 75
    elif(points==98):
        print("Snake")
        return 79
    else:
        return points #not a snake
def check_ladder(points):
    if(points==1):
        print("Ladder")
        return 38
    elif(points==4):
        print("Ladder")
        return 14
    elif(points==9):
        print("Ladder")
        return 31
    elif(points==21):
        print("Ladder")
        return 42
    elif(points==28):
        print("Ladder")
        return 84
    elif(points==51):
        print("Ladder")
        return 67
    elif(points==72):
        print("Ladder")
        return 91
    elif(points==80):
        print("Ladder")
        return 99
    else:
        return points #not a ladder
def reached_end(points):
    if(points==end):
        return True
    else:
        return False
def play():
#     input player-1 name
    player_1=input("Player_1 , Please enter your name:")
#     input player-1 name
    player_2=input("Player_2 , Please enter your name:")
#     initial points for player-1 and player-2 are set to zero
    p1=0
    p2=0
    
    turn=0
    while(1):   #infinite loop
        if(turn%2==0):  #player-1 have even turns
            print(player_1,"'s turn")
            c=int(input("Select 1 to continue and 0 to quit:"))
            if(c==0):
                print(player_1,'scored ',p1)
                print(player_2,'scored ',p2)
                print('Game over! \n THANKS FOR PLAYING!')
                break
            dice=random.randint(1,6)   #Generates random number from 1 to 6
            print("Dice roll: ",dice)
            if p1 + dice <= end:  # Only add dice if it doesn't exceed 100
                p1 += dice
            p1=check_ladder(p1)
            p1=check_snake(p1)
            print(f"{player_1}'s current score: {p1}")  # Print player 1's score
            if(p1>end):
                p1=end
                print(player_1,'Your score: ',p1)
            if(reached_end(p1)):
                print(player_1,'won the game')
                break                
                
        else: #player2 has odd turns
            print(player_2,"'s turn")
            c=int(input("Select 1 to continue and 0 to quit"))
            if(c==0):
                print(player_1,'scored ',p1)
                print(player_2,'scored ',p2)
                print('Game over! \n THANKS FOR PLAYING!')
                break
            dice=random.randint(1,6)   #Generates random number from 1 to 6
            print("Dice roll:",dice)
            if p2 + dice <= end:  # Only add dice if it doesn't exceed 100
                p2 += dice
            p2=check_ladder(p2)
            p2=check_snake(p2)
            print(f"{player_2}'s current score: {p2}")  # Print player 2's score
            if(p2>end):
                p2=end
                print(player_2,'Your score: ',p2)
            if(reached_end(p2)):
                print(player_2,'won the game')
                break
        turn=turn+1
show_board()
play()
