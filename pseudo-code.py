# Depuis random importer randint 
#Créer un tableau
#Ajouter dans tableau: '-','-','-'
#Ajouter dans tableau: '-','-','-'
#Ajouter dans tableau: '-','-','-'

#Definir une fonction showBoard sans parametre
    #Pour i dans l'intervale 0 et 9
        #Alors
        #Afficher: " | " et joindre une chaîne de caractères e pour e dans tableau

#Definir une fonction choixJoueur avec comme parametre signeJoueur
    #Assigner à isVide qui est égale à 1
    #Assigner à entreeJouers qui permet de contenir les coordonnées avec l'input et afficher: "Joueur 1 Tu souhaites écrire dans quelles case ?: "
    #Assigner à choixJoueurs qui est égale à entreeJoueurs sous forme de liste 
    #Pour i dans l'intervalle  0 et le nombre d'éléments dans choixJoueurs
        #Alors
        #Assigner àux index de choixJoueurs qu'ils sont égale à un entier
    #Tant que isVide est bien égale à 1 
        #Alors
        #Si dans le tableau les indexes du choixJoueurs 0 et 1 sont bien égale à "-"
            #Alors 
            #Assigner àux indexes du choixJours 0 et 1 qu'ils sont égale à signeJoueur
            #Pause
        #sinon
            #Alors
            #Afficher: "Case pleine essaie une autre !"
            #Assigner à isVide egle a 0
            #Executer la fonction choixJoueurs avec parametre signeJoueur
    #Retourner choixJoueurs et signeJoueur

#Definir une fonction testing avec comme parametre signeJoueur
        #Assigner à n qui est égale àux nombres d'indexes dans tableau
        #Verifier les lignes
        #Pour i dans l'intervalle n
            #Assigner à win qui est égale à Vraie
            #Pour j dans l'intervalle n
                #Si i et j est différents de signeJoueur
                    #Alors
                    #Assigner à win qui est égale à Faux
                    #Pause
            #Si win
                #Alors
                #Afficher "gagné ROW"
                #Retourner win

#Definir une fonction checkColums avec comme parametre signeJoueur
    #Assigner à n qui est égale àux nombres d'indexes dans tableau
    # checking columns
    #Pour i dans l'intervalle n
        #Assigner à win qui est égale à Vraie
    #Pour j dans l'intervalle n
        #Si i et j est différents de signeJoueur
            #Alors
            #Assigner à win qui est égale à Faux 
            #Pause
        #Si win
            #Alors
            #Afficher "gagné Col"
    #Retourner win       


    #Assigner à n qui est égale àux nombres d'indexes dans tableau
    # checking diagonals
    #Assigner à win qui est égale à Vraie
    #Pour i dans l'intervalle n
        #Si i et j est différents de signeJoueur
            #Alors
            #Assigner à win qui est égale à Faux
            #Pause
    #Si win
        #Alors
        #Afficher "gagné diag"
        #Retourner win
    #Assigner à win qui est égale à Vraie
    #Pour i dans l'intervalle n
        #Si i et n soustrait de 1 et i est différents de tableau
            #Alors
            #Assigner à win qui est égale à Faux
            #Pause
    #Si win
        #Alors
        #Retourner win
    #Retourner Faux

#Definir une fonction game sans paraletre
    #Assigner à signeJoueur qui est égale à 'X'
    #Assigner à start qui est égale à 1
    #Assigner à choiceGame qui contient l'input et affiche: "Tu souhaites jouer avec un ami, ou avec un bot ?: "
    #Assigner à restart qui est égale à 0
    #Assigner à equal qui est égale à 0

    #Tant que start est bien égale à 1
        #Si choice est bien égale à "ami"
            #Alors
            #Assigner à tourJoueurUn qui est égale à Vrai
            #Si tourJoueurUn est bien égale à Vraie
                #Alors
                #Afficher "Joueur 1"
            #Sinon
                #Afficher "Joueur 2"
        #Tant que tourJoueurUn est bien égale à Vrai
            #Executer la fonction showBoard
            #Si signeJoueur est bien égale à 'O'
                #Alors
                #Assigner à signeJoueur qui est égale à 'X'
            #Sinon
                #Assigner à signeJoueur qui est égale à 'o'
            #Afficher: "C'est au tour de :" et signeJoueur
            #Tant que start est bien égale à 1
                #Executer la fonction signeJoueur
                #Assigner à equal qui est égale à equal ajouter 1
                #Si equal est bien égale à 9
                    #Alors
                    #Afficher "Egalité"
                    #Assigner à start qui est égale à 0
                    #Assigner à tourJoueurUn qui est bien égale à Faux
                    #Assigner à restart qui est égale à 1
                #Si la fonction testing avec parametre signeJoueur ou la fonction checkColumns avec parametre signeJoueur ou la fonction checkDiagonals avec parametre signeJoueur 
                    #Alors
                    #Afficher : "Le joueur " et signeJoueur et " a gagné "
                    #Assigner à start  qui est égale à 0 
                    #Assigner à tourJoueur qui est bien égale à Faux
                    #Assigner à restart qui est égale à 1
                #Si restrat est bien égale à 1 
                    #Aloes
                    #Assigner à choiceRestart qui contient l'input et affiche "Vous voulez rejouer ?: "
                    #Si choiceRestart est bien égale à "oui"
                        #Alors
                        #Executer la fonction Clear
                        #Executer la fonction game
                    #Sinon
                        #Pause
                #Pause
       
#Executer la fonction game