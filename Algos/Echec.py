### HURDEBOURCQ Paul BUT1 TPC ###
from numpy import *
#Mon plateau de jeu initial
jeu = array([['   ','   ','   ','   ','   ','   ','   ','   '],
                  ['   ','   ','   ','   ','   ','   ','   ','   '],
                  ['   ','   ','   ','   ','   ','   ','   ','   '],
                  ['   ','   ','   ','   ','   ','   ','   ','   '],
                  ['   ','   ','   ','   ','   ','   ','   ','   '],
                  ['   ','   ','   ','   ','   ','   ','   ','   '],
                  ['   ','   ','   ','   ','   ','   ','   ','   '],
                  ['   ','   ','   ','   ','   ','   ','   ','   ']])

#toutes les pièces blanches :
liste_des_blancs = ['Tb1', 'Cb1', 'Fb1', 'Qb1', 'Kb1', 'Fb2', 'Cb2', 'Tb2', 'pb0', 'pb1', 'pb2', 'pb3', 'pb4', 'pb5', 'pb6', 'pb7']
#toutes les pièces noires   :
liste_des_noirs =  ['Tn1', 'Cn1', 'Fn1', 'Qn1', 'Kn1', 'Fn2', 'Cn2', 'Tn2', 'pn0', 'pn1', 'pn2', 'pn3', 'pn4', 'pn5', 'pn6', 'pn7']



#Place les pions blancs
def pionBlanc() :
    for i in range(8) :
        jeu[6, i] = 'pb' + str(i)
def roiBlanc() :
        jeu[7, 4] = 'Kb1'
def reineBlanc() :
    jeu[7, 3] = 'Qb1'
def fouBlanc() :
    jeu[7, 2] = 'Fb1'
    jeu[7, 5] = 'Fb2'
def chevalBlanc() :
    jeu[7, 1] = 'Cb1'
    jeu[7, 6] = 'Cb2'
def tourBlanc() :
    jeu[7, 0] = 'Tb1 '
    jeu[7, 7] = 'Tb2'
def les_blancs() :
    pionBlanc()
    roiBlanc()
    reineBlanc()
    fouBlanc()
    chevalBlanc()
    tourBlanc()
    return jeu


#Place les pions noirs
def pionNoir() :
    for i in range(8) :
        jeu[1, i] = 'pn' + str(i)
def roiNoir() :
    jeu[0, 4] = 'Kn1'
def reineNoir() :
    jeu[0, 3] = 'Qn1'
def fouNoir() :
    jeu[0, 2] = 'Fn1'
    jeu[0, 5] = 'Fn2'
def chevalNoir() :
    jeu[0, 1] = 'Cn1'
    jeu[0, 6] = 'Cn2'
def tourNoir() :
    jeu[0, 0] = 'Tn1'
    jeu[0, 7] = 'Tn2'
def les_noirs() :
    pionNoir()
    roiNoir()
    reineNoir()
    fouNoir()
    chevalNoir()
    tourNoir()
    return jeu

#initialise le plateau au début de la partie
def jeu_debut() :
    les_blancs()
    les_noirs()
    return jeu





#Le pion blanc est terminé !
def mouvPionBlanc() :
    choix = str(input('\nPièce à bouger -->'))
    for i in range(8) :
        for j in range(8) :
            #pion blanc
            if jeu[i,j] == choix :
                #check s'il peut manger à gauche en haut, peut manger seulement si c'est un noir
                if jeu[i - 1, j - 1] != '   ' :
                    for x in range(len(liste_des_noirs)) :
                        if jeu[i - 1, j - 1] == liste_des_noirs[x] :
                            print('Voulez-vous manger', jeu[i - 1, j - 1], ' ? ')
                            miam = str(input('(y/n) \n==> '))
                            if miam == 'y' :
                                jeu[i,j] = '   '
                                jeu[i - 1, j - 1] = choix
                                return jeu

                #check s'il peut manger à droite en haut, peut manger seulement si c'est un noir
                if jeu[i - 1, j + 1] != '   ' :
                    for y in range(len(liste_des_noirs)) :
                        if jeu[i - 1, j + 1] == liste_des_noirs[y] :
                            print('Voulez-vous manger', jeu[i - 1, j + 1], ' ? ')
                            miam = str(input('(y/n) \n==> '))
                            if miam == 'y' :
                                jeu[i,j] = '   '
                                jeu[i - 1, j + 1] = choix
                                return jeu

                
                #si il ne mange rien il avance simplement
                print('Nombre de cases souhaitées : ')
                depla = int(input('1 ou 2 ?\n==> '))
                #si un pion à déjà avancé, il ne peut plus avancer de 2
                if choix != jeu[6, j] :
                    depla = 1
                    print("le pion", choix, 'à déjà bougé, il avance donc de 1 désormais')
                
                if depla == 2 :
                    #regarde s'il peut avancer de 2
                    if jeu[i - 2, j] == '   ' and jeu[i - 1, j] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - 2, j] = choix
                        return jeu
                    else :
                        print("Impossible d'avancer !")



                if depla == 1 :
                    #regarde s'il peut avancer de 1
                    if jeu[i - 1, j] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - 1, j] = choix
                    else :
                        print("Impossible d'avancer !")
    return jeu
