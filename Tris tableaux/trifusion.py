### HURDEBOURCQ Paul Victor ###
    ### BUT1 TPC ###

###TRI FUSION EN TROIS PARTIES###

import numpy as np
import random as rdm

MAX = 10
vecteur = np.empty(MAX,dtype=int)

def eclatement(V:vecteur,V1:vecteur,V2:vecteur):
    '''Les éléments de V sont répartis dans V1 et V2
    V1 contient les monotonies de rang impair, V2 celles de rang pair'''
    precedent = V[1]
    rangerdansV1 = True
    i1 = 0
    i2 = 0
    for i in range(MAX):
        if V[i] < precedent:
            rangerdansV1 = False
        if rangerdansV1 :
            i1 += 1
            V1[i1] = V1[i]
        else :
            i2 += 1
            V2[i2] = V2[i]
        precedent = V[i] 





def fusion(V:vecteur,V1:vecteur,V2:vecteur,nb1:int,nb2:int):
    i = 1
    i1 = 1
    i2 =1 
    while(i1 <=  nb1 and i2<=nb2):
        if V1[i1] <= V2[i2]:
            V[i] =  V1[i1]
            i1 = i1 + 1
        else:
            V[i] = V2[i2]
            i2 = i2 +1 
        i = i+1
    while(i1 <= nb1):
        V[i] = V1[i1]
        i1 = i1 + 1
        i = i + 1
    while(i2<= nb2):
        V[i] = V2[i2]
        i2 = i2 + 1
        i = i + 1


def tri_fusion_eclatement(v1:vecteur,v2:vecteur,nb1:int,nb2:int) :
    eclatement(v1, v2, nb1, nb2)
    while nb2 != 0 :
        fusion(v1, v2, nb1, nb2)
        eclatement(v1, v2, nb1, nb2)


def mode_demploi():
    print("\n  Bienvenue dans la matrix, la matrix est universelle.\n  Vous avez plusieurs fonctions à votre disposition :\n     [1] eclatement : sépare un tableau en un autre avec ces valeurs impaire, et l'autre avec ces valeurs paires.\n     [2] fusion : Effectue la méthode du tri par fusion.\n     [3] tri_fusion_eclatement : Effectue l'éclatement puis la fusion.")
    choice = int(input(("--> ")))
    if choice == 1:
        eclatement()
    if choice == 2:
        fusion()
    if choice == 3:
        tri_fusion_eclatement()
    if choice == 5:
        print("\n   - Fin du programme -\n")
        quit()

if __name__ == "__main__" :
    V1 = vecteur
    V2 = vecteur
    V = np.array([rdm.randint(1,10),rdm.randint(1,10),rdm.randint(1,10),rdm.randint(1,10),rdm.randint(1,10),rdm.randint(1,10),rdm.randint(1,10),rdm.randint(1,10),rdm.randint(1,10),rdm.randint(1,10)],dtype=int)
    n1:int = int(input("    Entrez n1 :"))
    n2:int = int(input("    Entrez n2 :"))
    mode_demploi()
