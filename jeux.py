from random import randint
tableau = []
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])

import os
clear = lambda: os.system('cls')

def showtableau(): 
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


def iaPlay(signeJoueur,turn):


    for x in range(len(tableau)):
        for y in range(len(tableau[x])):
            if tableau[x][y] != 'O':
                if turn == 1:
                    # si on commence
                        # si on joue milieu
                        if tableau[0][0] == 'O':
                            # alors l'ia j oue coin
                            tableau[1][1] = signeJoueur
                        else:
                            tableau[2][1] = signeJoueur
                            return tableau,signeJoueur
                if turn == 3 or turn == 5 or turn == 7:
                #row
                    if tableau[0][0] and tableau[0][1] == 'O' and tableau[0][2] == '-':
                        tableau[0][2] = signeJoueur
                        # return tableau, signeJoueur 
                    elif tableau[0][1] and tableau[0][2] == 'O' and tableau[0][0] == '-':
                        tableau[0][0] = signeJoueur
                        print("TEST 1")
                        # return tableau, signeJoueur            
                    elif tableau[0][0] and tableau[0][2] == 'O' and tableau[0][1] == '-':
                        tableau[0][1] = signeJoueur
                        # return tableau, signeJoueur
                    elif tableau[1][0] and tableau[1][1] == 'O' and tableau[1][2] == '-':
                        tableau[1][2] = signeJoueur
                        # return tableau, signeJoueur           
                    elif tableau[1][1] and tableau[1][2] == 'O' and tableau[1][0] == '-':
                        tableau[1][0] = signeJoueur
                        # return tableau, signeJoueur
                    elif tableau[1][0] and tableau[1][2] == 'O' and tableau[1][1] == '-':
                        tableau[1][1] = signeJoueur
                        # return tableau, signeJoueur
                    elif tableau[2][0] and tableau[2][1] == 'O' and tableau[2][2] == '-':
                        tableau[2][2] = signeJoueur
                        # return tableau, signeJoueur
                    elif tableau[2][1] and tableau[2][2] == 'O' and tableau[2][0] == '-' :
                        tableau[2][0] = signeJoueur
                        # return tableau, signeJoueur
                    elif tableau[2][0] and tableau[2][2] == 'O' and tableau[2][1] == '-':
                        tableau[2][1] = signeJoueur
                        # return tableau, signeJoueur
                # col
                    elif tableau[0][0] and tableau[1][0] == 'O' and tableau[2][0] == '-':
                        tableau[2][0] = signeJoueur
                        # return tableau, signeJoueur
                    elif tableau[2][0] and tableau[1][0] == 'O' and tableau[0][0] == '-':
                        tableau[0][0] = signeJoueur
                        print("TEST 2")
                        return tableau, signeJoueur     
                    elif tableau[0][0] and tableau[2][0] == 'O'and tableau[1][0] == '-':
                        tableau[1][0] = signeJoueur
                        # return tableau, signeJoueur           
                    elif tableau[0][1] and tableau[1][1] == 'O'and tableau[2][1] == '-':
                        tableau[2][1] = signeJoueur
                        # return tableau, signeJoueur            
                    elif tableau[2][1] and tableau[1][1] == 'O'and tableau[0][1] == '-':
                        tableau[0][1] = signeJoueur
                        # return tableau, signeJoueur                
                    elif tableau[0][1] and tableau[2][1] == 'O'and tableau[1][1] == '-':
                        tableau[1][1] = signeJoueur
                        # return tableau, signeJoueur            
                    elif tableau[0][2] and tableau[1][2] == 'O' and tableau[2][2] == '-':
                        tableau[2][2] = signeJoueur
                        # return tableau, signeJoueur            
                    elif tableau[2][2] and tableau[1][2] == 'O' and tableau[0][2] == '-':
                        tableau[0][2] = signeJoueur
                        # return tableau, signeJoueur              
                    elif tableau[0][2] and tableau[2][2] == 'O'and tableau[1][2] == '-':
                        tableau[1][2] = signeJoueur
                        # return tableau, signeJoueur              
                # diag
                    elif tableau[0][0] and tableau[1][1] == 'O'and tableau[2][2] == '-':
                        tableau[2][2] = signeJoueur
                        # return tableau, signeJoueur
                    elif tableau[2][2] and tableau[1][1] == 'O'and tableau[0][0] == '-':
                        tableau[0][0] = signeJoueur
                        print("TEST 3")
                        # return tableau, signeJoueur
                    return tableau, signeJoueur
            else:
                print("Case non disponible")
        

   
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
        

def game ():
    signeJoueur = 'X'
    start = 1
    choiceGame = input(("Tu souhaites jouer avec un ami, ou avec un bot ?: "))
    restart = 0
    equal = 0
    turn = 0
    iaPlayer= False
    
    
    while start == 1:                    
        if choiceGame == "ami":
            tourJoueurUn = True
            player = True
            if tourJoueurUn == True:
                print("Party contre un ami :")
            else : 
                print("Party contre un bot") 



        while tourJoueurUn == True: 
            showtableau()
            if signeJoueur == 'O':
                signeJoueur = 'X'
                iaPlayer = True
                player = False
            else: 
                signeJoueur ='O'
                player = True
                iaPlayer =False
            print("C'est au tour de :"+ signeJoueur)
            
            while player == True:
                    choixJoueur(signeJoueur)
                    print(turn)
                    equal = equal + 1
                    turn = turn + 1
                    
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
                    break
            
            while iaPlayer == True:
                    iaPlay(signeJoueur,turn)
                    print(turn)
                   
                    equal = equal + 1
                    turn = turn + 1
                    
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
                    break

            if restart == 1 :
                choiceRestart = input("Vous voulez rejouer ?: ")
                if choiceRestart == "oui":
                    clear()
                    game()
                else:
                    break 
       
game()