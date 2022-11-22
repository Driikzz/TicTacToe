from random import randint
import os

class morpion: 
    tableau = []
    tableau.append(['-','-','-'])
    tableau.append(['-','-','-'])
    tableau.append(['-','-','-'])
    signeJoueur = ' '

    
    clear = lambda: os.system('cls')
    
    def showBoard(self): 
        for i in range(0,len(self.tableau)):
            print(" | ".join(str(e) for e in self.tableau[i]))

    def choixJoueur(self):
        entreeJoueurs = input(("Joueur 1 Tu souhaites écrire dans quelles case ?: "))
        return entreeJoueurs

    def choixJoueurDeux(self):
            entreeJoueursDeux = input(("Joueur 2 Tu souhaites écrire dans quelles case ?: "))
            return entreeJoueursDeux

    def joueurSigne(self):
       
        return self.signeJoueur


    def testing(self):
            n = len(self.tableau)

            # checking rows
            for i in range(n):
                win = True
                for j in range(n):
                    if self.tableau[i][j] != self.signeJoueur:
                        win = False
                        break
                if win:
                    print("gagné ROW")
                    return win

    def checkColumns(self):
            n = len(self.tableau)
            # checking columns
            for i in range(n):
                win = True
                for j in range(n):
                    if self.tableau[j][i] != self.signeJoueur:
                        win = False
                        break
                if win:
                    start = 0
                    print("gagné Col ")
                    
                    return win

    def randomStarter(self):
        return randint(0,1)
   
    def checkDiagonals(self):
            n = len(self.tableau)
            # checking diagonals
            win = True
            for i in range(n):
                if self.tableau[i][i] != self.signeJoueur:
                    win = False
                    break
            if win:
                print("gagné diag")
                return win
            
            win = True
            for i in range(n):
                if self.tableau[i][n - 1 - i] != self.tableau:
                    win = False
                    break
            if win:
                return win
            return False
    
    def game (self):
        start = 1
        choiceGame = input(("Tu souhaites jouer avec un ami, ou avec un bot ?: "))
        restart = 0
        equal = 0
        if self.randomStarter() == 1: 
            self.signeJoueur = 'X'
        else: 
            self.signeJoueur = 'O'
        
        while start == 1:                
            if choiceGame == "ami":
                tourJoueurUn = True
                if tourJoueurUn == True:
                    print("Joueur 1")
                else : 
                    print("Joueur 2 ") 
            
            while tourJoueurUn == True: 
                self.showBoard()
                if self.signeJoueur == 'O':
                    self.signeJoueur = 'X'
                if self.signeJoueur == 'X':
                    self.signeJoueur = 'O'
                    
                print("C'est au tour de :"+ self.signeJoueur)
                choixJoueurs = (self.choixJoueur().split())
                for i in range(0,len(choixJoueurs)):
                    choixJoueurs[i] = int(choixJoueurs[i])
                while start == 1:
                    if(self.tableau[choixJoueurs[0]][choixJoueurs[1]]=="-"):
                        self.tableau[choixJoueurs[0]][choixJoueurs[1]] = self.signeJoueur
                        equal = equal + 1
                        print(equal)
                        if equal == 9:
                            print("Egalité")
                            start = 0
                            tourJoueurUn == False
                            restart = 1
                        if self.testing():
                            print("Le joueur " + self.signeJoueur +" a gagné ")
                            start = 0
                            tourJoueurUn == False
                            restart = 1
                        if self.checkColumns(): 
                            print("Le joueur " + self.signeJoueur +" a gagné ")
                            start = 0
                            tourJoueurUn == False
                            restart = 1
                        if self.checkDiagonals(): 
                            print("Le joueur " + self.signeJoueur +" a gagné ")
                            start = 0
                            tourJoueurUn == False
                            restart = 1
                        if restart == 1 :
                            choiceRestart = input("Vous voulez rejouer ?: ")
                            if choiceRestart == "oui":
                                self.clear()
                                self.game()
                            else:
                                break
                        break   
                    else: 
                        print("Case occupé, essaie une autre !")
                        break
morpion = morpion()
morpion.game()
                



