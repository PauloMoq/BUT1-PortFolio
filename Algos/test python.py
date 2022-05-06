if __name__ == "__main__" :
    tableau = []
    for i in range(10) :
        dico = []
        for j in range(10) :
            dico.append({'contenu' : 'Eau', 'numero' : 0, 'etat' : 'Neuf'})
        tableau.append(dico)

    #Dans chaque case du tableau, on met le dico ci-dessus