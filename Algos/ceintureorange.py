#%%
tableau_lettrechiffre=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

tableau_lettres=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#valeur du PGCD des nombres a et b
def pgcd(a:int,b:int)-> int:
    """"pgcd :  calcule le pgcd entre a et b.

    Args:
        a (int) : nombre
        b (int): nombre

    Returns:
        int : pgcd entre a et b.
    """
    while b!=0:
        r=a%b
        a,b=b,r
    return a

def Cryptage_affine2(texte:str,a:int,b:int,tableau : int)-> str:
    if tableau == 1:
        for i in range(len(texte)):
            place=tableau_lettres.index(texte[i])
            a=pgcd(a,b)
            place=(place*a,b)%26
            nvell_lettre=tableau_lettres[place]
            print(nvell_lettre,end = "")
            i = i+1
    elif tableau ==2:
        for i in range(len(texte)):
            place=tableau_lettrechiffre.index(texte[i])
            place=(place*a,b)%36
            nvell_lettre=tableau_lettrechiffre[place]
            print(nvell_lettre,end = "")
            i = i+1
    else:
        print("invalide")

def Inverse_mod(a,n):
    for i in range(0,n):
        if i*a%n==1:
            resultat = i
            print(i)

def Decryptage_affine(texte:str,a:int,b:int,cle:int)-> str:
    for i in range(len(texte)):
        place = tableau_lettres.index(texte[i])
        Inverse_mod(place,cle)
        resultat=i
        place =int((resultat-b)/a)
        nvlle_lettre=tableau_lettres[place]
        print(nvlle_lettre,end = "")
        i=i+1
     


# -------------------------------------------------------
# programme principal
# -------------------------------------------------------
if __name__ == "__main__":
    print("-- ceinture orange --")
    # compléter avec les jeux d'essais
# %%
