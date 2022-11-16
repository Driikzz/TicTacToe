
tableau = []
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])
tableau.append(['-','-','-'])

    

def showBoard(): 
    for i in range(0,len(tableau)):
        print(" | ".join(str(e) for e in tableau[i]))

            
    

def choixJoueur():
    caseDisponible = 9
    test = False
    while caseDisponible > 0: 
        entreeJoueurs = input(("Tu souhaites écrire dans quelles case ?: "))
        for x in range(0,len(tableau)):
            for y in range(0,len(tableau[x])) : 
                if tableau[x][y] == '-':
                    print(caseDisponible)
                    caseDisponible = caseDisponible- 1
                    test = True
                    break  
                else:
                    print("Erreur: case pleine essaie une autre case.")
        
        if test == True:
            break
    return entreeJoueurs

    

def game ():
    start = 1
    while start == 1:
        showBoard()
        choixJoueurs = choixJoueur()

        for x in range(0,len(tableau)):
            for y in range(0,len(tableau[x])): 

                if choixJoueurs == "1": 
                    tableau[0][0]= ('X')
                if choixJoueurs == "2": 
                    tableau[0][1]= ('X')
                if choixJoueurs == "3": 
                    tableau[0][2]= ('X')
                if choixJoueurs == "4": 
                    tableau[1][0]= ('X')   
                if choixJoueurs == "5": 
                    tableau[1][1]= ('X')           
                if choixJoueurs == "6": 
                    tableau[1][2]= ('X')
                if choixJoueurs == "7": 
                    tableau[2][0]= ('X')
                if choixJoueurs == "8": 
                    tableau[2][1]= ('X')  
                if choixJoueurs == "9": 
                    tableau[2][2]= ('X')

        
           
       
            
            

game()






