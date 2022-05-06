#TD2 TPC Hurdebourcq Paul
#Exo 2 :

#je réutilise mes fonctions de l'exercice précédent

from numpy import *
import random as rdm

def creer_tab(taille : int) -> ndarray :
    tab = zeros(taille, dtype = int)
    return tab

def remplir_tab(tab : ndarray) -> ndarray :
    for i in range(len(tab)) :
        tab[i] = random.randint(0,9)
    return tab

def affiche_tab(taille : int) -> ndarray:
    return creer_tab(taille)

def fini() -> None :
    return None #une fonction doit renvoyer une valeur, et non une chaîne de caractères

#fin de je réutilise mes fonctions de l'exercice précédent

def mode_demploi() -> str :
    print('\nProgramme des Tris : Veuillez choisir un chiffre compris entre 1 et 7 pour obtenir un résultat.')
    print("Attention : Un tableau de taille variante (choisie pas l'utilisateur) est créé au préalable, tentez de l'afficher grâce au 2 !")
    print('IMPORTANT : La première valeur entrée correspond à la longueur du tableau souhaitée, et non à une action à effectuer !')
    print("\n1 : remplir aleatoirement le tableau ; \n2 : afficher le tableau ; \n3 : tri à bulles ; \n4 : tri par sélection ; \n5 : tri par insertion ; \n6 : tri par fusion ; \n7 : quitter ")

def rappel_ME() -> str :
    print("\n1 : remplir aleatoirement le tableau ; \n2 : afficher le tableau ; \n3 : tri à bulles ; \n4 : tri par sélection ; \n5 : tri par insertion ; \n6 : tri par fusion ; \n7 : quitter ")

def tri_bulles(tab : ndarray) -> ndarray : #le but est de comparer si un tab[i] est supérieur à un tab[i + 1]
    taille = len(tab)
    permut = True
    while permut == True : #on continue tant qu'on réussis à permuter (si on ne peux plus permuter, c'est que le tableau est trié)
        permut = False
        for i in range(0, taille - 1) : 
            if tab[i] > tab[i + 1] : #on permute 
                tab[i], tab[i + 1] = tab[i + 1], tab[i]
                permut = True
        taille = taille - 1 #la dernière case n'est plus a considérer
        print(tab) #pour voir les étapes lors de l'éxecution
    return tab

def tri_selection(tab : ndarray) -> ndarray : #le but est de chercher le minimum est de le placer
    for indexi in range(len(tab)) :
        min = indexi #on trouve le minimum
        for indexj in range(indexi + 1, len(tab)) :
            if tab[min] > tab[indexj] :
                min = indexj
        tab[indexi], tab[min] = tab[min], tab[indexi]
        print(tab) #pour voir les étapes lors de l'éxecution
    return tab

def tri_insertion(tab : ndarray) -> ndarray : #le but est de déplacer la valeur souhaitée case par case
    for i in range(1, len(tab)) :
        indexi = tab[i]
        indexj = i - 1
        while indexj >= 0 and tab[indexj] > indexi :
            tab[indexj + 1] = tab[indexj]
            indexj -= 1
        tab[indexj + 1] = indexi
        print(tab) #pour voir les étapes lors de l'éxecution
    return tab




#J'avoue celui-ci j'ai eu besoin d'aide :'(
def tri_fusion(tableau):

    if  len(tableau) <= 1: 
        return tableau

    pivot = len(tableau)//2

    tableau1 = tableau[:pivot]

    tableau2 = tableau[pivot:]

    gauche = tri_fusion(tableau1)

    droite = tri_fusion(tableau2)

    fusionne = fusion(gauche,droite)


    return fusionne



def fusion(tableau1,tableau2):

    indice_tableau1 = 0
    indice_tableau2 = 0    
    taille_tableau1 = len(tableau1)
    taille_tableau2 = len(tableau2)
    tableau_fusionne = []

    while indice_tableau1<taille_tableau1 and indice_tableau2<taille_tableau2:

        if tableau1[indice_tableau1] < tableau2[indice_tableau2]:
            tableau_fusionne.append(tableau1[indice_tableau1])
            indice_tableau1 += 1

        else:
            tableau_fusionne.append(tableau2[indice_tableau2])
            indice_tableau2 += 1

    while indice_tableau1<taille_tableau1:

        tableau_fusionne.append(tableau1[indice_tableau1])
        indice_tableau1+=1
    
    while indice_tableau2<taille_tableau2:

        tableau_fusionne.append(tableau2[indice_tableau2])
        indice_tableau2+=1
       
    
    return tableau_fusionne



#même début de programme que l'exo précédent
if __name__ == '__main__' :
    mode_demploi()
    longueur = int(input('---> longueur du tab : '))
    action = 0
    tableau = creer_tab(longueur) #créé au préalable, pour ne pas interférer avec l'énoncé du TP
    while action != 7 :
        action = int(input('choisis un chiffre ci-dessus : '))

        if action == 1 :
            tab = remplir_tab(tableau)
            print('le tableau est modifié !')

        if action == 2 :
            print('voila votre tableau', tableau)
#fin de même début de programme que l'exo précédent
        
        if action == 3 :
            print('Un classique, le tri à bulles :', tri_bulles(tableau), '\n\n\n')
            rappel_ME() #affiche les options à nouveau : non nécessaire au programme évidemment 

        if action == 4 :
            print('Voilà le tri par sélection :', tri_selection(tableau), '\n\n\n')
            rappel_ME() #affiche les options à nouveau : non nécessaire au programme évidemment

        if action == 5 :
            print('Voici le tri par insertion :', tri_insertion(tableau), '\n\n\n')
            rappel_ME() #affiche les options à nouveau : non nécessaire au programme évidemment
        
        if action == 6 :
            print("Vous l'attendiez, le voilà, le tri fusion !!! :", tri_fusion(tableau), '\n\n\n')
            print("J'ai eu besoin d'aide pour celui-ci, désolé")
            rappel_ME() #affiche les options à nouveau : non nécessaire au programme évidemment

        if action == 7 :
            print('Fin du programme, à bientôt !', fini())

#Hurdebourcq Paul
#TD2 TPC