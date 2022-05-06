#Hurdebourcq Paul BUT1 TPC#

import sys
import random



def placement_navire(plateau, tailleNavire) :
    if(random.randint(0, 1) == 0) :
        orientation = 'Horizontale'

    else :
        orientation = 'Verticale'


    if(orientation == 'Horizontale') :
        ligne = random.randint(0, plateau - 1)
        colonne = random.randint(0, plateau - tailleNavire)

    else:
        ligne = random.randint(0, plateau - tailleNavire)
        colonne = random.randint(0, plateau - 1)

    return orientation, (ligne, colonne)
    #Place le navire (cible)



def verif_place(plateau, position, taille_navire, orientation) :
    ligne, colonne = position[0], position[1]
    if orientation == 'H' :
        for j in range(taille_navire) :
            if(plateau[ligne] [colonne + j] ['contenu'] != 'Eau') :
                return False


    else :
        for i in range(taille_navire) :
            if(plateau[ligne + i] [colonne] ['contenu'] != 'Eau') :
                return False


    return True
    #Vérifie si la case contient de l'eau ou non, donc si elle a déjà était touchée ou non



if __name__ == "__main__" :
    tableau = []
    taille = 10 

    for i in range(taille) :
        dico = []

        for j in range(taille) :
            dico.append({'contenu' : 'Eau', 'numero' : 0, 'etat' : 'Neuf'})
        tableau.append(dico)
    #Dans chaque case du tableau, on met le dico
        


    tailleBatiment = 5
    Bateau = 'Porte-avions'
    numeroNavire = 0
    orientation, position = placement_navire(len(tableau), tailleBatiment)
    #Variables 

    #Pour le porte-avions
    while(verif_place(tableau, position, tailleBatiment, orientation) == False) :
        print('Impossible. Nouvelle position')
        orientation, position = placement_navire(len(tableau), tailleBatiment)

    if(orientation == 'H') :
        for j in range(tailleBatiment) :
            tableau[position[0]] [position[1] + j] = {'contenu' : Bateau, 'numero' : numeroNavire, 'etat' : 'Neuf'}

    else :
        for i in range(tailleBatiment) :
            tableau[position[0] + i][position[1]] = {'contenu' : Bateau, 'numero' : numeroNavire, 'etat':'Neuf'}



    tailleBatiment = 4
    Bateau = 'Croiseur'
    numeroNavire = 0
    orientation, position = placement_navire(len(tableau), tailleBatiment)
    #Variables 

    #Pour le croiseur
    while(verif_place(tableau, position, tailleBatiment, orientation) == False) :
        print('Impossible. Nouvelle position')
        orientation, position = placement_navire(len(tableau), tailleBatiment)

    if(orientation == 'H') :
        for j in range(tailleBatiment) :
            tableau[position[0]] [position[1] + j] = {'contenu' : Bateau, 'numero' : numeroNavire, 'etat' : 'Neuf'}

    else :
        for i in range(tailleBatiment) :
            tableau[position[0] + i] [position[1]] = {'contenu' : Bateau, 'numero' : numeroNavire, 'etat' : 'Neuf'}
    
    

    tailleBatiment = 3
    Bateau = 'Destroyer'
    numeroNavire = 0
    orientation, position = placement_navire(len(tableau), tailleBatiment)
    #Variables 

    #Pour le destroyer
    while(verif_place(tableau, position, tailleBatiment, orientation) == False) : 
        print('Impossible. Nouvelle position')
        orientation, position = placement_navire(len(tableau), tailleBatiment)
    if(orientation == 'H') :
        for j in range(tailleBatiment) :
            tableau[position[0]] [position[1] + j] = {'contenu' : Bateau, 'numero' : numeroNavire, 'etat' : 'Neuf'}
    else :
        for i in range(tailleBatiment) :
            tableau[position[0] + i] [position[1]] = {'contenu' : Bateau, 'numero' : numeroNavire, 'etat' : 'Neuf'}



    tailleBatiment = 3
    Bateau = 'Destroyer'
    numeroNavire = 1
    orientation, position = placement_navire(len(tableau), tailleBatiment)
    #Variables 

    #Pour le destroyer
    while(verif_place(tableau, position, tailleBatiment, orientation) == False) :
        print('Impossible. Nouvelle position')
        orientation, position = placement_navire(len(tableau), tailleBatiment)

    if(orientation == 'H') :
        for j in range(tailleBatiment) :
            tableau[position[0]] [position[1] + j] = {'contenu' : Bateau, 'numero' : numeroNavire, 'etat' : 'Neuf'}

    else :
        for i in range(tailleBatiment) :
            tableau[position[0] + i] [position[1]] = {'contenu' : Bateau, 'numero' : numeroNavire, 'etat' : 'Neuf'}
    
    
    
    tailleBatiment = 2
    Bateau = 'Torpilleur'
    numeroNavire = 0
    orientation, position = placement_navire(len(tableau), tailleBatiment)
    #Variables 

    #Pour le torpilleur
    while(verif_place(tableau, position, tailleBatiment, orientation)==False) :
        print('Impossible. Nouvelle position')
        orientation, position = placement_navire(len(tableau), tailleBatiment)

    if(orientation == 'H') :
        for j in range(tailleBatiment) :
            tableau[position[0]] [position[1] + j] = {'contenu' : Bateau, 'numero' : numeroNavire, 'etat' : 'Neuf'}
    
    else :
        for i in range(tailleBatiment) :
            tableau[position[0] + i] [position[1]] = {'contenu' : Bateau, 'numero' : numeroNavire, 'etat' : 'Neuf'}
    print('-' * (len(tableau) + 2))










    for ligne in tableau :
        contours = '|'

        for colonne in ligne :
            if(colonne['etat'] == 'Neuf') :
                contours = contours + ' '

            else :
                if(colonne['contenu'] == 'Eau') :
                    contours = contours + 'X'

                else :
                    contours = contours + '{}'.format(colonne['contenu'] [0].lower())
        contours = contours + '|'
        print(contours)
    print('-' * (len(tableau) + 2))
    touchercouler=False

    while(not touchercouler) :
        #i c'est la ligne
        #j c'est la colonne
        print('où voulez vous tirer ? - 0 pour quitter')
        i = (int)(input('Numéro de ligne entre 1 et {} : '.format(10)))

        if(i == 0) :
            print('Tu ne vas même pas jusqu\'au bout du jeu ? Tant pis. Bye !')
            sys.exit(0)

        #Pour le mode triche
        j = (int)(input('Numéro de colonne entre 1 et {} : '.format(10)))
        if((i < 0) or (j < 0)) :
            print('MODE TRICHE :')
            print('-' * (len(tableau) + 2))

            #Pour gagner
            for ligne in tableau :
                contours = '|'

                for colonne in ligne :
                    if(colonne['contenu'] == 'Eau') :
                        contours = contours + ' '

                    else :
                        contours = contours + '{}'.format(colonne['contenu'] [0])

                contours = contours + '|'
                print(contours)
            print('-' * (len(tableau) + 2))

        else :
            if(tableau[(i - 1)] [(j - 1)] ['etat'] == 'Touche') :
                print('Position déjà touchée')

            else :
                tableau[(i - 1)] [(j - 1)] ['etat'] = 'Touche'

                if(tableau[(i - 1)] [(j - 1)] ['contenu'] == 'Eau') :
                    print('A l\'eau')

                else :
                    verifcouler = True

                    for ligne in tableau:
                        for colonne in ligne:
                            if colonne['contenu'] == tableau[(i - 1)] [(j - 1)] ['contenu'] and colonne['numero'] == tableau[(i - 1)] [(j - 1)] ['numero'] and colonne['etat'] == 'Neuf' :
                                verifcouler = False
                                
                    if(verifcouler) :
                        print(tableau[(i - 1)] [(j - 1)] ['contenu'], tableau[(i - 1)] [(j - 1)] ['numero'], 'coulé')

                    else :
                        print(tableau[(i - 1)] [(j - 1)] ['contenu'], tableau[(i - 1)] [(j - 1)] ['numero'], 'touché')

            print('-' * (len(tableau) + 2))
            for ligne in tableau :
                contours = '|'

                for colonne in ligne :
                    if(colonne['etat'] == 'Neuf') :
                        contours = contours + ' '
                        
                    else :
                        if(colonne['contenu'] == 'Eau') :
                            contours = contours + 'X'

                        else :
                            contours = contours + '{}'.format(colonne['contenu'] [0].lower())

                contours = contours + '|'
                print(contours)
            print('-' * (len(tableau) + 2))

        touchercouler = True
        for ligne in tableau :
            for colonne in ligne :
                if((colonne['contenu'] != 'Eau') and (colonne['etat'] == 'Neuf')) :
                    touchercouler = False

    #J'ai gagné                
    print('Tu as coulé tous les bateaux.')
    print('GG')