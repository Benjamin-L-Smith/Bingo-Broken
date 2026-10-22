#the computer (enemy) would select a random spot that has not yet been selected.
#on your turn all of the points are yours, and on the enemy's turn they all belong to it.
#this was a bug I got while working on an actual bingo game, but I think it's kinda fun.

#numbers across, letters down

#the user can also use their numpad, but do note that the spaces align with where the numbers are on the numpad.
#ex: slot A1=7 or C3=3


import random

#these are for text colors:
norm = "\033[0m" #short for normal - resets color
blue = "\033[34m" #makes '☼' Blue
purple = "\033[35m" #makes 'x' Purple



#this is the one for if the player is x
def GameX(a1,b1,c1,a2,b2,c2,a3,b3,c3):
    if a1==True:
        oneA="x"
    else:
        oneA=" "
    if b1==True:
        oneB="x"
    else:
        oneB=" "
    if c1==True:
        oneC="x"
    else:
        oneC=" "
    if a2==True:
        twoA="x"
    else:
        twoA=" "
    if b2==True:
        twoB="x"
    else:
        twoB=" "
    if c2==True:
        twoC="x"
    else:
        twoC=" "
    if a3==True:
        threeA="x"
    else:
        threeA=" "
    if b3==True:
        threeB="x"
    else:
        threeB=" "
    if c3==True:
        threeC="x"
    else:
        threeC=" "
    print("---YOUR TURN---")
    print("   1  2  3")
    print(f"A [{oneA}][{twoA}][{threeA}]")
    print(f"B [{oneB}][{twoB}][{threeB}]")
    print(f"C [{oneC}][{twoC}][{threeC}]")

    gameSet=False
    #this is for ups/downs and lefts/rights
    if (oneA=="x" and twoA=="x" and threeA=="x") or (oneB=="x" and twoB=="x" and threeB=="x") or (oneC=="x" and twoC=="x" and threeC=="x") or (oneA=="x" and oneB=="x" and oneC=="x") or (twoA=="x" and twoB=="x" and twoC=="x") or (threeA=="x" and threeB=="x" and threeC=="x"):
        gameSet=True
    #this is for diagonals
    if (oneA=="x" and twoB=="x" and threeC=="x") or (threeA=="x" and twoB=="x" and oneC=="x"):
        gameSet=True
    return gameSet


def Game0(a1,b1,c1,a2,b2,c2,a3,b3,c3):
    if a1==True:
        oneA="☼"
    else:
        oneA=" "
    if b1==True:
        oneB="☼"
    else:
        oneB=" "
    if c1==True:
        oneC="☼"
    else:
        oneC=" "
    if a2==True:
        twoA="☼"
    else:
        twoA=" "
    if b2==True:
        twoB="☼"
    else:
        twoB=" "
    if c2==True:
        twoC="☼"
    else:
        twoC=" "
    if a3==True:
        threeA="☼"
    else:
        threeA=" "
    if b3==True:
        threeB="☼"
    else:
        threeB=" "
    if c3==True:
        threeC="☼"
    else:
        threeC=" "
    print("---ENEMY TURN---")
    print("   1  2  3")
    print(f"A [{oneA}][{twoA}][{threeA}]")
    print(f"B [{oneB}][{twoB}][{threeB}]")
    print(f"C [{oneC}][{twoC}][{threeC}]")

    gameSet=False
    #this is for ups/downs and lefts/rights
    if (oneA=="☼" and twoA=="☼" and threeA=="☼") or (oneB=="☼" and twoB=="☼" and threeB=="☼") or (oneC=="☼" and twoC=="☼" and threeC=="☼") or (oneA=="☼" and oneB=="☼" and oneC=="☼") or (twoA=="☼" and twoB=="☼" and twoC=="☼") or (threeA=="☼" and threeB=="☼" and threeC=="☼"):
        gameSet=True
    #this is for diagonals
    if (oneA=="☼" and twoB=="☼" and threeC=="☼") or (threeA=="☼" and twoB=="☼" and oneC=="☼"):
        gameSet=True
    return gameSet


def askForPlay(a1,b1,c1,a2,b2,c2,a3,b3,c3):
    if a1==False:
        a1="[1A], "
    else:
        a1=""
    if b1==False:
        b1="[1B], "
    else:
        b1=""
    if c1==False:
        c1="[1C], "
    else:
        c1=""
    if a2==False:
        a2="[2A], "
    else:
        a2=""
    if b2==False:
        b2="[2B], "
    else:
        b2=""
    if c2==False:
        c2="[2C], "
    else:
        c2=""
    if a3==False:
        a3="[3A], "
    else:
        a3=""
    if b3==False:
        b3="[3B], "
    else:
        b3=""
    if c3==False:
        c3="[3C]"
    else:
        c3=""
    if(a1=="" and a2=="" and a3=="" and b1=="" and b2=="" and b3=="" and c1=="" and c2=="" and c3==""):
            print("You have already entered all the choices! I don't know how you did that.")
    ask=input(f"Which slot do you want to claim?\n{a1}{b1}{c1}{a2}{b2}{c2}{a3}{b3}{c3}: ")
    return ask #this gets put into placement



#Fun Fact: if the user chooses 2B-or-5, they have a 100% oppurtunity to win the next round.

