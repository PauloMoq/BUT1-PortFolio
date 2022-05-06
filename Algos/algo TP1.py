#%%

#HURDEBOURCQ PAUL BUT1 TPC 
#Algos :


#Pour utiliser chaque fonction, il suffira d'enlever les # devant le princpal de la fonction.
#1
def taxe(prixHT) :
    prixTTC = prixHT*1.2
    print('purée téma lbazar !', prixTTC)
#2   
def switch(x, y) :
    var = x
    x = y
    y = var
    return x,y
#3
def novariable(a,b) :
    a,b = b,a
    print(a,b)
#4
def permut(x,y,z) :
    x,y,z = y,z,x
    return x,y,z
#5
def menus(cb_damis):
    compt = 0
    for i in range(cb_damis) :
        print('Choisis le menu n°', i+1, (' [menu1 : 15€ ; menu2 : 20€ ; menu3 : 25€ ; BOISSON COMPRISE]'))
        print('Entre le numéro du menu genre 1, 2 ou 3 !')
        prix_menu = int(input('--->'))
        if prix_menu == 1 :
            prix_menu = 15
        if prix_menu == 2 :
            prix_menu = 20
        if prix_menu == 3 :
            prix_menu = 25
        compt += prix_menu
        print('Pour l"instant' , compt, '€')
    print('Rien d"autre ?' ' Ok ça fait', compt, '€', 'au prochain guichet bg !')

#if __name__ == "__main__":
#    cb_damis = int(input("Nb damis --> "))
#    menus(cb_damis)

#6
def temps(secondes) :
    #Programme Convertion seconde en heure,minute,seconde Exercice 7
    heure = secondes / 3600
    secondes = secondes % 3600
    minute = secondes / 60
    secondes = secondes % 60
    print("=", int(heure) ,"heure(s)",int(minute),"minute(s)",int(secondes),"seconde(s)")
    

#if __name__ == '__main__' :
#    secondes = int(input('Secondes --->'))  
#    temps(secondes)

#7
def tri(x,y,z) :
    if x > y :
        var = x
        x = y
        y = var
    if y > z :
        var = y   
        y = z
        z = var
        if x > y :
            var = x
            x = y
            y = var
    print('Ordre croissant (pas chocolatine hein)' , x,y,z)

#if __name__ == '__main__' :
#    x = int(input('x --->'))  
#    y = int(input('y --->')) 
#    z = int(input('z --->')) 
#    tri(x,y,z)

#8
def IMC(poids,taille) :
    imc = poids/(taille*taille)
    if imc < 18.5 : 
        print('Insufisance pondérale')
    if imc > 18.5 and imc <= 25 :
        print('Corpulence normale')
    if imc > 25 and imc <= 30 :
        print('Surpoids')
    if imc > 30 and imc <= 35 :
        print('Obésité modérée')
    if imc > 35 :
        print('Obésité sévère')
    return imc

#if __name__ == '__main__' :
#    poids = int(input('poids --->'))
#    taille = float(input('taille --->'))
#    print(IMC(poids,taille))

#9
def number(nb_pos_imp): 
    while nb_pos_imp % 2 == 0 or nb_pos_imp < 0 :
        nb_pos_imp = int(input("Donnez un nombre strictement positif et impair"))
        if nb_pos_imp < 0 :
            print("Nombre positif seulement")
        elif nb_pos_imp > 0 or nb_pos_imp % 2 == 0 :
            print("Nombre positif mais pair")
    print("Saisie valide")

#if __name__ == '__main__' :
#    nb_pos_imp = int(input('Donnez un nombre positif et impair --->'))
#    number(nb_pos_imp)

#10
def sommedch(nb_pos) :
    somme = 0 
    nbvierge = nb_pos
    if nb_pos < 0 :
        print('Nb strictement positif stp')
        print('Réessaie') 
    while nb_pos > 0 :
        print(nb_pos)
        somme += nb_pos % 10
        nb_pos //= 10
    print('La somme des chiffres de ton nombre', nbvierge, 'est :', somme)

#if __name__ == '__main__' :
#    nb_pos = int(input('nb positif ou nul stp --->'))
#    sommedch(nb_pos)
        
#11
def EgaliteSomme(nb1, nb2 = 201) :
    nb1debut = 1
    for i in range(nb1, nb2) :
        nb1dernier = i % 10
        nb1milieu = (i // 10) - 10
        check1 = nb1debut + nb1milieu
        check2 = nb1milieu + nb1dernier
        check3 = nb1debut + nb1dernier
        if check1 == nb1dernier or check2 == nb1debut or check3 == nb1milieu :
            print(i, end=',')


#if __name__ == '__main__' :
#    EgaliteSomme(100)


def Etoiles(figure) :
    if figure == 'ligne' :
        for _ in range(1,6) :
            print('*', end=' ')

if __name__ == '__main__' :
    figure = str(input('---> ligne, --->'))
    Etoiles(figure)
# %%