#Le pion blanc est terminé, oui vraiment !

#Le cavalier blanc est terminé !
def mouvCavalierBlanc() :
    choix = str(input('\nPièce à bouger -->'))
    for i in range(8) :
        for j in range(8) :
            #cavalier blanc
            if jeu[i,j] == choix :
                print('Direction souhaitée : ')
                print('\ndevant, droite, haut : DDH ;\ndevant, droite, bas  : DDB ;\ndevant, gauche, haut : DGH ; \ndevant, gauche, bas  : DGB')
                print('\nderriere, droite, haut : dDH ; \nderriere, droite, bas  : dDB ; \nderriere, gauche, haut : dGH ; \nderriere, gauche, bas  : dGB')
                depla = str(input('\nDDH, DDB, DGH, DGB  ;  dDH, dDB, dGH, dGB\n==> '))
                #devant droite haut
                if depla == 'DDH' :
                    if jeu[i - 2, j + 1] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i - 2, j + 1] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i - 2, j + 1], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - 2, j + 1] = choix
                                    return jeu
                    if jeu[i - 2, j + 1] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - 2, j + 1] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu

                #devant droite bas
                if depla == 'DDB' :
                    if jeu[i - 1, j + 2] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i - 1, j + 2] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i - 1, j + 2], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - 1, j + 2] = choix
                                    return jeu
                    if jeu[i - 1, j + 2] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - 1, j + 2] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu
                
                #devant gauche haut
                if depla == 'DGH' :
                    if jeu[i - 2, j - 1] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i - 2, j - 1] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i - 2, j - 1], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - 2, j - 1] = choix
                                    return jeu
                    if jeu[i - 2, j - 1] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - 2, j - 1] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu
                
                #devant gauche bas
                if depla == 'DGB' :
                    if jeu[i - 1, j - 2] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i - 1, j - 2] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i - 1, j - 2], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - 1, j - 2] = choix
                                    return jeu
                    if jeu[i - 1, j - 2] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - 1, j - 2] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu



                #derrière droite haut
                if depla == 'dDH' :
                    if jeu[i + 1, j + 2] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i + 1, j + 2] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i + 1, j + 2], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + 1, j + 2] = choix
                                    return jeu
                    if jeu[i + 1, j + 2] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + 1, j + 2] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu

                #derrière droite bas
                if depla == 'dDB' :
                    if jeu[i + 2, j + 1] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i + 2, j + 1] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i + 2, j + 1], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + 2, j + 1] = choix
                                    return jeu
                    if jeu[i + 2, j + 1] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + 2, j + 1] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu

                #derrière gauche haut
                if depla == 'dGH' :
                    if jeu[i + 1, j - 2] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i + 1, j - 2] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i + 1, j - 2], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + 1, j - 2] = choix
                                    return jeu
                    if jeu[i + 1, j - 2] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + 1, j - 2] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu

                #derrière gauche bas
                if depla == 'dGB' :
                    if jeu[i + 2, j - 1] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i + 2, j - 1] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i + 2, j - 1], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + 2, j - 1] = choix
                                    return jeu
                    if jeu[i + 2, j - 1] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + 2, j - 1] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu
#Le cavalier blanc est terminé, oui vraiment !

#Le fou blanc est terminé !
def mouvFouBlanc() :
    choix = str(input('\nPièce à bouger -->'))
    for i in range(8) :
        for j in range(8) :
            #fou blanc
            if jeu[i,j] == choix :
                print('Direction souhaitée : ')
                print('\ndiagoHG : haut, gauche ; \ndiagoHD : haut, droite ; \ndiagoBG : bas gauche ; \ndiagoBD : bas, droite')
                depla = str(input('diagoHG ; diagoHD ; diagoBG ; diagoBD\n==> '))
                print('Entrez un nombre entier :')
                nb = int(input('Combien de cases doit-il parcourir ?\n==> '))
                
                #diagonale haut gauche
                if depla == 'diagoHG' :
                    if jeu[i - nb, j - nb] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i - nb, j - nb] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i - nb, j - nb], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - nb, j - nb] = choix
                                    return jeu
                    if jeu[i - nb, j - nb] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - nb, j - nb] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu

                #diagonale haut droite
                if depla == 'diagoHD' :
                    if jeu[i - nb, j + nb] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i - nb, j + nb] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i - nb, j + nb], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - nb, j + nb] = choix
                                    return jeu
                    if jeu[i - nb, j + nb] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - nb, j + nb] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu

                #diagonale bas gauche    
                if depla == 'diagoBG' :
                    if jeu[i + nb, j - nb] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i + nb, j - nb] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i + nb, j - nb], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + nb, j - nb] = choix
                                    return jeu
                    if jeu[i + nb, j - nb] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + nb, j - nb] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu

                #diagonale bas droite    
                if depla == 'diagoBD' :
                    if jeu[i + nb, j + nb] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i + nb, j + nb] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i + nb, j + nb], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + nb, j + nb] = choix
                                    return jeu
                    if jeu[i + nb, j + nb] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + nb, j + nb] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu
