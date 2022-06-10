/*############################################################################################################### */
/* Groupe n°19 : Fournier Benjamin (TPC) & Hurdebourcq Paul (TPC)                                                 */
/*############################################################################################################### */

/* Question n°1 : */

/* Il semble en effet que certains articles ou catégories ne soient jamais commandés est-ce le cas ? */
 
 select distinct(numarticle) from detailcommande order by numarticle ;
  numarticle
------------
          1
          2
          3
          4
          5
          6
          8
          9
         10
         11
         12
         13
         14
         15
         16
         17
         18
         19
         20
         21
         22
         23
         24
         25
         26
         27
         28
         29
         30
         31
         32
(31 lignes)

/* On voit en effet que seulement 31 lignes sont trouvées alors que l'on a 32 numarticle distincts, il en manque donc un, ici le 7. Le numarticle 7 n'as pas été commandé. */



/*############################################################################################################### */

/*############################################################################################################### */

/* Question n°2 : */

/* Une action commerciale a été menée il y a 3 semaines sur les clients basés en Suisse. L’entreprise
souhaiterait savoir s’il y a eu un effet sur les commandes. (Indice : Vous présenterez les résultats de
vente cad le chiffre d’affaires par mois et le chiffre d’affaires par numéro de semaine). */



/* On choisit ici les clients avec le codeetiquette 'CH', la Suisse, et on regarde leurs commandes. */

/* CHIFFRE D'AFFAIRES HT */

select numclient,datecommande,montantht from commande where numclient in(select numclient from client where codeetiquette like'CH');
 numclient | datecommande | montantht
-----------+--------------+-----------
         8 | 2021-10-17   |   2870.00
         9 | 2021-10-17   |   3000.00
         8 | 2021-11-16   |   3000.00
         9 | 2021-11-16   |   6450.00
         8 | 2021-12-16   |   5950.00
         9 | 2021-12-16   |  18500.00
        10 | 2021-12-16   |  10500.00
        11 | 2021-12-16   |  15817.50
(8 lignes)


/* Pour la semaine n°41, au 2021-10-17. */
/* Le CA est de 2870 + 3000 = 5700 */
/* Le mois d'octobre étant composé des semaines n°40, 41, 42 et 43, on suppose un CA mensuel de 5700*4 = 22 800. */

/* Pour la semaine n°46, au 2021-11-16. */
/* Le CA est de 3000 + 6450 = 9450  */
/* Le mois de novembre étant composé des semaines n°44, 45, 46 et 47, on suppose un CA mensuel de 9450*4 = 37 800. */

/* Pour la semaine n°50, au 2021-12-16. */
/* Le CA est de 5950 + 18500 + 10500 + 15817.50 = 50 767,50  */
/* Le mois de décembre étant composé des semaines n°48, 49, 50, 51 et 52, on suppose un CA mensuel de 50 767,50*5 = 253 837,50. */





/* CHIFFRE D'AFFAIRES TTC */

select numclient,datecommande,montantttc from commande where numclient in(select numclient from client where codeetiquette like'CH');
 numclient | datecommande | montantttc
-----------+--------------+------------
         8 | 2021-10-17   |    3444.00
         9 | 2021-10-17   |    3600.00
         8 | 2021-11-16   |    3600.00
         9 | 2021-11-16   |    7740.00
         8 | 2021-12-16   |    7140.00
         9 | 2021-12-16   |   22200.00
        10 | 2021-12-16   |   12600.00
        11 | 2021-12-16   |   18981.00
(8 lignes)


/* Pour la semaine n°41, au 2021-10-17. */
/* Le CA est de 3444 + 3600 = 7044 */
/* Le mois d'octobre étant composé des semaines n°40, 41, 42 et 43, on suppose un CA mensuel de 7044*4 = 28 176. */

/* Pour la semaine n°46, au 2021-11-16. */
/* Le CA est de 3600 + 7740 = 11 340  */
/* Le mois de novembre étant composé des semaines n°44, 45, 46 et 47, on suppose un CA mensuel de 11 340*4 = 45 360. */

/* Pour la semaine n°50, au 2021-12-16. */
/* Le CA est de 7140 + 22 200 + 12 600 + 18981 = 60 831  */
/* Le mois de décembre étant composé des semaines n°48, 49, 50, 51 et 52, on suppose un CA mensuel de 60 831*5 = 304 155. */



/*############################################################################################################### */

/*############################################################################################################### */

/* Question n°3 : */

/* Existe-t-il des clients qui n’ont jamais passé de commandes ? Existe-t-il des clients d’un pays entier qui
n’ont jamais passé de commandes ? */

select distinct(numclient) from commande order by numclient;
 numclient
-----------
         1
         2
         3
         4
         5
         8
         9
        10
        11
        12
        13
        16
        17
(13 lignes)

/* On voit ici que seulement 13 clients différents ont passé (au moins) une commande, alors qu'il y a au total 20 clients, il en manque donc 7. Les clients n'ayant pas passé commande sont les numclient n°6, 7, 14, 15, 18, 19, 20 */


/* Requête permettant de voir le nombre de clients */
select distinct(numclient) from client order by numclient;
 numclient
-----------
         1
         2
         3
         4
         5
         6
         7
         8
         9
        10
        11
        12
        13
        14
        15
        16
        17
        18
        19
        20
(20 lignes)



/*############################################################################################################### */

/*############################################################################################################### */

/* Question n°4 : */

/* Il semble que certaines commandes ne soient pas livrées totalement le phénomène est-il inquiétant ? */

 select * from detailcommande where quantitecommandee > quantitelivree ;
 numcommande | numarticle | quantitecommandee | quantitelivree
-------------+------------+-------------------+----------------
           1 |          5 |                15 |             10
           3 |          3 |                 8 |              0
           3 |          4 |                15 |              0
           3 |          5 |                18 |              0
           5 |         22 |                 7 |              5
          13 |          5 |                15 |             10
          23 |          5 |                15 |             10
(7 lignes)

/* On voit que sur les 84 commandes enregistrées, 7 d'entre elles n'ont pas été livrés correctement, ce qui est évidemment inquiétant. */


/*############################################################################################################### */
/* Groupe n°19 : Fournier Benjamin (TPC) & Hurdebourcq Paul (TPC)                                                 */
/*############################################################################################################### */