gameplayLoopCount=0 #tracks how many times the game has run
gameplayLoop=True
while(gameplayLoop==True):
    #☼ => alt+15
    if(gameplayLoopCount==0):
        print("This not true bingo.\nThe claimed slots are traded between yourself and the enemy every turn.\nYou can only win as 'X'.")
    start=(input("You are [x]\nReady to start? ")) #this is not tied to anything.
    userWin = False
    enemyWin = False
    turn=0 #determines if it's the user's turn or the enemy's
    recordPlaces=[] #this records what places the user has already been.
    recordEnemyPlaces=[] #this records what places the enemy has already been.
    #these are the variables that hold whether or not a slot is claimed:
    aOne=False
    bOne=False
    cOne=False
    aTwo=False
    bTwo=False
    cTwo=False
    aThree=False
    bThree=False
    cThree=False
    print("   1  2  3") #this is just here to display the initial board
    print("A [ ][ ][ ]")
    print("B [ ][ ][ ]")
    print("C [ ][ ][ ]")
    while(userWin==False and enemyWin==False):
        if(turn%2==0):
            #placement=(input("Which slot do you want to claim?\n[1A], [1B], [1C], [2A], [2B], [2C], [3A], [3B], [3C]: "))
            placement = askForPlay(aOne,bOne,cOne,aTwo,bTwo,cTwo,aThree,bThree,cThree)
            #this input needs the Continent treatment to determine if the user can choose that square or not.
            if(placement=='1' or placement=='2' or placement=='3' or placement=='4' or placement=='5' or placement=='6' or placement=='7' or placement=='8' or placement=='9'): #does not record the letters.
                recordPlaces.append(int(placement))
            if placement=='7' or 7 in recordPlaces or placement.upper()=="1A":
                aOne=True
                if placement!='7': #if the user did not input a number, it still needs to be added.
                    recordPlaces.append(7)
            else:
                aOne=False
            if placement=='8' or 8 in recordPlaces or placement.upper()=="2A":
                bOne=True
                if placement!=8:
                    recordPlaces.append(2)
            else:
                bOne=False
            if placement==9 or 9 in recordPlaces or placement.upper()=="3A":
                cOne=True
                if placement!=9:
                    recordPlaces.append(9)
            else:
                cOne=False
            if placement==4 or 4 in recordPlaces or placement.upper()=="1B":
                aTwo=True
                if placement!=4:
                    recordPlaces.append(4)
            else:
                aTwo=False
            if placement==5 or 5 in recordPlaces or placement.upper()=="2B":
                bTwo=True
                if placement!=5:
                    recordPlaces.append(5)
            else:
                bTwo=False
            if placement==6 or 6 in recordPlaces or placement.upper()=="3B":
                cTwo=True
                if placement!=6:
                    recordPlaces.append(6)
            else:
                cTwo=False
            if placement==1 or 1 in recordPlaces or placement.upper()=="1C":
                aThree=True
                if placement!=1:
                    recordPlaces.append(1)
            else:
                aThree=False
            if placement==2 or 2 in recordPlaces or placement.upper()=="2C":
                bThree=True
                if placement!=2:
                    recordPlaces.append(2)
            else:
                bThree=False
            if placement==3 or 3 in recordPlaces or placement.upper()=="3C":
                cThree=True
                if placement!=3:
                    recordPlaces.append(3)
            else:
                cThree=False
            placement=0
            userWin=GameX(aOne,aTwo,aThree,bOne,bTwo,bThree,cOne,cTwo,cThree) #used to run if player is x - gameFinished matches to gameSet
        elif(turn%2==1): #gameX - enemy's turn
            wait=input("Press 'ENTER' to have the enemy play: ") #this isn't tied to anything
            i=1
            while(i==1):
                enemy=random.randint(0,9) #stuck in a loop until gives an unselected square
                if(enemy not in recordPlaces):
                    i+=1 #breaks this loop
                    recordPlaces.append(enemy)
            if placement==7 or 7 in recordPlaces:
                aOne=True
            else:
                aOne=False
            if placement==8 or 8 in recordPlaces:
                bOne=True
            else:
                bOne=False
            if placement==9 or 9 in recordPlaces:
                cOne=True
            else:
                cOne=False
            if placement==4 or 4 in recordPlaces:
                aTwo=True
            else:
                aTwo=False
            if placement==5 or 5 in recordPlaces:
                bTwo=True
            else:
                bTwo=False
            if placement==6 or 6 in recordPlaces:
                cTwo=True
            else:
                cTwo=False
            if placement==1 or 1 in recordPlaces:
                aThree=True
            else:
                aThree=False
            if placement==2 or 2 in recordPlaces:
                bThree=True
            else:
                bThree=False
            if placement==3 or 3 in recordPlaces:
                cThree=True
            else:
                cThree=False
            enemyWin=Game0(aOne,aTwo,aThree,bOne,bTwo,bThree,cOne,cTwo,cThree) #used to run if player is x - gameFinished matches to gameSet
        turn+=1
    print("Game over")
    if enemyWin==True and userWin==False:
        print("You Lost.")
    elif userWin==True and enemyWin==False:
        print("You Won.")
    else:
        print("Something weird happened.")
    #this plays once the win-while loop breaks
    again=input("Play again? ") #this ties to nothing because I assume the user can just close the console if they want to leave
    print("")
    gameplayLoopCount+=1

'''
Started on 9/23/26.
Completed* on 10/21/26.
------
*nothing is ever completed
'''