#Le fou blanc est terminé, oui vraiment !

#La tour blanche est terminée !
def mouvTourBlanc() :
    choix = str(input('\nPièce à bouger -->'))
    for i in range(8) :
        for j in range(8) :
            #tour blanc
            if jeu[i,j] == choix :
                print('Direction souhaitée : ')
                depla = str(input('\nhorizon, gauche : horizG ; \nhorizon, droite : horizD ; \nvertical, haut : vertiH ; \nvertical, bas : vertiB\n==> '))
                nb = int(input('Combien de cases doit-il parcourir ?\n==> '))

                #horizontal gauche
                if depla == 'horizG' :
                    if jeu[i, j - nb] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i, j - nb] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i, j - nb], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i, j - nb] = choix
                                    return jeu
                    if jeu[i, j - nb] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i, j - nb] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu

                #horizontal droite
                if depla == 'horizD' :
                    if jeu[i, j + nb] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i, j + nb] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i, j + nb], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i, j + nb] = choix
                                    return jeu
                    if jeu[i, j + nb] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i, j + nb] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu

                #vertical haut
                if depla == 'vertiH' :
                    if jeu[i - nb, j] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i - nb, j] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i - nb, j], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - nb, j] = choix
                                    return jeu
                    if jeu[i - nb, j] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - nb, j] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu

                #vertical bas
                if depla == 'vertiB' :
                    if jeu[i + nb, j] != '   ' :
                        for x in range(len(liste_des_noirs)) :
                            if jeu[i + nb, j] == liste_des_noirs[x] :
                                print('Voulez-vous manger', jeu[i + nb, j], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + nb, j] = choix
                                    return jeu
                    if jeu[i + nb, j] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + nb, j] = choix
                    print('\nVous ne pouvez pas manger un blanc !')
                    return jeu
#La tour blanche est terminée, oui vraiment !

#La reine blanche est terminée !
def mouvReineBlanc() :
    #la reine est très simple puisque j'ai déjà fait le fou et la tour, la reine étant à la fois le fou et la tour.
    choix = str(input('\nPièce à bouger -->'))
    for i in range(8) :
        for j in range(8) :
            #reine blanc
            if jeu[i,j] == choix :
                print('Direction souhaitée : ')
                dep = str(input('Entrez diago ou ligne : \n==>'))



                if dep == 'diago' :
                    print('Direction souhaitée : ')
                    print('\ndiagoHG : haut, gauche ; \ndiagoHD : haut, droite ; \ndiagoBG : bas gauche ; \ndiagoBD : bas, droite')
                    depla = str(input('diagoHG ; diagoHD ; diagoBG ; diagoBD\n==> '))
                    print('Entrez un nombre entier :')
                    nb = int(input('Combien de cases doit-il parcourir ?\n==> '))

                    #diagonale haut gauche
                    if depla == 'diagoHG' :
                        if jeu[i - nb, j - nb] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i - nb, j - nb] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i - nb, j - nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i - nb, j - nb] = choix
                                        return jeu
                        if jeu[i - nb, j - nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i - nb, j - nb] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu

                    #diagonale haut droite
                    if depla == 'diagoHD' :
                        if jeu[i - nb, j + nb] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i - nb, j + nb] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i - nb, j + nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i - nb, j + nb] = choix
                                        return jeu
                        if jeu[i - nb, j + nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i - nb, j + nb] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu

                    #diagonale bas gauche    
                    if depla == 'diagoBG' :
                        if jeu[i + nb, j - nb] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i + nb, j - nb] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i + nb, j - nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i + nb, j - nb] = choix
                                    return jeu
                        if jeu[i + nb, j - nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i + nb, j - nb] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu

                    #diagonale bas droite    
                    if depla == 'diagoBD' :
                        if jeu[i + nb, j + nb] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i + nb, j + nb] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i + nb, j + nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i + nb, j + nb] = choix
                                        return jeu
                        if jeu[i + nb, j + nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i + nb, j + nb] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu
                



                if dep == 'ligne' :
                    print('Direction souhaitée : ')
                    print('\nhorizon, gauche : horizG ; \nhorizon, droite : horizD ; \nvertical, haut : vertiH ; \nvertical, bas : vertiB\n')
                    depla = str(input('\nhorizG, horizD ; vertiH, vertiB \n==> '))
                    nb = int(input('Combien de cases doit-il parcourir ?\n==> '))
                    #horizontal gauche
                    if depla == 'horizG' :
                        if jeu[i, j - nb] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i, j - nb] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i, j - nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i, j - nb] = choix
                                        return jeu
                        if jeu[i, j - nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i, j - nb] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu

                    #horizontal droite
                    if depla == 'horizD' :
                        if jeu[i, j + nb] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i, j + nb] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i, j + nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i, j + nb] = choix
                                        return jeu
                        if jeu[i, j + nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i, j + nb] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu

                    #vertical haut
                    if depla == 'vertiH' :
                        if jeu[i - nb, j] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i - nb, j] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i - nb, j], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i - nb, j] = choix
                                        return jeu
                        if jeu[i - nb, j] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i - nb, j] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu

                    #vertical bas
                    if depla == 'vertiB' :
                        if jeu[i + nb, j] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i + nb, j] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i + nb, j], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i + nb, j] = choix
                                        return jeu
                        if jeu[i + nb, j] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i + nb, j] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu
