from random import randint
tableau = []
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])
winner = 0
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
                if tableau[i][j] != joueur:
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
                if tableau[j][i] != joueur:
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
            if tableau[i][i] != joueur:
                win = False
                break
        if win:
            winner = 1
            print("gagné")
            return winner

def tourJoueur():
    joueur = 'X' if randint(0, 1) == 1 else 'O'
    print(joueur)
    return 'X' if joueur == 'O' else 'O'


def caseDisponible(): 
    choixJoueurs = (choixJoueur().split())
    for i in range(0,len(choixJoueurs)):
        choixJoueurs[i] = int(choixJoueurs[i])
    if(tableau[choixJoueurs[0]][choixJoueurs[1]]=="-"):
        tableau[choixJoueurs[0]][choixJoueurs[1]] = tourJoueur()
    else: 
        print("Case occupé, essaie une autre !")
    

def game ():
    start = 1
    choiceGame = input(("Tu souhaites jouer avec un ami, ou avec un bot ?: "))
    
    while start == 1:        
        
        if choiceGame == "ami":
            tourJoueurUn = True
            if tourJoueurUn == True:
                print("Joueur 1")
            else : 
                print("Joueur 2 ")

        if tourJoueur() == 'X':
            showBoard()
            print("C'est au tour du joueur X")
            caseDisponible()
            checkColumns()
            checkDiagonals()
            testing()

        elif tourJoueur() == 'O':
                    showBoard()
                    print("C'est au tour du joueur O")
                    caseDisponible()
                    checkColumns()
                    checkDiagonals()
                    testing()

        # match tourJoueur():
        #     case 'X':
        #             showBoard()
        #             print("C'est au tour du joueur X")
        #             caseDisponible()
        #             checkColumns()
        #             checkDiagonals()
        #             testing()
                    
        #     case 'O':
        #         showBoard()
        #         print("C'est au tour du Joueur O")
        #         caseDisponible()
        #         checkColumns()
        #         checkDiagonals()
        #         testing()

game()






