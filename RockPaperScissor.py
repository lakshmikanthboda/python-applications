import random
g = {1:'Rock',2:'Paper',3:'Scissor'}
user_points = 0
cmo_points = 0
h = """1 : Rock
2 : Paper
3 : Scissor
"""
def choise():
    user_choise = int(input(h))
    global user_points
    global cmo_points
    cmputer_choise = random.randint(1, 3)
    if user_choise == 1:
        if cmputer_choise == 1:
            print ('Tie')
            choise()
        elif cmputer_choise == 2:
            cmo_points += 1
            print ('computer  wins', cmo_points)
        elif cmputer_choise == 3:
            user_points += 1
            print ('user  wins', user_points)
    if user_choise == 2:
        if cmputer_choise == 1:
            user_points += 1
            print ('user  wins', user_points)
        elif cmputer_choise == 2:
            print ('Tie')
            choise()
        elif cmputer_choise == 3:
            cmo_points += 1
            print ('computer  wins', cmo_points)

    if user_choise == 3:
        if cmputer_choise == 1:
            cmo_points += 1
            print ('computer  wins', cmo_points)
        elif cmputer_choise == 2:
            user_points += 1
            print ('user  wins', user_points)
        elif cmputer_choise == 3:
            print ('Tie')
            choise()
    if user_points>=10:
        user_points = 0
        cmo_points = 0
        print ('user wins the Game ')
    elif cmo_points>=10:
        user_points = 0
        cmo_points = 0
        print ('Computer wins The Game')
    else:
        choise()

if user_points<10 or  cmo_points<10:
    choise()