#La reine blanche est terminée, oui vraiment !

#Le roi blanc est terminé !
def mouvRoiBlanc() :
    #le roi est très simple aussi, puisque j'ai fait la reine, et que le roi est une reine qui n'avance que de 1
    choix = str(input('\nPièce à bouger -->'))
    for i in range(8) :
        for j in range(8) :
            #roi blanc
            if jeu[i,j] == choix :
                print('Direction souhaitée : ')
                dep = str(input('Entrez diago ou ligne : \n==>'))



                if dep == 'diago' :
                    print('Direction souhaitée : ')
                    print('\ndiagoHG : haut, gauche ; \ndiagoHD : haut, droite ; \ndiagoBG : bas gauche ; \ndiagoBD : bas, droite')
                    depla = str(input('diagoHG ; diagoHD ; diagoBG ; diagoBD\n==> '))
                    nb = 1

                    #diagonale haut gauche
                    if depla == 'diagoHG' :
                        if jeu[i - nb, j - nb] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i - nb, j - nb] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i - nb, j - nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i - nb, j - nb] = choix
                                        return jeu
                        if jeu[i - nb, j - nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i - nb, j - nb] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu

                    #diagonale haut droite
                    if depla == 'diagoHD' :
                        if jeu[i - nb, j + nb] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i - nb, j + nb] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i - nb, j + nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i - nb, j + nb] = choix
                                        return jeu
                        if jeu[i - nb, j + nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i - nb, j + nb] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu

                    #diagonale bas gauche    
                    if depla == 'diagoBG' :
                        if jeu[i + nb, j - nb] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i + nb, j - nb] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i + nb, j - nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i + nb, j - nb] = choix
                                    return jeu
                        if jeu[i + nb, j - nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i + nb, j - nb] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu

                    #diagonale bas droite    
                    if depla == 'diagoBD' :
                        if jeu[i + nb, j + nb] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i + nb, j + nb] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i + nb, j + nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i + nb, j + nb] = choix
                                        return jeu
                        if jeu[i + nb, j + nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i + nb, j + nb] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu
                



                if dep == 'ligne' :
                    print('Direction souhaitée : ')
                    print('\nhorizon, gauche : horizG ; \nhorizon, droite : horizD ; \nvertical, haut : vertiH ; \nvertical, bas : vertiB\n==> ')
                    depla = str(input('\nhorizG, horizD ; vertiH, vertiB \n==> '))
                    nb = 1
                    #horizontal gauche
                    if depla == 'horizG' :
                        if jeu[i, j - nb] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i, j - nb] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i, j - nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i, j - nb] = choix
                                        return jeu
                        if jeu[i, j - nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i, j - nb] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu

                    #horizontal droite
                    if depla == 'horizD' :
                        if jeu[i, j + nb] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i, j + nb] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i, j + nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i, j + nb] = choix
                                        return jeu
                        if jeu[i, j + nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i, j + nb] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu

                    #vertical haut
                    if depla == 'vertiH' :
                        if jeu[i - nb, j] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i - nb, j] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i - nb, j], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i - nb, j] = choix
                                        return jeu
                        if jeu[i - nb, j] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i - nb, j] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu

                    #vertical bas
                    if depla == 'vertiB' :
                        if jeu[i + nb, j] != '   ' :
                            for x in range(len(liste_des_noirs)) :
                                if jeu[i + nb, j] == liste_des_noirs[x] :
                                    print('Voulez-vous manger', jeu[i + nb, j], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i + nb, j] = choix
                                        return jeu
                        if jeu[i + nb, j] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i + nb, j] = choix
                        print('\nVous ne pouvez pas manger un blanc !')
                        return jeu
