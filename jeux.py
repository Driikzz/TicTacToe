from random import randint
tableau = []
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])
winner = 0
signeJoueur = ' '
tourJoueurUn = False 
tourJoueurDeux = False

def showBoard(): 
    for i in range(0,len(tableau)):
        print(" | ".join(str(e) for e in tableau[i]))


def choixJoueur():
        entreeJoueurs = input(("Joueur 1 Tu souhaites écrire dans quelles case ?: "))
        return entreeJoueurs

def choixJoueurDeux():
        entreeJoueursDeux = input(("Joueur 2 Tu souhaites écrire dans quelles case ?: "))
        return entreeJoueursDeux

def testing():
        n = len(tableau)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if tableau[i][j] != signeJoueur:
                    win = False
                    break
            if win:
                print("gagné")
                winner = 1
                tourJoueurUn = False 
                tourJoueurDeux = False
                return tourJoueurUn and tourJoueurDeux

def checkColumns():
        n = len(tableau)
        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if tableau[j][i] != signeJoueur:
                    win = False
                    break
            if win:
                print("gagné")
                winner = 1
                tourJoueurUn = False 
                tourJoueurDeux = False
                return tourJoueurUn and tourJoueurDeux

def checkDiagonals():
        n = len(tableau)
        # checking diagonals
        win = True
        for i in range(n):
            if tableau[i][i] != signeJoueur:
                win = False
                break
        if win:
            winner = 1
            print("gagné")
            return winner


def game ():
    start = 1
    choiceGame = input(("Tu souhaites jouer avec un ami, ou avec un bot ?: "))
    signeJoueur = 'X' if randint(1,2) == 1 else 'O'
    
    
    while start == 1:            
        if choiceGame == "ami":
            tourJoueurUn = True
            if tourJoueurUn == True:
                print("Joueur 1")
            else : 
                print("Joueur 2 ") 


        while tourJoueurUn == True: 
            showBoard()
            print("C'est au tour de :"+ signeJoueur)
            choixJoueurs = (choixJoueur().split())
            for i in range(0,len(choixJoueurs)):
                choixJoueurs[i] = int(choixJoueurs[i])
            if(tableau[choixJoueurs[0]][choixJoueurs[1]]=="-"):
                tableau[choixJoueurs[0]][choixJoueurs[1]] = signeJoueur
                tourJoueurDeux = True
                testing()
                checkColumns()
                checkDiagonals()
                break   
            else: 
                print("Case occupé, essaie une autre !")
            

        while tourJoueurDeux == True:
            if signeJoueur == 'X':
                signeJoueur = 'O'
            else:
                signeJoueur = 'X'     
            showBoard()
            print("C'est au tour de :"+ signeJoueur) 
            choixJoueursDeux = (choixJoueurDeux().split())
            for i in range(0,len(choixJoueurs)):
                choixJoueursDeux[i] = int(choixJoueursDeux[i])
            if(tableau[choixJoueursDeux[0]][choixJoueursDeux[1]]=="-"):
                tableau[choixJoueursDeux[0]][choixJoueursDeux[1]] = signeJoueur
                tourJoueurUn = True
                testing()
                checkColumns()
                checkDiagonals()
                if winner == 1 :
                    print(signeJoueur + "Bien joué tu as gagné !")
                break   
            else: 
                print("Case occupé, essaie une autre !")

game()






