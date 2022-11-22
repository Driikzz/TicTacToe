from random import randint
tableau = []
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])

import os
clear = lambda: os.system('cls')

def showBoard(): 
    for i in range(0,len(tableau)):
        print(" | ".join(str(e) for e in tableau[i]))


def choixJoueur(signeJoueur):
        isVide = 1
        entreeJoueurs = input(("Joueur 1 Tu souhaites écrire dans quelles case ?: "))
        choixJoueurs = (entreeJoueurs.split())
        for i in range(0,len(choixJoueurs)):
                choixJoueurs[i] = int(choixJoueurs[i])
        while isVide == 1:
            if(tableau[choixJoueurs[0]][choixJoueurs[1]]=="-"):
                tableau[choixJoueurs[0]][choixJoueurs[1]] = signeJoueur
                break
            else:
                print("Case pleine essaie une autre !")
                isVide = 0
                choixJoueur(signeJoueur)

        return choixJoueurs, signeJoueur

def testing(signeJoueur):
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

def checkColumns(signeJoueur):
        
        n = len(tableau)
        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if tableau[j][i] != signeJoueur:
                    win = False
                    break
            if win:
                print("gagné Col")
                
                return win

def checkDiagonals(signeJoueur):
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

def game ():
    signeJoueur = 'X'
    start = 1
    choiceGame = input(("Tu souhaites jouer avec un ami, ou avec un bot ?: "))
    restart = 0
    equal = 0
    
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
                signeJoueur ='O'
            print("C'est au tour de :"+ signeJoueur)
            while start == 1:
                    choixJoueur(signeJoueur)
                    equal = equal + 1
                    
                    if equal == 9:
                        print("Egalité")
                        start = 0
                        tourJoueurUn == False
                        restart = 1
                    
                    if testing(signeJoueur) or checkColumns(signeJoueur) or checkDiagonals(signeJoueur):
                        print("Le joueur " + signeJoueur +" a gagné ")
                        start = 0
                        tourJoueurUn == False
                        restart = 1
                    
                    if restart == 1 :
                        choiceRestart = input("Vous voulez rejouer ?: ")
                        if choiceRestart == "oui":
                            clear()
                            game()
                        else:
                            break 
                    break
       
game()






