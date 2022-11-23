def iatest(a,b,c,playerSymbole):
    playerSibole= 'O'
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

    

         