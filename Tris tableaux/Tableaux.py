#TD2 TPC Hurdebourcq Paul
#Exo 1 :

from numpy import *
import random as rdm

def mode_demploi() -> str :
    print("\nProgramme du tableau : Saisir un chiffre compris entre 1 et 7 ci-dessous pour obtenir le résultat.")
    print("Attention : Un tableau de taille variante (choisie pas l'utilisateur) est créé au préalable, tentez de l'afficher grâce au 2 !")
    print('IMPORTANT : La première valeur entrée correspond à la longueur du tableau souhaitée, et non à une action à effectuer !')
    print("\n1 : remplir aleatoirement le tableau ; \n2 : afficher le tableau ; \n3 : trouve le minimum ; \n4 : occurence d'un chiffre ; \n5 : recherche d'index ; \n6 : moyenne des valeurs ; \n7 : quitter ")

def creer_tab(taille : int) -> ndarray :
    tab = zeros(taille, dtype = int)
    return tab

def remplir_tab(tab : ndarray) -> ndarray :
    for i in range(len(tab)) :
        tab[i] = random.randint(0,9)
    return tab

def affiche_tab(taille : int) -> ndarray:
    return creer_tab(taille)

def mini_tab(tab : ndarray) -> int :
    mini = tab[-1] #je choisis la dernière valeur du tableau mais ce n'est pas spécialement important
    for i in range(len(tab)) :
        if tab[i] < mini :
            mini = tab[i]
    return mini

def occu_tab(tab : ndarray, chiffre : int) -> int :
    compt = 0
    for i in range(len(tab)) :
        if tab[i] == chiffre :
            compt += 1
    return compt

def rech_tab(tab : ndarray, val : int) -> list :
    places = []
    for i in range(len(tab)) :
        if tab[i] == val :
            places.append(i)
    return places

def moy_tab(tab : ndarray) -> float :
    moyenne = 0
    compt = 0
    for i in range(len(tab)) :
        compt = compt + 1
        moyenne += tab[i]
    moyenne /= compt
    return moyenne

def fini() -> None :
    return None #une fonction doit renvoyer une valeur, non pas print une chaîne de caractères


       
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

        if action == 3 :
            mini = mini_tab(tableau)
            print('voila le minimum du tab : ', mini)

        if action == 4 :
            chiffre = int(input('chiffre recherché ? '))
            print('l"occurence de :', chiffre,'est', occu_tab(tableau, chiffre))
        
        if action == 5 :
            val = int(input('chiffre recherché ? '))
            print(val, 'est présent à l"index', rech_tab(tab, val))

        if action == 6 : 
            print('la moyenne du tab', tab, 'est', moy_tab(tab))

        if action == 7 :
            print('Fin du programme, à bientôt !', fini())

#Hurdebourcq Paul
#TD2 TPC