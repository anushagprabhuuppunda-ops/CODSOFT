import random
while True: 

    try:
        round=int(input("Enter how many rounds to play:"))
        us=0
        cs=0
        for i in range(0,round):
            print("ROCK-PAPER-SCISSORS")
            print("1.Rock")
            print("2.Paper")
            print("3.Scissors")
            uii=int(input("Enter a choice(1,2,3):"))
            if uii==1:
                ui="Rock"
            elif uii==2:
                ui="Paper"
            elif uii==3:
                ui="Scissors"
            cii=random.randint(1,3)
            if cii==1:
                ci="Rock"
            elif cii==2:
                ci="Paper"
            elif cii==3:
                ci="Scissors"
            print("Your selection:",ui)
            print("Computer selection:",ci)
            if uii==cii:
                us+=0
                cs+=0
                print("Your score:",us,"Computer score:",cs)
            elif ((uii==1 and cii==3) or (uii==2 and cii==1) or (uii==3 and cii==2)):
                us+=1
                cs+=0
                print("Your score:",us,"Computer score:",cs)
            else:
                cs+=1
                us+=0
                print("Your score:",us,"Computer score:",cs)
        if us>cs:
            print("You win!")
        elif cs>us:
            print("Computer win!")
        elif us==cs:
            print("A Tie!") 
        ch=int(input("Wanna play again yes(1) or no(0):"))  
        if ch==0:
            print("Thank you for playing!")
            break
    except:
        print("Please enter valid")
        