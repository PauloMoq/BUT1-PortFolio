#%%
# projet python semaine 1
# -------------------------------------------------
# année 2021-2022 S1
# Ceinture Blanche
# -------------------------------------------------
# Nom-Prénom : Hurdebourcq Paul
# -------------------------------------------------
# variables à portée globale
# -------------------------------------------------
tableau_lettrechiffre=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
tableau_lettres=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# -------------------------------------------------
# fonctions
# -------------------------------------------------
# décalage de 1

def fonction1(lettre: str)-> str:
    tableau_lettrechiffre=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    tableau_lettres=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    """fonction1 :  effectue un décalage de 1 case dans un tableau de lettres.

    Args:
        lettre (str) : lettre est un element du tableau de lettres (tableau_lettres).

    Returns:
        str : nouvelle lettre.
    """
    # assertion, verification des paramètres d'appel
    assert lettre in tableau_lettres, "fonction1 : la lettre doit être dans le tableau : tableau_lettres."

    place=tableau_lettres.index(lettre)
    if place!=25:
        nvlle_lettre=tableau_lettres[place+1]
    else:
        nvlle_lettre=tableau_lettres[0]
    return nvlle_lettre
# -------------------------------------------------
# décalage de 2
def fonction2(lettre: str)-> str:
    """fonction2 :  effectue un décalage de 2 cases dans un tableau de lettres.

    Args:
        lettre (str) : lettre est un element du tableau de lettres (tableau_lettres).

    Returns:
        str : nouvelle lettre.
    """
    # assertion, verification des paramètres d'appel
    assert lettre in tableau_lettres, "fonction2 : la lettre doit être dans le tableau : tableau_lettres."

    place=tableau_lettres.index(lettre)
    if place!=25 and place!=24:
        nvlle_lettre=tableau_lettres[place+2]
    elif place==24 :
        nvlle_lettre=tableau_lettres[0]
    else :
        nvlle_lettre=tableau_lettres[1]
    return nvlle_lettre

# décalage de cle
def Cesar(lettre: str,cle: int)-> str:
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
    place= place + cle         
    nvlle_lettre=tableau_lettres[place%26]
    return nvlle_lettre

# écrire ici Cesar_inverse

# -------------------------------------------------------
# programme principal
# -------------------------------------------------------
def cesar_inverse(lettre :str, cle : int) :
    assert lettre in tableau_lettres, "Cesar : la lettre doit être dans le tableau : tableau_lettres."
    
    place=tableau_lettres.index(lettre)
    place= place - cle         
    nvlle_lettre=tableau_lettres[place%26]
    return nvlle_lettre
if __name__ == "__main__":
    print("-- ceinture blanche --")
    # compléter avec les jeux d'essais



# %%
