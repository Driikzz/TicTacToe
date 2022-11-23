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


def iatest(a,b,c,playerSymbole):
    playerSymbole= 'O'
    if a == b == playerSymbole and c == '-': 
        return True
    elif c == a == playerSymbole and b == '-': 
        return True
    elif b == c == playerSymbole and a == '-':
        return True
    else: 
        return False

def possbileWin(playerSymbole): 
    for i in range(3):
        ligne = iatest(tableau[i][0],tableau[i][1],tableau[i][2],playerSymbole)
        if ligne[0] == True: 
            return i, ligne[1]
        colonne = iatest(tableau[0][i],tableau[1][i],tableau[2][i],playerSymbole)
        if colonne[0] == True:
            return colonne[1],i


def iaPlay(signeJoueur,turn,playerSymbole):
    # premier tour
    if turn == 1:
        # si on commence 
            # si on joue milieu 
            if tableau[0][0] == 'O':
                # alors l'ia joue coin 
                tableau[1][1] = signeJoueur
                return tableau,signeJoueur
            # si autre
            else:
                tableau[randint(0,2)][randint(0,2)] = signeJoueur
                return tableau,signeJoueur
    if turn == 3: 

        if tableau[1][1] == 'O':
            tableau[2][0] = signeJoueur
            return tableau,signeJoueur
        elif tableau[0][1] == 'O':
            tableau[0][2] = signeJoueur
            return tableau, signeJoueur
    # row
        elif possbileWin(playerSymbole) == 'O':

        elif tableau[0][0] and tableau[0][1] == 'O':
            tableau[0][2] = signeJoueur
            return tableau, signeJoueur
        elif tableau[0][1] and tableau[0][2] == 'O':
            tableau[0][2] = signeJoueur
            return tableau, signeJoueur
        elif tableau[0][1] and tableau[0][2] == 'O':
            tableau[0][2] = signeJoueur
            return tableau, signeJoueur
    # col
        elif tableau[0][0] and tableau[1][0] == 'O':
            tableau[2][0] = signeJoueur
            return tableau, signeJoueur
        elif tableau[0][1] and tableau[1][1] == 'O':
            tableau[2][1] = signeJoueur
            return tableau, signeJoueur
        elif tableau[0][2] and tableau[1][2] == 'O':
            tableau[2][2] = signeJoueur
            return tableau, signeJoueur

    
        
        

    if turn == 5 or turn == 7:   
        if tableau[2][0] == '-':
            tableau[2][0] = signeJoueur
            return tableau,signeJoueur
        elif tableau[0][2] == '-':
            tableau[0][2] = signeJoueur
            return tableau,signeJoueur
    # deuxième tour
    # if turn == 3:
    #         # si on a joue milieu
    #         if tableau[1][1] == signeJoueur:
    #             # si on joue toute les cases qui peuvent nous faire gagner 
    #             if canWin(signeJoueur) != []:  # a [x,x]
    #                 # l'ia bloque la dernière case 
    #                 tableau([0][1]).append([canWin(tableau,signeJoueur)[0],canWin(tableau,signeJoueur)[1]])  
    #                 return tableau, canWin(tableau,signeJoueur)[0], canWin(tableau,signeJoueur)[1], iacoup
    #             # si on joue la case qui s'aligne avec le coup de l'ia 
    #             if canWin(signeJoueur) == []:
    #                 # l'ia joue le coin case opposé pour créer une ligne avec un coup au milieu manquant
    #                 if tableau[2][0] == iacoup:
    #                     tableau[0][0].append([0][0]) 
    #                     return tableau, 0, 0, iacoup
                
    #         # si on a joue coin 
    #         if tableau[0][0] == signeJoueur or tableau[0][2] == signeJoueur or tableau[2][0] == signeJoueur or tableau[2][2] == signeJoueur :
    #             # si on joue une case qui aligne deux de nos coups
    #             if canWin(signeJoueur) != []:  # a [x,x]
    #                 # l'ia le bloque
    #                 tableau.append([canWin(tableau,signeJoueur)[0],canWin(tableau,signeJoueur)[1]])
    #                 return tableau, canWin(tableau,signeJoueur)[0], canWin(tableau,signeJoueur)[1], iacoup
    #             # si on joue un coup qui n'aligne pas deux de nos coups
    #             if canWin(tableau) == []:
    #                 # l'ia aligne son deuxieme coup avec son premier et un espace vide
    #                 if tableau[0][0] == signeJoueur and tableau[2][2] == signeJoueur or tableau[0][2] == signeJoueur and tableau[2][0] == signeJoueur :
    #                     tableau.append([1,0]) 
    #                     return tableau, 1, 0, iacoup
    #                 else:
    #                     if tableau[0][0] == signeJoueur and tableau[2][1] == signeJoueur:
    #                         tableau.append([1, 2]) 
    #                         return tableau, 1, 2, iacoup
    #                     if tableau[0][0] == signeJoueur and tableau[1][2] == signeJoueur:
    #                         tableau.append([2, 1]) 
    #                         return tableau, 2, 1, iacoup
    #                     if tableau[0][2] == signeJoueur and tableau[2][1] == signeJoueur:
    #                         tableau.append([1, 0]) 
    #                         return tableau, 1, 0, iacoup
    #                     if tableau[0][2] == signeJoueur and tableau[1][0] == signeJoueur:
    #                         tableau.append([2, 1]) 
    #                         return tableau, 2, 1, iacoup
    #                     if tableau[2][0] == signeJoueur and tableau[0][1] == signeJoueur:
    #                         tableau.append([1, 2]) 
    #                         return tableau, 1, 2, iacoup
    #                     if tableau[2][0] == signeJoueur and tableau[1][2] == signeJoueur:
    #                         tableau.append([0, 1]) 
    #                         return tableau, 0, 1, iacoup
    #                     if tableau[2][2] == signeJoueur and tableau[1][0] == signeJoueur:
    #                         tableau.append([0, 1]) 
    #                         return tableau, 0, 1, iacoup
    #                     if tableau[2][2] == signeJoueur and tableau[0][1] == signeJoueur:
    #                         tableau.append([1, 0]) 
    #                         return tableau, 1, 0, iacoup
    # # troisieme tour
    # if turn == 5:
    #     # si possibilité de gagner == True 
    #     if canWin(tableau) != []:  # a [x,x]
    #         # gagner 
    #         tableau.append([canWin(tableau,signeJoueur)[0],canWin(tableau,signeJoueur)[1]])
    #         return tableau, canWin(tableau,iacoup)[0], canWin(tableau,iacoup)[1], iacoup
    #     # si joueur possibilité de gagner == True
    #     if canWin(tableau) != []:  # a [x,x]
    #         # bloquer 
    #         tableau.append([canWin(tableau,signeJoueur)[0],canWin(tableau,signeJoueur)[1]])
    #         return tableau, canWin(tableau,signeJoueur)[0], canWin(tableau,signeJoueur)[1], iacoup
    #     # sinon 
    #     if canWin(tableau) == [] and  canWin(tableau) == []: 
    #         # jouer pour aligner / remplir
    #         for l in range(3):
    #             for r in range(3):
    #                 if [l,r] not in tableau :
    #                     tableau.append([l,r])
    #                     return tableau, l, r, iacoup


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
                    print(turn)
                    iaPlay(signeJoueur,turn)
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






