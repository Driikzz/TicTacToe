from random import randint
tableau = []
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])


signeJoueur = 'X'
signeJoueur = 'O'

import os
clear = lambda: os.system('cls')

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
                print("gagné ROW")
                return win

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
                start = 0
                print("gagné Col ")
                
                return win

def checkDiagonals():
        n = len(tableau)
        # checking diagonals
        win = True
        for i in range(n):
            if tableau[i][i] != signeJoueur:
                win = False
                break
        if win:
            print("gagné diag")
            return win
        
        win = True
        for i in range(n):
            if tableau[i][n - 1 - i] != tableau:
                win = False
                break
        if win:
            return win
        return False

        for row in taleau:
            for item in row:
                if item == '-':
                    return False
        return True

def checkEqual():
        for row in tableau:
            for item in row:
                if item == '-':
                    return False
        return True


def game ():
    start = 1
    choiceGame = input(("Tu souhaites jouer avec un ami, ou avec un bot ?: "))
    signeJoueur = 'X'
    restart = 0
    
    while start == 1:            
        
        
        if choiceGame == "ami":
            tourJoueurUn = True
            if tourJoueurUn == True:
                print("Joueur 1")
            else : 
                print("Joueur 2 ") 

        while tourJoueurUn == True: 
            showBoard()
            if signeJoueur == 'O':
                signeJoueur = 'X'
            else:
                signeJoueur = 'O'
            print("C'est au tour de :"+ signeJoueur)
            choixJoueurs = (choixJoueur().split())
            for i in range(0,len(choixJoueurs)):
                choixJoueurs[i] = int(choixJoueurs[i])
            while start == 1:
                if(tableau[choixJoueurs[0]][choixJoueurs[1]]=="-"):
                    tableau[choixJoueurs[0]][choixJoueurs[1]] = signeJoueur
                    if testing():
                        print("ROW")
                        print("Le joueur " + signeJoueur +" a gagné ")
                        start = 0
                        tourJoueurUn == False
                        restart = 1
                    if checkColumns():
                        print("COL")
                        print("Le joueur " + signeJoueur +" a gagné ")
                        start = 0
                        tourJoueurUn == False
                        restart = 1
                    if checkDiagonals(): 
                        print("Le joueur " + signeJoueur +" a gagné ")
                        start = 0
                        tourJoueurUn == False
                        restart = 1
                    if not checkEqual:
                        print("Equal")
                    if restart == 1 :
                        choiceRestart = input("Vous voulez rejouer ?: ")
                        if choiceRestart == "oui":
                            clear()
                            game()
                            

                        else:
                            break
                    break   
                else: 
                    print("Case occupé, essaie une autre !")
                    break
            

game()






