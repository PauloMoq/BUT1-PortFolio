#%%
# projet python semaine 1
# -------------------------------------------------
# année 2021-2022 S1
# Ceinture Jaune
# -------------------------------------------------
# Nom-Prénom :
# -------------------------------------------------
# variables à portée globale
# -------------------------------------------------

from typing import List


tableau_lettrechiffre=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

tableau_lettres=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# -------------------------------------------------
# fonctions

# -------------------------------------------------
#décalage de cle
def Cesar(lettre: str,cle: int, tableau : int) -> str:
    """Cesar :  effectue un décalage de clé cases dans un tableau de lettres.

    Args:
        lettre (str) : lettre est un element du tableau de lettres (tableau_lettres).
        cle (int) : clé de codage

    Returns:
        str : nouvelle lettre.
    """
    # assertion, verification des paramètres d'appel
    assert lettre in tableau_lettres, "Cesar : la lettre doit être dans le tableau : tableau_lettres."

    place=tableau_lettres.index(lettre)
    place=(place+cle)%26
    nvlle_lettre=tableau_lettres[place]

    return nvlle_lettre


# écrire ici Cesar_plus
def Cesar_plus(lettre: str,cle:int,tableau:int) -> str:

    assert lettre in tableau
    place=tableau.index(lettre)
    place=(place*cle)%len(tableau)
    nvlle_lettre=tableau[place]


    return nvlle_lettre




#application de cesar sur un texte
def Cesar_texte(texte:str, cle1, tab = tableau_lettres)-> str:
    """Cesar_texte :  encode le texte.

    Args:
        texte (str) : texte à encoder.

    Returns:
        str : texte codé.
    """
    nveau_texte=[] #tab vide
    compt = (-1) #compteur qui commence à 0
    tableau_lettres.append(texte) #plusieurs caractères
    for j in range(len(texte)): #1e lettre, 2e etc
        compt += 1 #compteur + 1
        dec = Cesar(lettre = texte[compt], cle = cle1) #decalage de la lettre 
        print('le decalage :', dec) #pas besoin
        print('le compteur :', compt) #same
        nveau_texte += dec #on ajoute chaque lettre décalée 1 à 1
    print('le texte :', str(nveau_texte)) #résultat

# écrire ici Cryptage_lineaire
def cryptage_lineaire(texte:str,cle:int,tableau:int):
    nveau_texte=''
    for i in range(len(texte)):
        j=Cesar_plus(texte[i],cle,tableau_lettres)
        nveau_texte=nveau_texte+j
    return nveau_texte
    

# écrire ici Decryptage_lineaire  #non

# écrire ici Cryptrage_affine
def Cryptage_Affine(texte:str,a:int,b:int,tableau:int) -> str:

    nveau_texte = ''
    for i in range(len(texte)):
        nveau_texte = nveau_texte + Cesar_plus(Cesar(texte[i],a,tableau),b,tableau)

    return nveau_texte

# -------------------------------------------------------
# programme principal
# -------------------------------------------------------
'''if name == "main":
    print("-- ceinture jaune --")
    # compléter avec les jeux d'essais'''

# %%