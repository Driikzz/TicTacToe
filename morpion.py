from random import randint
tableau = []
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])
playerSign = 'X'

def showBoard(): 
    for i in range(0,len(tableau)):
        print(" | ".join(str(e) for e in tableau[i]))

def playerSignSwap(): 
    playerSign = 'X'
    if playerSign == 'X':
        playerSign = 'O'
    else:
        playerSign = 'X'
    return playerSign

def caseDisponible():
    choixJoueur = input("Tu choisie qu'elle cordoonée: ")
    choixJoueurSplit = (choixJoueur.split())
    for i in range(0,len(choixJoueurSplit)):
        choixJoueurSplit[i] = int(choixJoueurSplit[i])
    if(tableau[choixJoueurSplit[0]][choixJoueurSplit[1]]=="-"):
        tableau[choixJoueurSplit[0]][choixJoueurSplit[1]] = playerSignSwap()
    else: 
        print("Case occupé, essaie une autre !")

def game():

    start = 1
    

    
    while start == 1:
        showBoard()
        caseDisponible()


game()