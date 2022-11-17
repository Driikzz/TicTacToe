from random import randint
tableau = []
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])



    

def showBoard(): 
    for i in range(0,len(tableau)):
        print(" | ".join(str(e) for e in tableau[i]))

            

def choixJoueur():
    caseDisponible = 9
    test = False
    while caseDisponible > 0: 
        entreeJoueurs = input(("Tu souhaites écrire dans quelles case ?: "))
        for x in range(0,len(tableau)):
            for y in range(0,len(tableau[x])) : 
                if tableau[x][y] == '-':
                    print(caseDisponible)
                    caseDisponible = caseDisponible- 1
                    test = True
                    break  
                else:
                    print("Erreur: case pleine essaie une autre case.")
            if test == True:
                break        
        if test == True:
            break
    return entreeJoueurs

def choixJoueurDeux():
    caseDisponible = 9
    test = False
    while caseDisponible > 0: 
        entreeJoueurs2 = input(("Tu souhaites écrire dans quelles case ?: "))
        for x in range(0,len(tableau)):
            for y in range(0,len(tableau[x])) : 
                if tableau[x][y] == '-':
                    caseDisponible = caseDisponible- 1
                    test = True
                    break  
                else:
                    print("Erreur :")
            if test == True:
                break        
        if test == True:
            break
    return entreeJoueurs2


    

def game ():
    joueurDeux = 0 
    start = 1
    charPlayer = input(("Tu souhaites jouer O ou X: "))
    choiceGame = input(("Tu souhaites jouer avec un ami, ou avec un bot ?: "))
    tourJoueurUn = False 
    tourJoueurDeux = False
    while start == 1:
        
        if charPlayer == 'X':
            joueurDeux = 1
            if joueurDeux == 1 :
                charPlayerDeux = 'O'
            else:
                charPlayer = 'X'
            
            
            if choiceGame == "ami":
                tourJoueurUn = True
                if tourJoueurUn == True:
                    # tourJoueurUn = True
                    print("Joueur 1 commence")
                else : 
                    tourJoueurDeux = tourJoueurDeux + 1
                    print("Joueur 2 commence") 

        if tourJoueurUn == True :
            showBoard()
            choixJoueurs = choixJoueur()
            print("Tour au joueur 1")
            if choixJoueurs == "1": 
                tableau[0][0]= (charPlayer)
                showBoard()
            if choixJoueurs == "2": 
                    tableau[0][1]= (charPlayer)
                    showBoard()
            if choixJoueurs == "3": 
                    tableau[0][2]= (charPlayer)
                    showBoard()
            if choixJoueurs == "4": 
                    tableau[1][0]= (charPlayer)
                    showBoard()
            if choixJoueurs == "5": 
                    tableau[1][1]= (charPlayer) 
                    showBoard() 
            if choixJoueurs == "6": 
                    tableau[1][2]= (charPlayer)
                    showBoard()
            if choixJoueurs == "7": 
                    tableau[2][0]= (charPlayer)
                    showBoard()
            if choixJoueurs == "8": 
                    tableau[2][1]= (charPlayer)
                    showBoard()
            if choixJoueurs == "9": 
                    tableau[2][2]= (charPlayer)
                    showBoard()
            

        if tourJoueurDeux == 1 :
            choixJoueur2 = choixJoueurDeux()
            print("Tour au joueur 2")
            if choixJoueur2 == "1": 
                tableau[0][0]= (charPlayerDeux)
                showBoard()
            if choixJoueur2 == "2": 
                    tableau[0][1]= (charPlayerDeux)
                    showBoard()
            if choixJoueur2 == "3": 
                    tableau[0][2]= (charPlayerDeux)
                    showBoard()
            if choixJoueur2 == "4": 
                    tableau[1][0]= (charPlayerDeux)
                    showBoard()   
            if choixJoueur2 == "5": 
                    tableau[1][1]= (charPlayerDeux)
                    showBoard()          
            if choixJoueur2 == "6": 
                    tableau[1][2]= (charPlayerDeux)
                    showBoard()
            if choixJoueur2 == "7": 
                    tableau[2][0]= (charPlayerDeux)
                    showBoard()
            if choixJoueur2 == "8": 
                    tableau[2][1]= (charPlayerDeux)
                    showBoard()
            if choixJoueur2 == "9": 
                    tableau[2][2]= (charPlayerDeux)
                    showBoard()
            

              


game()