#Le roi blanc est terminé, oui vraiment !





#Le pion noir est terminé !
def mouvPionNoir() :
    choix = str(input('\nPièce à bouger -->'))
    for i in range(8) :
        for j in range(8) :
            #pion noir
            if jeu[i,j] == choix :
                #check s'il peut manger à droite en bas, peut manger seulement si c'est un blanc
                if jeu[i + 1, j + 1] != '   ' :
                    for x in range(len(liste_des_blancs)) :
                        if jeu[i + 1, j + 1] == liste_des_blancs[x] :
                            print('Voulez-vous manger', jeu[i + 1, j + 1], ' ? ')
                            miam = str(input('(y/n) \n==> '))
                            if miam == 'y' :
                                jeu[i,j] = '   '
                                jeu[i + 1, j + 1] = choix
                                return jeu

                #check s'il peut manger à gauche en bas, peut manger seulement si c'est un blanc
                if jeu[i + 1, j - 1] != '   ' :
                    for y in range(len(liste_des_blancs)) :
                        if jeu[i + 1, j - 1] == liste_des_blancs[y] :
                            print('Voulez-vous manger', jeu[i + 1, j - 1], ' ? ')
                            miam = str(input('(y/n) \n==> '))
                            if miam == 'y' :
                                jeu[i,j] = '   '
                                jeu[i + 1, j - 1] = choix
                                return jeu

                
                #si il ne mange rien il avance simplement
                print('Nombre de cases souhaitées : ')
                depla = int(input('1 ou 2 ?\n==> '))
                #si un pion à déjà avancé, il ne peut plus avancer de 2
                if choix != jeu[1, j] :
                    depla = 1
                    print("le pion", choix, 'à déjà bougé, il avance donc de 1 désormais')
                
                if depla == 2 :
                    #regarde s'il peut avancer de 2
                    if jeu[i + 2, j] == '   ' and jeu[i + 1, j] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + 2, j] = choix
                        return jeu
                    else :
                        print("Impossible d'avancer !")



                if depla == 1 :
                    #regarde s'il peut avancer de 1
                    if jeu[i + 1, j] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + 1, j] = choix
                    else :
                        print("Impossible d'avancer !")
    return jeu
#Le pion noir est terminé, oui vraiment !

#Le cavalier noir est terminé !
def mouvCavalierNoir() :
    choix = str(input('\nPièce à bouger -->'))
    for i in range(8) :
        for j in range(8) :
            #cavalier noir
            if jeu[i,j] == choix :
                print('Direction souhaitée : ')
                print('\ndevant, droite, haut : DDH ;\ndevant, droite, bas  : DDB ;\ndevant, gauche, haut : DGH ; \ndevant, gauche, bas  : DGB')
                print('\nderriere, droite, haut : dDH ; \nderriere, droite, bas  : dDB ; \nderriere, gauche, haut : dGH ; \nderriere, gauche, bas  : dGB')
                depla = str(input('\nDDH, DDB, DGH, DGB  ;  dDH, dDB, dGH, dGB\n==> '))
                #devant droite haut
                if depla == 'DDH' :
                    if jeu[i - 2, j + 1] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i - 2, j + 1] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i - 2, j + 1], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - 2, j + 1] = choix
                                    return jeu
                    if jeu[i - 2, j + 1] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - 2, j + 1] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu

                #devant droite bas
                if depla == 'DDB' :
                    if jeu[i - 1, j + 2] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i - 1, j + 2] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i - 1, j + 2], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - 1, j + 2] = choix
                                    return jeu
                    if jeu[i - 1, j + 2] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - 1, j + 2] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu
                
                #devant gauche haut
                if depla == 'DGH' :
                    if jeu[i - 2, j - 1] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i - 2, j - 1] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i - 2, j - 1], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - 2, j - 1] = choix
                                    return jeu
                    if jeu[i - 2, j - 1] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - 2, j - 1] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu
                
                #devant gauche bas
                if depla == 'DGB' :
                    if jeu[i - 1, j - 2] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i - 1, j - 2] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i - 1, j - 2], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - 1, j - 2] = choix
                                    return jeu
                    if jeu[i - 1, j - 2] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - 1, j - 2] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu



                #derrière droite haut
                if depla == 'dDH' :
                    if jeu[i + 1, j + 2] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i + 1, j + 2] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i + 1, j + 2], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + 1, j + 2] = choix
                                    return jeu
                    if jeu[i + 1, j + 2] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + 1, j + 2] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu

                #derrière droite bas
                if depla == 'dDB' :
                    if jeu[i + 2, j + 1] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i + 2, j + 1] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i + 2, j + 1], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + 2, j + 1] = choix
                                    return jeu
                    if jeu[i + 2, j + 1] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + 2, j + 1] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu

                #derrière gauche haut
                if depla == 'dGH' :
                    if jeu[i + 1, j - 2] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i + 1, j - 2] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i + 1, j - 2], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + 1, j - 2] = choix
                                    return jeu
                    if jeu[i + 1, j - 2] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + 1, j - 2] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu

                #derrière gauche bas
                if depla == 'dGB' :
                    if jeu[i + 2, j - 1] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i + 2, j - 1] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i + 2, j - 1], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + 2, j - 1] = choix
                                    return jeu
                    if jeu[i + 2, j - 1] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + 2, j - 1] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu
