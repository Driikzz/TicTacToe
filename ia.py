
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
            return colonne[1], i
    diagonaleUn = iatest(tableau[0][0],tableau[1][1],tableau[2][2])
    diagonaleDeux = iatest(tableau[0][2],tableau[1][1],tableau[2][0])
    if diagonaleUn[0] == True: 
        return diagonaleUn[1],diagonaleUn[1]
    if diagonaleDeux[0] == True:
        return diagonaleDeux[1], 2-diagonaleDeux[1]
    return[]

def iaPlay(playerSymbole,turn):
    # premier tour
    if turn == 1:
        # si on commence 
            # si on joue milieu 
            if taleau[1][1] == playerSymbole:
                # alors l'ia joue coin 
                tableau = ([2,0]) 
                return tableau
            # si autre
            else:
                # alors l'ia joue milieu
                tableau = ([1,1]) 
                return tableau
           
    # deuxième tour
    if turn == 2:
            # si on a joue milieu
            if tableau[1][1] == playerSymbole:
                # si on joue toute les cases qui peuvent nous faire gagner 
                if possbileWin(tableau,playerSymbole) != []:  # a [x,x]
                    # l'ia bloque la dernière case 
                    tableau =([possbileWin(tableau,playerSymbole)[0],possbileWin(tableau,playerSymbole)[1]])  
                    return tableau
                # si on joue la case qui s'aligne avec le coup de l'ia 
                if possbileWin(tableau,playerSymbole) == []:
                    # l'ia joue le coin case opposé pour créer une ligne avec un coup au milieu manquant
                    if tableau[2][0] == playerSymbole:
                        tableau =([0,0]) 
                        return tableau
                
            # si on a joue coin 
            if tableau[0][0] == playerSymbole or tableau[0][2] == playerSymbole or tableau[2][0] == playerSymbole or tableau[2][2] == playerSymbole :
                # si on joue une case qui aligne deux de nos coups
                if possbileWin(tableau,playerSymbole) != []:  # a [x,x]
                    # l'ia le bloque
                    tableau =([possbileWin(tableau,playerSymbole)[0],possbileWin(tableau,playerSymbole)[1]])
                    return tableau
                # si on joue un coup qui n'aligne pas deux de nos coups
                if possbileWin(tableau,playerSymbole) == []:
                    # l'ia aligne son deuxieme coup avec son premier et un espace vide
                    if tableau[0][0] == playerSymbole and tableau[2][2] == playerSymbole or tableau[0][2] == playerSymbole and tableau[2][0] == playerSymbole :
                        tableau =([1,0]) 
                        return tableau 
                    else:
                        if tableau[0][0] == playerSymbole and tableau[2][1] == playerSymbole:
                            tableau =([1, 2]) 
                            return tableau
                        if tableau[0][0] == playerSymbole and tableau[1][2] == playerSymbole:
                            tableau =([2, 1]) 
                            return tableau
                        if tableau[0][2] == playerSymbole and tableau[2][1] == playerSymbole:
                            tableau =([1, 0]) 
                            return tableau 
                        if tableau[0][2] == playerSymbole and tableau[1][0] == playerSymbole:
                            tableau =([2, 1]) 
                            return tableau
                        if tableau[2][0] == playerSymbole and tableau[0][1] == playerSymbole:
                            tableau =([1, 2]) 
                            return tableau
                        if tableau[2][0] == playerSymbole and tableau[1][2] == playerSymbole:
                            tableau =([0, 1]) 
                            return tableau
                        if tableau[2][2] == playerSymbole and tableau[1][0] == playerSymbole:
                            tableau =([0, 1]) 
                            return tableau
                        if tableau[2][2] == playerSymbole and tableau[0][1] == playerSymbole:
                            tableau =([1, 0]) 
                            return tableau 
    # troisieme tour
    if turn == 3 or turn == 4:
        # si possibilité de gagner == True 
        if possbileWin(tableau,playerSymbole) != []:  # a [x,x]
            # gagner 
            tableau =([possbileWin(tableau,playerSymbole)[0],possbileWin(tableau,playerSymbole)[1]])
            return tableau(tableau, possbileWin(tableau,playerSymbole)[0], possbileWin(tableau,playerSymbole)[1], playerSymbole)
        # si joueur possibilité de gagner == True
        if possbileWin(tableau,playerSymbole) != []:  # a [x,x]
            # bloquer 
            tableau =([possbileWin(tableau,playerSymbole)[0],possbileWin(tableau,playerSymbole)[1]])
            return tableau
        # sinon 
        if possbileWin(tableau,playerSymbole) == [] and  possbileWin(tableau,playerSymbole) == []: 
            # jouer pour aligner / remplir
            for l in range(3):
                for r in range(3):
                    if [l,r] not in tableau :
                        tableau =([l,r])
                        return tableau
    

         