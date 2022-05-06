### Programme Calculette ###
# Ce programme simule quelques opérations basiques d'une calculatrice.
# Le code étant inclut dans un unique programme principal,
# il est inutile d'importer ce module dans un autre.
# (Code source libre sans licence)

# Exercice : comme pour le TD correspondant, extraire les fonctions indiquées.

def mode_demploi() -> str :
    print("\nCalculette : saisir deux nombres séparés par un opérateur pour obtenir le résultat.")
    print("Attention : un espace doit séparer chaque élément.")
    print("Les opérateurs reconnus sont : + (addition), - (soustraction), / (division réelle),")
    print("                               d (division entière), p (puissance) et")
    print("                               s (sortie du programme sans prendre en compte les 2 nombres).")

def erreur_operateur(operateur : str) -> str :
    print("L'opérateur",operateur,"n'est pas reconnu par la calculette.")
    print('Sortie du programme')

def addition(nombre1 : float, nombre2 : float) -> float :
    return(nombre1 + nombre2)

def soustraction(nombre1 : float, nombre2 : float) -> float :
    return(nombre1 - nombre2)

def multiplication(nombre1 : float, nombre2 : float) -> float :
    return(nombre1 * nombre2)

def division_reelle(nombre1 : float, nombre2 : float) -> float :
    if nombre2 != 0 :
        return(nombre1 / nombre2)
    else :
        print('Division par zéro !')

def division_entiere(nombre1 : float, nombre2 : float) -> int :
    q = nombre1 // nombre2
    r = nombre1 % nombre2
    return(q, r)
    
if __name__ == "__main__":
    nombre1:float;nombre2:float;resultat:float
    nombre1str:str;nombre2str:str;operateur:str
    nombre2int:int;i:int
    mode_demploi()
    operateur=''
    while operateur != 's' :
        nombre1str,operateur,nombre2str=input('? ').split() # permet de lire les 3 variables séparées par des espaces
        nombre1=float(nombre1str)
        nombre2=float(nombre2str)
        if operateur == '+' :
            addition(nombre1, nombre2)
            print('=', nombre1 + nombre2)
        elif operateur == '-' :
            soustraction(nombre1, nombre2)
            print('=', nombre1 - nombre2)
        elif operateur == '*' :
            multiplication(nombre1, nombre2)
            print('=', nombre1 * nombre2)
        elif operateur == '/' :
            print('=', nombre1 / nombre2)
        elif operateur == 'd' : # division entière
            division_entiere(nombre1, nombre2)
            print("quotient =", int(nombre1//nombre2))
            print("reste =", nombre1%nombre2)
        elif operateur == 'p': # puissance : attention l'exposant doit être un entier
            resultat=1
            nombre2int=int(nombre2)
            for i in range(nombre2int):
                resultat=resultat*nombre1
            print(nombre1,"^",nombre2int,"=",resultat)
        elif operateur == 's':
            erreur_operateur(operateur)
        else:
            mode_demploi()



            if __name__ == '__main__' :
    mode_demploi()
    action = str(input('choisis une action ci-dessus : '))
    while action != 'fin' :
        longueur = int(input('---> longueur du tab'))
        tab = creer_tab(longueur)
        action = str(input('choisis une action ci-dessus : '))
        if action == 'creer_tab' :
            creer_tab(longueur)

        if action == 'remplir_tab' :
            remplir_tab(tab)

        if action == 'affiche_tab' :
            affiche_tab(tab)