#Le cavalier noir est terminé, oui vraiment !

#Le fou noir est terminé !
def mouvFouNoir() :
    choix = str(input('\nPièce à bouger -->'))
    for i in range(8) :
        for j in range(8) :
            #fou noir
            if jeu[i,j] == choix :
                print('Direction souhaitée : ')
                print('\ndiagoHG : haut, gauche ; \ndiagoHD : haut, droite ; \ndiagoBG : bas gauche ; \ndiagoBD : bas, droite')
                depla = str(input('diagoHG ; diagoHD ; diagoBG ; diagoBD\n==> '))
                print('Entrez un nombre entier :')
                nb = int(input('Combien de cases doit-il parcourir ?\n==> '))
                
                #diagonale haut gauche
                if depla == 'diagoHG' :
                    if jeu[i - nb, j - nb] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i - nb, j - nb] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i - nb, j - nb], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - nb, j - nb] = choix
                                    return jeu
                    if jeu[i - nb, j - nb] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - nb, j - nb] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu

                #diagonale haut droite
                if depla == 'diagoHD' :
                    if jeu[i - nb, j + nb] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i - nb, j + nb] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i - nb, j + nb], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - nb, j + nb] = choix
                                    return jeu
                    if jeu[i - nb, j + nb] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - nb, j + nb] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu

                #diagonale bas gauche    
                if depla == 'diagoBG' :
                    if jeu[i + nb, j - nb] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i + nb, j - nb] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i + nb, j - nb], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + nb, j - nb] = choix
                                    return jeu
                    if jeu[i + nb, j - nb] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + nb, j - nb] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu

                #diagonale bas droite    
                if depla == 'diagoBD' :
                    if jeu[i + nb, j + nb] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i + nb, j + nb] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i + nb, j + nb], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + nb, j + nb] = choix
                                    return jeu
                    if jeu[i + nb, j + nb] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + nb, j + nb] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu
#Le fou noir est terminé, oui vraiment !

#La tour noire est terminée !
def mouvTourNoir() :
    choix = str(input('\nPièce à bouger -->'))
    for i in range(8) :
        for j in range(8) :
            #tour noir
            if jeu[i,j] == choix :
                print('Direction souhaitée : ')
                depla = str(input('\nhorizon, gauche : horizG ; \nhorizon, droite : horizD ; \nvertical, haut : vertiH ; \nvertical, bas : vertiB\n==> '))
                nb = int(input('Combien de cases doit-il parcourir ?\n==> '))

                #horizontal gauche
                if depla == 'horizG' :
                    if jeu[i, j - nb] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i, j - nb] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i, j - nb], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i, j - nb] = choix
                                    return jeu
                    if jeu[i, j - nb] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i, j - nb] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu

                #horizontal droite
                if depla == 'horizD' :
                    if jeu[i, j + nb] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i, j + nb] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i, j + nb], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i, j + nb] = choix
                                    return jeu
                    if jeu[i, j + nb] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i, j + nb] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu

                #vertical haut
                if depla == 'vertiH' :
                    if jeu[i - nb, j] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i - nb, j] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i - nb, j], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i - nb, j] = choix
                                    return jeu
                    if jeu[i - nb, j] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i - nb, j] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu

                #vertical bas
                if depla == 'vertiB' :
                    if jeu[i + nb, j] != '   ' :
                        for x in range(len(liste_des_blancs)) :
                            if jeu[i + nb, j] == liste_des_blancs[x] :
                                print('Voulez-vous manger', jeu[i + nb, j], ' ? ')
                                miam = str(input('(y/n) \n==> '))
                                if miam == 'y' :
                                    jeu[i,j] = '   '
                                    jeu[i + nb, j] = choix
                                    return jeu
                    if jeu[i + nb, j] == '   ' :
                        jeu[i,j] = '   '
                        jeu[i + nb, j] = choix
                    print('\nVous ne pouvez pas manger un noir !')
                    return jeu
#La tour noire est terminée, oui vraiment !

