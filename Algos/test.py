import numpy as np
tableau = np.array([['Anne','Tom','Léo','Eva'], [6,7,8,9],[10,20,30,40]])
print("Tableau\n", tableau,'\n')
print("Ligne\n", tableau[0],'\n')
print("Elément d'une ligne\n", tableau[0][0],'\n')
print("Elément d'une ligne\n", tableau[1][2],'\n')
print("Elément d'une ligne, à partir de la fin\n", tableau[-1][-1],'\n')
print("Elément d'une ligne, à partir de la fin\n",tableau[-1][0], "\n")
print("Transposition\n", tableau.T, "\n")
print("Partie de tableau\n", tableau[0:3,1:3], "\n")
print("Colonne\n", tableau[:,0], "\n")


jeu = np.array([['aa8','bb8','cc8','dd8','ee8','ff8','gg8','hh8'], 
                  ['aa7','bb7','cc7','dd7','ee7','ff7','gg7','hh7'],
                  ['   ','   ','   ','   ','   ','   ','   ','   '],
                  ['   ','   ','   ','   ','   ','   ','   ','   '],
                  ['   ','   ','   ','   ','   ','   ','   ','   '],
                  ['   ','   ','   ','   ','   ','   ','   ','   '],
                  ['aa2','bb2','cc2','dd2','ee2','ff2','gg2','hh2'],
                  ['aa1','bb1','cc1','dd1','ee1','ff1','gg1','h1']])

if __name__ == '__main__' :
    print(jeu[6][0])