
tableau = []

def choixJoueur():
    choixJoueurs = input(("Tu souhaites écrire dans quelles case ?: "))
    return choixJoueurs

def showBoard(): 
    for i in range(3):
        tableau.append([]) 
        for j in range(3):
            tableau[i].append(' ') 
    for i in range(3): 
        print(tableau[i])
    return print(tableau[i])

def game ():
    showBoard()
    choixJoueurs = choixJoueur()
    start = 1
    
    if choixJoueurs == "oui": 
        tableau[0]= ('X')
        showBoard()
    else: 
        print("NON")

game()