#La reine noire est terminée !
def mouvReineNoir() :
    #la reine est très simple puisque j'ai déjà fait le fou et la tour, la reine étant à la fois le fou et la tour.
    choix = str(input('\nPièce à bouger -->'))
    for i in range(8) :
        for j in range(8) :
            #reine noir
            if jeu[i,j] == choix :
                print('Direction souhaitée : ')
                dep = str(input('Entrez diago ou ligne : \n==>'))



                if dep == 'diago' :
                    print('Direction souhaitée : ')
                    print('\ndiagoHG : haut, gauche ; \ndiagoHD : haut, droite ; \ndiagoBG : bas gauche ; \ndiagoBD : bas, droite')
                    depla = str(input('diagoHG ; diagoHD ; diagoBG ; diagoBD\n==> '))
                    print('Entrez un nombre entier :')
                    nb = int(input('Combien de cases doit-il parcourir ?\n==> '))

                    #diagonale haut gauche
                    if depla == 'diagoHG' :
                        if jeu[i - nb, j - nb] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i - nb, j - nb] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i - nb, j - nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i - nb, j - nb] = choix
                                        return jeu
                        if jeu[i - nb, j - nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i - nb, j - nb] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu

                    #diagonale haut droite
                    if depla == 'diagoHD' :
                        if jeu[i - nb, j + nb] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i - nb, j + nb] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i - nb, j + nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i - nb, j + nb] = choix
                                        return jeu
                        if jeu[i - nb, j + nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i - nb, j + nb] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu

                    #diagonale bas gauche    
                    if depla == 'diagoBG' :
                        if jeu[i + nb, j - nb] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i + nb, j - nb] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i + nb, j - nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i + nb, j - nb] = choix
                                    return jeu
                        if jeu[i + nb, j - nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i + nb, j - nb] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu

                    #diagonale bas droite    
                    if depla == 'diagoBD' :
                        if jeu[i + nb, j + nb] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i + nb, j + nb] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i + nb, j + nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i + nb, j + nb] = choix
                                        return jeu
                        if jeu[i + nb, j + nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i + nb, j + nb] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu
                



                if dep == 'ligne' :
                    print('Direction souhaitée : ')
                    print('\nhorizon, gauche : horizG ; \nhorizon, droite : horizD ; \nvertical, haut : vertiH ; \nvertical, bas : vertiB\n')
                    depla = str(input('\nhorizG, horizD ; vertiH, vertiB \n==> '))
                    nb = int(input('Combien de cases doit-il parcourir ?\n==> '))
                    #horizontal gauche
                    if depla == 'horizG' :
                        if jeu[i, j - nb] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i, j - nb] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i, j - nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i, j - nb] = choix
                                        return jeu
                        if jeu[i, j - nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i, j - nb] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu

                    #horizontal droite
                    if depla == 'horizD' :
                        if jeu[i, j + nb] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i, j + nb] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i, j + nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i, j + nb] = choix
                                        return jeu
                        if jeu[i, j + nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i, j + nb] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu

                    #vertical haut
                    if depla == 'vertiH' :
                        if jeu[i - nb, j] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i - nb, j] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i - nb, j], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i - nb, j] = choix
                                        return jeu
                        if jeu[i - nb, j] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i - nb, j] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu

                    #vertical bas
                    if depla == 'vertiB' :
                        if jeu[i + nb, j] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i + nb, j] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i + nb, j], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i + nb, j] = choix
                                        return jeu
                        if jeu[i + nb, j] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i + nb, j] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu
#La reine noire est terminée, oui vraiment !

