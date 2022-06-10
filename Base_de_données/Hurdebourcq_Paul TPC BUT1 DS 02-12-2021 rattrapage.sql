/* HURDEBOURCQ Paul TPC */
/* 02/12/2021 */


1)/*Création de la base de données.*/
postgres=# CREATE DATABASE employe_hurdebourcq 
WITH OWNER paulo ;
CREATE DATABASE



2)/*Création de relations dans la base de données (et remplissage).*/
CREATE TABLE service (num_service INTEGER PRIMARY KEY, nom_service VARCHAR(50));
CREATE TABLE employe (num_employe INTEGER PRIMARY KEY, nom VARCHAR(50), prenom VARCHAR(50), salaire INTEGER, num_service INTEGER REFERENCES service(num_service));
CREATE TABLE nature_conge (num_nature_conge INTEGER PRIMARY KEY, nom_nature_conge VARCHAR(100));
CREATE TABLE droit_conge(num_employe INTEGER REFERENCES employe(num_employe), num_nature_conge INTEGER REFERENCES nature_conge(num_nature_conge), nb_jour INTEGER, CONSTRAINT pk_droit_conge PRIMARY KEY(num_employe,num_nature_conge));
CREATE TABLE conge_pris (num_conge_pris INTEGER PRIMARY KEY, num_employe INTEGER REFERENCES employe(num_employe),  date_debut date, date_fin date, num_nature_conge INTEGER REFERENCES nature_conge(num_nature_conge));

INSERT INTO service VALUES (1, 'commercial'),(2, 'comptabilite'),(3, 'ressources_humaines'), (4, 'sav'); 
INSERT INTO employe VALUES (1, 'capitaine', 'dany', 10500, 1), (2, 'letrez', 'severine',9000,2), (3,'synave', 'rémi',3900, 3), (4, 'delepouille', 'samuel',6500,4),(5,'talon', 'bénédicte', 7500,1), (6,'fernandez', 'marguerite',9000, 2), (7,'sannoy', 'gauthier',7500,2),(8, 'deligniere', 'isabelle',10500,1);
INSERT INTO nature_conge VALUES (1, 'rtt'), (2,'maladie'), (3, 'recup'), (4, 'ete'), (5,'hiver'),(6, 'maternite'),(7,'deces');
INSERT INTO droit_conge VALUES (1, 1,120), (2,1,10), (3,1,100), (4,1,200), (1,2,10), (2,2,15),(3,2,20), (4,2,15), (1,3,10), (2,3,10), (3,3,10), (4,3,10), (1,4,100), (2,4,150), (3,4,100), (4,4,0); 
INSERT INTO conge_pris VALUES (1,1,'10/10/2018', '15/10/2018',1), (2,1,'20/11/2017', '15/10/2018',2), (3,1, '15/11/2017', '15/06/2018',3), (4,1,'12/12/2018', '18/12/2018',2);



3)/*Modification de la relation conge_pris, pour être sûr que la fin du congé est supérieur au début du congé.*/
employe_hurdebourcq=# ALTER TABLE conge_pris 
ADD CONSTRAINT check_date 
CHECK (date_fin > date_debut) ;
ALTER TABLE



4)/*Mise à jour du nombre de congés annuels pour l'employé "CAPITAINE", remplacer le 120 par 60.*/
employe_hurdebourcq=# UPDATE droit_conge 
SET nb_jour = 60 
WHERE num_employe = 1 
AND num_nature_conge = 1 ;
UPDATE 1



5)/*Affichage du nom et prénom des employés dont le nom se termine par un 'E' et le prénom commence par un 'D' et se termine par un 'Y'.*/
employe_hurdebourcq=# SELECT em.nom, em.prenom 
FROM employe 
AS em 
WHERE nom 
LIKE '%e' AND prenom LIKE 'd%y' ;

    nom    | prenom
-----------+--------
 capitaine | dany
(1 ligne)



6)/*Affichage du nom des employés qui ont un salaire supérieur au salaire moyen des autres employés.*/
employe_hurdebourcq=# SELECT emp.nom 
FROM employe 
AS emp
WHERE emp.salaire > (SELECT avg(salaire) FROM employe) ;

    nom
------------
 capitaine
 letrez
 fernandez
 deligniere
(4 lignes)

/*Je dois ici renommer la table employe dans un premier temps car j'ai besoin d'utiliser deux fois la colonne salaire.*/



7)/*Affichage du nom des employés par nom de service sauf le service commercial.*/
employe_hurdebourcq=# SELECT  nom, nom_service 
FROM employe 
INNER JOIN service 
ON employe.num_service = service.num_service 
WHERE nom_service 
NOT LIKE 'commercial' 
ORDER BY nom_service ;

     nom     |     nom_service
-------------+---------------------
 letrez      | comptabilite
 fernandez   | comptabilite
 sannoy      | comptabilite
 synave      | ressources_humaines
 delepouille | sav
(5 lignes)

/*Dans la question il est marqué "par nom de service", je comprends donc qu'il me faut trier le résultat par nom_service (avec order by), mais ce n'est pas nécessaire en soit.*/



8)/*Affichage de l'employe ayant le plus de congés disponible.*/
SELECT  emp.nom 
FROM  employe 
AS emp 
INNER JOIN droit_conge 
AS dro 
ON dro.num_employe = emp.num_employe 
WHERE dro.nb_jour = (SELECT max(nb_jour) FROM droit_conge) ;

     nom
-------------
 delepouille
(1 ligne)



9)/*Affichage du nombre total de congés déjà pris par les employés (nom et prénom) par type de congés (rtt, ete, recup, etc...) seulement pour le service 'commercial'.*/



10)/*Affichage des noms et prénoms des employés qui sont dans le service commercial ayant pris au moins une fois des congés en 2018.*/
SELECT emp.nom, emp.prenom 
FROM employe 
AS emp
INNER JOIN service 
AS ser 
ON ser.num_service = emp.num_service 
INNER JOIN conge_pris 
AS con 
ON con.num_employe = emp.num_employe 
WHERE nom_service 
LIKE 'commercial' 
AND date_debut >= '01/01/2018' ;

    nom    | prenom
-----------+--------
 capitaine | dany
 capitaine | dany
(2 lignes)



11)/*Affichage du nombre de congés pris par salariés (nom) mais seulement ceux qui dépassent 10.*/



12)/*Ajout d'un tuple concernant Madame Letrez.*/
INSERT into conge_pris 
VALUES  
(5,
(SELECT num_employe FROM employe WHERE nom LIKE 'letrez'),
'24/11/2021' ,
'28/11/2021' ,
(SELECT  num_nature_conge FROM nature_conge WHERE nom_nature_conge LIKE 'maladie') ) ;
INSERT 0 1



13)/*Invention d'une requête nécessitant l'utilisation d'un group by ET d'un having.*/
/*Affichage des employés avec un salaire inférieur à 9 000 euros avec des congés 'recup'.*/ 
