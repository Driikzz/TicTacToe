from random import randint
tableau = []
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])



    

def showBoard(): 
    for i in range(0,len(tableau)):
        print(" | ".join(str(e) for e in tableau[i]))

            

def choixJoueur():
        entreeJoueurs = input(("Joueur 1 Tu souhaites écrire dans quelles case ?: "))

        return entreeJoueurs

def choixJoueurDeux():
        entreeJoueursDeux = input(("Joueur 2 Tu souhaites écrire dans quelles case ?: "))

        return entreeJoueursDeux





    

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
                    print("Joueur 1")
                else : 
                    print("Joueur 2 ") 

       

        while tourJoueurUn == True: 
            showBoard()
            choixJoueurs = (choixJoueur().split())
            for i in range(0,len(choixJoueurs)):
                choixJoueurs[i] = int(choixJoueurs[i])
            if(tableau[choixJoueurs[0]][choixJoueurs[1]]=="-"):
                tableau[choixJoueurs[0]][choixJoueurs[1]] = charPlayer
                tourJoueurDeux = True
                break   
            else: 
                print("TESTS")


        while tourJoueurDeux == True: 
            showBoard()
            choixJoueursDeux = (choixJoueurDeux().split())
            for i in range(0,len(choixJoueurs)):
                choixJoueursDeux[i] = int(choixJoueursDeux[i])
            if(tableau[choixJoueursDeux[0]][choixJoueursDeux[1]]=="-"):
                tableau[choixJoueursDeux[0]][choixJoueursDeux[1]] = charPlayerDeux
                tourJoueurUn = True
                break   
            else: 
                print("TESTS")

game()