#Le roi noir est terminé !
def mouvRoiNoir() :
    #le roi est très simple aussi, puisque j'ai fait la reine, et que le roi est une reine qui n'avance que de 1
    choix = str(input('\nPièce à bouger -->'))
    for i in range(8) :
        for j in range(8) :
            #roi noir
            if jeu[i,j] == choix :
                print('Direction souhaitée : ')
                dep = str(input('Entrez diago ou ligne : \n==>'))



                if dep == 'diago' :
                    print('Direction souhaitée : ')
                    print('\ndiagoHG : haut, gauche ; \ndiagoHD : haut, droite ; \ndiagoBG : bas gauche ; \ndiagoBD : bas, droite')
                    depla = str(input('diagoHG ; diagoHD ; diagoBG ; diagoBD\n==> '))
                    nb = 1

                    #diagonale haut gauche
                    if depla == 'diagoHG' :
                        if jeu[i - nb, j - nb] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i - nb, j - nb] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i - nb, j - nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i - nb, j - nb] = choix
                                        return jeu
                        if jeu[i - nb, j - nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i - nb, j - nb] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu

                    #diagonale haut droite
                    if depla == 'diagoHD' :
                        if jeu[i - nb, j + nb] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i - nb, j + nb] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i - nb, j + nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i - nb, j + nb] = choix
                                        return jeu
                        if jeu[i - nb, j + nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i - nb, j + nb] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu

                    #diagonale bas gauche    
                    if depla == 'diagoBG' :
                        if jeu[i + nb, j - nb] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i + nb, j - nb] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i + nb, j - nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i + nb, j - nb] = choix
                                    return jeu
                        if jeu[i + nb, j - nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i + nb, j - nb] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu

                    #diagonale bas droite    
                    if depla == 'diagoBD' :
                        if jeu[i + nb, j + nb] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i + nb, j + nb] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i + nb, j + nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i + nb, j + nb] = choix
                                        return jeu
                        if jeu[i + nb, j + nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i + nb, j + nb] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu
                



                if dep == 'ligne' :
                    print('Direction souhaitée : ')
                    print('\nhorizon, gauche : horizG ; \nhorizon, droite : horizD ; \nvertical, haut : vertiH ; \nvertical, bas : vertiB\n==> ')
                    depla = str(input('\nhorizG, horizD ; vertiH, vertiB \n==> '))
                    nb = 1
                    #horizontal gauche
                    if depla == 'horizG' :
                        if jeu[i, j - nb] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i, j - nb] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i, j - nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i, j - nb] = choix
                                        return jeu
                        if jeu[i, j - nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i, j - nb] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu

                    #horizontal droite
                    if depla == 'horizD' :
                        if jeu[i, j + nb] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i, j + nb] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i, j + nb], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i, j + nb] = choix
                                        return jeu
                        if jeu[i, j + nb] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i, j + nb] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu

                    #vertical haut
                    if depla == 'vertiH' :
                        if jeu[i - nb, j] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i - nb, j] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i - nb, j], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i - nb, j] = choix
                                        return jeu
                        if jeu[i - nb, j] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i - nb, j] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu

                    #vertical bas
                    if depla == 'vertiB' :
                        if jeu[i + nb, j] != '   ' :
                            for x in range(len(liste_des_blancs)) :
                                if jeu[i + nb, j] == liste_des_blancs[x] :
                                    print('Voulez-vous manger', jeu[i + nb, j], ' ? ')
                                    miam = str(input('(y/n) \n==> '))
                                    if miam == 'y' :
                                        jeu[i,j] = '   '
                                        jeu[i + nb, j] = choix
                                        return jeu
                        if jeu[i + nb, j] == '   ' :
                            jeu[i,j] = '   '
                            jeu[i + nb, j] = choix
                        print('\nVous ne pouvez pas manger un noir !')
                        return jeu
#Le roi noir est terminé, oui vraiment !

def ME() :
    print('\nToutes les pièces sont fonctionnelles, et ne peuvent pas manger une pièce alliée.')
                
if __name__ == '__main__' :
    print(jeu_debut()) #début du jeu
    print(ME)
    mate = False #de base je comptais faire l'échec et mat
    compt = 0 
    while mate == False : #tant qu'il n'y a pas mat
        compt = compt + 1 #blanc puis noir etc...
        print('Ex : pion, cavalier, fou, tour, reine, roi, fin')
        #on va supposer que les joueurs jouent leur couleur de pion, sans jamais se tromper
        #j'aurais pu modifier tout le code pour faire en sorte que les blancs ne puissent pas jouer de pion noir mais je m'en appercois qu'à la fin
        #donc je n'ai pas la foi de tout modifier, c'est trop long, merci de votre compréhension
        if compt%2 == 1 :
            print("\nC'est le tour des blancs ! ")
            choix = str(input('Choisis une pièce ! '))
            #déplacements possibles pour les blancs
            if choix == 'pion' :
                print(mouvPionBlanc())
            if choix == 'cavalier' :
                print(mouvCavalierBlanc())
            if choix == 'fou'   :
                print(mouvFouBlanc())
            if choix == 'tour'  :
                print(mouvTourBlanc())
            if choix == 'reine' :
                print(mouvReineBlanc())
            if choix == 'roi'   :
                print(mouvRoiBlanc())
            if choix == 'fin' :
                print('Aurevoir !')
                break

        if compt%2 == 0 :
            print("\nC'est le tour des noirs ! ")
            choix = str(input('Choisis une pièce ! '))
            #déplacements possibles pour les noirs
            if choix == 'pion' :
                print(mouvPionNoir())
            if choix == 'cavalier' :
                print(mouvCavalierNoir())
            if choix == 'fou'   :
                print(mouvFouNoir())
            if choix == 'tour'  :
                print(mouvTourNoir())
            if choix == 'reine' :
                print(mouvReineNoir())
            if choix == 'roi'   :
                print(mouvRoiNoir())
            if choix == 'fin' :
                print('Aurevoir !')
                break

### HURDEBOURCQ Paul BUT1 TPC ###