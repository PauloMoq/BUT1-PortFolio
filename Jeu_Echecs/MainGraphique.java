//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

// ################################################### //
// Import

import MG2D.*;
import MG2D.geometrie.*;
import java.util.ArrayList;

// ################################################### //
// Class

/*
  L'algo est le suivant :
  0 - Créer la fenetre et le plateau 
  1 - Boucle infinie { 
  ~~ 2 - Effacer la fenetre puis afficher le plateau et les pièces 
  ~~ 3 - Boucle pour attendre la sélection d'une pièce
  ~~ 4 - Attendre le clic suivant
  ~~ 5 - Si le second clic est une case vide ou une pièce de la même couleur que la pièce sélectionnée, on ne fait rien et on recommence la boucle infinie 
  ~~..... Sinon, on appel la méthode déplacer avec la position du premier clic en premier parametre et la position du second clic en second parametre puis on recommence la boucle infinie
  }
*/

public class MainGraphique{

    // Méthode pour afficher la fenêtre
    public static void afficherFenetre(Fenetre fenetre, Plateau p){

	    // Création de la liste des pièces blanches
        ArrayList<Piece> listePieceB = p.getPiecesBlanches();

        // Création de la liste des pièces noires
        ArrayList<Piece> listePieceN = p.getPiecesNoires();

	    // Création d'une pièce qui prendra une valeur de listePieceB / listePieceN
        Piece pieceActuelle = listePieceB.get(0);

	    // Création d'un point nécessaire à la création des textures blanches
        Point pointPieceB = new Point(); 

        // Création d'un point nécessaire à la création des textures noires
        Point pointPieceN = new Point(); 

        // Création d'une texture nécessaire à la création des textures, le constructeur Texture() ne peut pas être utilisé, c'est pourquoi on utilise une texture quelconque à l'initialisation de cette texture
        Texture imgPieceB = new Texture("./images/pion_B.png", pointPieceB, 90, 90);

        // Création d'une texture nécessaire à la création des textures
        Texture imgPieceN = new Texture("./images/pion_N.png", pointPieceN, 90, 90);



	    // Création de la dalleNoire par défaut pour le plateau de la fenêtre, il est nécessaire de déclarer les dalles dans le main, pour pouvoir utiliser la méthode translater par la suite.
        Rectangle dalleNoire = new Rectangle();

        // Création de la dalleBlanche
        Rectangle dalleBlanche = new Rectangle();

        

        // Je dois effacer la fenêtre afin de la modifier
        fenetre.effacer();

	    // --- 
        // Création de la fenêtre ( initialisation )
        // => on crée les dalles de couleurs, les textures seront créées plus tard

        for(int i = 0; i <=800; i = i + 200){ 
            // Alternation entre les dalles noires et les dalles blanches sur les lignes pairs
            for(int j = 0; j <= 800; j = j + 200){

                // Dalles noires
                dalleNoire = new Rectangle(Couleur.GRIS_CLAIR, new Point(i, j), 100, 100, true);
                fenetre.ajouter(dalleNoire);

                // Dalles blanches
                dalleBlanche = new Rectangle(Couleur.BLANC, new Point(i - 100, j), 100, 100, true);
                fenetre.ajouter(dalleBlanche);

            } // For j
        } // For i

        for(int i = 100; i <=700; i = i + 200){ 
            // Alternation entre les dalles noires et les dalles blanches sur les lignes impairs
            for(int j = 100; j <= 700; j = j + 200){

                // Dalles noires
                dalleNoire = new Rectangle(Couleur.GRIS_CLAIR, new Point(i, j), 100, 100, true);
                fenetre.ajouter(dalleNoire);

                // Dalles blanches
                dalleBlanche = new Rectangle(Couleur.BLANC, new Point(i - 100, j), 100, 100, true);
                fenetre.ajouter(dalleBlanche);

            } // For j
        } // For i

        // --- Pièces Blanches --- //
        for(int i = 0; i < listePieceB.size(); i++){
            // Parcours de chaque pièce blanche
            pieceActuelle = listePieceB.get(i);

            // Si pieceActuelle est un pion
            if(pieceActuelle.getType().equals("pionB")){
            pointPieceB = new Point((pieceActuelle.getPosition().getX()*100), ((pieceActuelle.getPosition().getY()*100) + 10)); // Le + 10 sert à ajouter une "marge" ayant pour but que la texture ne soit pas collée au bord de la fenêtre -> choix esthétique
            imgPieceB = new Texture("./images/pion_B.png", pointPieceB, 90, 90); // L'image est de taille 90x90
            fenetre.ajouter(imgPieceB);

            } // If pion

            // Si pieceActuelle est une tour
            if(pieceActuelle.getType().equals("tour")){ 
            pointPieceB = new Point((pieceActuelle.getPosition().getX()*100), ((pieceActuelle.getPosition().getY()*100) + 10));
            imgPieceB = new Texture("./images/tour_B.png", pointPieceB, 90, 90);
            fenetre.ajouter(imgPieceB);

            } // If tour

            // Si pieceActuelle est un cavalier
            if(pieceActuelle.getType().equals("cavalier")){ 
            pointPieceB = new Point((pieceActuelle.getPosition().getX()*100), ((pieceActuelle.getPosition().getY()*100) + 10));
            imgPieceB = new Texture("./images/cavalier_B.png", pointPieceB, 90, 90);
            fenetre.ajouter(imgPieceB);

            } // If cavalier

            // Si pieceActuelle est un fou
            if(pieceActuelle.getType().equals("fou")){ 
            pointPieceB = new Point((pieceActuelle.getPosition().getX()*100), ((pieceActuelle.getPosition().getY()*100) + 10));
            imgPieceB = new Texture("./images/fou_B.png", pointPieceB, 90, 90);
            fenetre.ajouter(imgPieceB);

            } // If fou

            // Si pieceActuelle est une dame
            if(pieceActuelle.getType().equals("dame")){ 
            pointPieceB = new Point((pieceActuelle.getPosition().getX()*100), ((pieceActuelle.getPosition().getY()*100) + 10));
            imgPieceB = new Texture("./images/dame_B.png", pointPieceB, 90, 90);
            fenetre.ajouter(imgPieceB);

            } // If dame

            // Si pieceActuelle est un roi
            if(pieceActuelle.getType().equals("roi")){ 
            pointPieceB = new Point((pieceActuelle.getPosition().getX()*100), ((pieceActuelle.getPosition().getY()*100) + 10));
            imgPieceB = new Texture("./images/roi_B.png", pointPieceB, 90, 90);
            fenetre.ajouter(imgPieceB);

            } // If roi

        } // For chaque pièce blanche

        // --- Pièces Noires --- //
        for(int i = 0; i < listePieceN.size(); i++){ 
            // Parcours de chaque pièce noire
            pieceActuelle = listePieceN.get(i);

            // Si pieceActuelle est un pion
            if(pieceActuelle.getType().equals("pionN")){ 
            pointPieceN = new Point((pieceActuelle.getPosition().getX()*100), ((pieceActuelle.getPosition().getY()*100) + 10)); // Le + 10 sert à ajouter une "marge" ayant pour but que la texture ne soit pas collée au bord de la fenêtre -> choix esthétique
            imgPieceN = new Texture("./images/pion_N.png", pointPieceN, 90, 90); // L'image est de taille 90x90
            fenetre.ajouter(imgPieceN);

            } // If pion

            // Si pieceActuelle est une tour
            if(pieceActuelle.getType().equals("tour")){ 
            pointPieceN = new Point((pieceActuelle.getPosition().getX()*100), ((pieceActuelle.getPosition().getY()*100) + 10));
            imgPieceN = new Texture("./images/tour_N.png", pointPieceN, 90, 90);
            fenetre.ajouter(imgPieceN);

            } // If tour

            // Si pieceActuelle est un cavalier
            if(pieceActuelle.getType().equals("cavalier")){ 
            pointPieceN = new Point((pieceActuelle.getPosition().getX()*100), ((pieceActuelle.getPosition().getY()*100) + 10));
            imgPieceN = new Texture("./images/cavalier_N.png", pointPieceN, 90, 90);
            fenetre.ajouter(imgPieceN);

            } // If cavalier

            // Si pieceActuelle est un fou
            if(pieceActuelle.getType().equals("fou")){ 
            pointPieceN = new Point((pieceActuelle.getPosition().getX()*100), ((pieceActuelle.getPosition().getY()*100) + 10));
            imgPieceN = new Texture("./images/fou_N.png", pointPieceN, 90, 90);
            fenetre.ajouter(imgPieceN);

            } // If fou

            // Si pieceActuelle est une dame
            if(pieceActuelle.getType().equals("dame")){ 
            pointPieceN = new Point((pieceActuelle.getPosition().getX()*100), ((pieceActuelle.getPosition().getY()*100) + 10));
            imgPieceN = new Texture("./images/dame_N.png", pointPieceN, 90, 90);
            fenetre.ajouter(imgPieceN);

            } // If dame

            // Si pieceActuelle est un roi
            if(pieceActuelle.getType().equals("roi")){ 
            pointPieceN = new Point((pieceActuelle.getPosition().getX()*100), ((pieceActuelle.getPosition().getY()*100) + 10));
            imgPieceN = new Texture("./images/roi_N.png", pointPieceN, 90, 90);
            fenetre.ajouter(imgPieceN);

            } // If roi

        } // For chaque pièce noire

        // Rafraîchissement de la fenêtre
        fenetre.rafraichir();
    } // Méthode afficherFenetre

    // --- 
    // Main

    public static void main(String[] args){

        // --- 
        // Création des objets



        // --- Objets reliés à la création / à l'affichage du plateau --- //

        // Création du plateau non graphique ( renvoyé dans le terminal )
        Plateau plateau = new Plateau(); 

        // Création du plateau graphique ( fenêtre cliquable )
        Fenetre fenetre = new Fenetre("Jeu d'echecs - Java", 800, 800);

        // Création d'un compteur me permettant de renvoyer le nombre de tours de jeu -> le compteur est à 1 de base, afin de renvoyer tour 1 et non pas tour 0 au début.
        int compteurDepla = 1;



        // --- Objets reliés à l'exécution de l'algorithme --- //

        // Création de la souris 
        Souris souris = fenetre.getSouris();

        // Création d'une liste de stockage des cercles de déplacements
        ArrayList<Cercle> listCercle = new ArrayList<Cercle>(); 

        // Création d'un cercle de déplacement possible
        Cercle cercleDispo = new Cercle(); 

        // Création d'un point indiquant la position de la souris
        Point posSouris = new Point();

        // Création d'entiers représentant les valeurs x et y de posSouris
        int sourisX, sourisY;

        // Création d'une position représentant une case du plateau en fonction de la position de la souris
        Position posSourisFenetre = new Position();

        // Création de la position de départ d'une pièce qui se déplace
        Position depart = null;

        // Création de la position de destination d'une pièce qui s'est déplacée
        Position destination = new Position();

        // Création d'une liste contenant tous les déplacements possibles d'une pièce
        ArrayList<Position> listeDeplaPossibles = new ArrayList<Position>();

        // Création d'entiers représentants le x et le y d'un déplacement possible
        int deplaPossX, deplaPossY;



        // --- Objets reliés aux règles du jeu --- //

        // Création de booléens servant à repérer les tours de jeu
        boolean tourJoueur1 = true;
        boolean tourJoueur2 = false;

        // Création d'un booléen servant à bloquer l'algorithme dans le cas où le joueur choisit une pièce ne lui appartenant pas.
        boolean bonneCouleur = true;

        afficherFenetre(fenetre, plateau);

        // ################################################### //
        // Début du programme

        while(true){

            // ---
            // Exceptions

            try{
                Thread.sleep(10); // Temps de repos au début
            } // Try sleep

            catch(InterruptedException e){
                System.out.println(" [!] Exception levée [!] "+"\n "+e.getMessage());
            } // Catch InterruptedException

            // ################################################### //
            // Joueur 1 ( blancs )

            // Premier clic
            // Attente jusqu'à sélection d'une pièce
            if (souris.getClicGauche() == true){

                // Je remets le booléen à true -> si l'un des joueurs choisit une pièce ne lui appartenant pas, on l'oblige à choisir une pièce lui appartenant ( sans cette mesure, le programme plante dès lors que le joueur agit de la sorte )
                bonneCouleur = true;

                
                if (tourJoueur1 == true && tourJoueur2 == false){
                    System.out.println("\n [TOUR DE JEU "+compteurDepla+"]"+" \n --C'est le tour du joueur 1 (blancs) !-- \n"+" \n  |?| Roi blanc en echec (true = vrai, false = faux) : "+plateau.estEchec('B'));
                } // Affichage joueur 1

                if (tourJoueur1 == false && tourJoueur2 == true){
                    System.out.println("\n [TOUR DE JEU "+compteurDepla+"]"+" \n --C'est le tour du joueur 2 (noirs) !-- \n"+" \n  |?| Roi noir en echec (true = vrai, false = faux) : "+plateau.estEchec('N'));
                } // Affichage joueur 2

                if (tourJoueur1 == true && tourJoueur2 == false){
  
                    // ---
                    // Cercles de déplacement possible

                    // Suppression des anciens cercles de déplacement possible
                    // Sinon, si le joueur change de pièce à bouger, les déplacements de l'ancienne pièce seront toujours présents
                    for (int j = 0; j < listCercle.size(); j++){
                        fenetre.supprimer(listCercle.get(j));
                    }

                    posSouris = souris.getPosition();

                    sourisX = posSouris.getX(); 
                    sourisY = posSouris.getY(); 

                    // Nous allons utiliser les x/100 et y/100 de la position de la souris afin de déterminer une position dans le plateau.
                    posSourisFenetre = new Position((sourisX/100), (sourisY/100));

                    // Si la case choisie est une case contenant une pièce appartenant au joueur, alors nous avons la position de départ
                    if (plateau.getCase(posSourisFenetre) != null && plateau.getCase(posSourisFenetre).getCouleur() == 'B'){

                            depart = new Position(posSourisFenetre);
                            System.out.println(" \n [Choisissez une destination ou changez de piece] =>\n");

                            listeDeplaPossibles = plateau.getCase(posSourisFenetre).getDeplacementPossible(plateau);

                            for (int i = 0; i < listeDeplaPossibles.size(); i++){
                                if (listeDeplaPossibles.get(i) != null){

                                    deplaPossX = listeDeplaPossibles.get(i).getX();
                                    deplaPossY = listeDeplaPossibles.get(i).getY();

                                    sourisX = (deplaPossX * 100) + 50;
                                    sourisY = (deplaPossY * 100) + 50;

                                    cercleDispo = new Cercle(Couleur.GRIS_FONCE, new Point(sourisX, sourisY), 15, true);
                                    listCercle.add(cercleDispo);
                                    fenetre.ajouter(cercleDispo);

                                } // If il existe bien un déplacement possible

                            } // For chaque déplacement possible

                            // Ajout des cercles à la fenêtre
                            fenetre.rafraichir();
                        
                    } // If les cercles

                    else { // If la pièce choisie n'appartient pas au joueur 1 -> pièce noire
                        if (depart == null){
                            bonneCouleur = false;
                        }
                    }

                    // Second clic
                    // Attente jusqu'à sélection d'une destination vide ou pièce adverse à manger
                    if (plateau.getCase(posSourisFenetre) == null || plateau.getCase(posSourisFenetre).getCouleur() == 'N' && bonneCouleur == true){

                            for (int i = 0; i < listeDeplaPossibles.size(); i++){
                                destination = new Position(listeDeplaPossibles.get(i));

                                // Déplacement seulement si la destination est une case vide
                                if (posSourisFenetre.equals(destination) && plateau.getCase(posSourisFenetre) == null){
                                    plateau.deplacer(depart, destination);
                                    System.out.println(" \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
                                    compteurDepla = compteurDepla + 1;
                                    tourJoueur1 = false;
                                    tourJoueur2 = true;

                                } // If si on trouve bien le déplacement à effectuer sur une case vide

                                // Déplacement seulement si la destination est une pièce adverse
                                if (posSourisFenetre.equals(destination) && plateau.getCase(posSourisFenetre).getCouleur() == 'N'){

                                    if (plateau.getCase(posSourisFenetre).getType() == "roi"){
                                        System.out.println("\n |!| Impossible de manger le roi |!|\n"+" [Choisissez un autre deplacement] \n");
                                        break;
                                    }

                                    // On peut donc déplacer notre pièce
                                    plateau.deplacer(depart, destination);
                                    System.out.println(" \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
                                    compteurDepla = compteurDepla + 1;
                                    tourJoueur1 = false;
                                    tourJoueur2 = true;

                                } // If si on trouve bien le déplacement à effectuer sur une pièce adverse

                            } // For chaque déplacement possible de la pièce de départ

                            // J'affiche la fenêtre après que j'ai cliqué pour la seconde fois
                            afficherFenetre(fenetre, plateau);
                            depart = null;
                            
                    } // If destination vide ou pièce adverse

                } // If tour du joueur 1

                // ################################################### //
                // Joueur 2 ( noirs )

                if (tourJoueur2 == true && tourJoueur1 == false){

                    // ---
                    // Cercles de déplacement possible

                    // Suppression des anciens cercles de déplacement possible
                    // Sinon, si le joueur change de pièce à bouger, les déplacements de l'ancienne pièce seront toujours présents
                    for (int j = 0; j < listCercle.size(); j++){
                        fenetre.supprimer(listCercle.get(j));
                    }

                    posSouris = souris.getPosition();

                    sourisX = posSouris.getX(); 
                    sourisY = posSouris.getY(); 

                    // Nous allons utiliser les x/100 et y/100 de la position de la souris afin de déterminer une position dans le plateau.
                    posSourisFenetre = new Position((sourisX/100), (sourisY/100));

                    // Si la case choisie est une case contenant une pièce appartenant au joueur, alors nous avons la position de départ
                    if (plateau.getCase(posSourisFenetre) != null && plateau.getCase(posSourisFenetre).getCouleur() == 'N'){

                            depart = new Position(posSourisFenetre);
                            System.out.println(" \n [Choisissez une destination ou changez de piece] =>\n");

                            listeDeplaPossibles = plateau.getCase(posSourisFenetre).getDeplacementPossible(plateau);

                            for (int i = 0; i < listeDeplaPossibles.size(); i++){
                                if (listeDeplaPossibles.get(i) != null){

                                    deplaPossX = listeDeplaPossibles.get(i).getX();
                                    deplaPossY = listeDeplaPossibles.get(i).getY();

                                    sourisX = (deplaPossX * 100) + 50;
                                    sourisY = (deplaPossY * 100) + 50;

                                    cercleDispo = new Cercle(Couleur.GRIS_FONCE, new Point(sourisX, sourisY), 15, true);
                                    listCercle.add(cercleDispo);
                                    fenetre.ajouter(cercleDispo);

                                } // If il existe bien un déplacement possible

                            } // For chaque déplacement possible

                            // Ajout des cercles à la fenêtre
                            fenetre.rafraichir();
                        
                    } // If les cercles

                    else { // If la pièce choisie n'appartient pas au joueur 2 -> pièce blanche
                        if (depart == null){
                            bonneCouleur = false;
                        }
                    }

                    // Second clic
                    // Attente jusqu'à sélection d'une destination vide ou pièce adverse à manger
                    if (plateau.getCase(posSourisFenetre) == null || plateau.getCase(posSourisFenetre).getCouleur() == 'B' && bonneCouleur == true){

                            for (int i = 0; i < listeDeplaPossibles.size(); i++){
                                destination = new Position(listeDeplaPossibles.get(i));

                                // Déplacement seulement si la destination est une case vide
                                if (posSourisFenetre.equals(destination) && plateau.getCase(posSourisFenetre) == null){
                                    System.out.println(" \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
                                    plateau.deplacer(depart, destination);
                                    compteurDepla = compteurDepla + 1;
                                    tourJoueur1 = true;
                                    tourJoueur2 = false;

                                } // If si on trouve bien le déplacement à effectuer sur une case vide

                                // Déplacement seulement si la destination est une pièce adverse
                                if (posSourisFenetre.equals(destination) && plateau.getCase(posSourisFenetre).getCouleur() == 'B'){

                                    if (plateau.getCase(posSourisFenetre).getType() == "roi"){
                                        System.out.println("\n |!| Impossible de manger le roi |!|\n"+" [Choisissez un autre deplacement] \n");
                                        break;
                                    }

                                    // On peut donc déplacer notre pièce
                                    plateau.deplacer(depart, destination);
                                    System.out.println(" \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
                                    compteurDepla = compteurDepla + 1;
                                    tourJoueur1 = true;
                                    tourJoueur2 = false;

                                } // If si on trouve bien le déplacement à effectuer sur une pièce adverse

                            } // For chaque déplacement possible de la pièce de départ

                            // J'affiche la fenêtre après que j'ai cliqué pour la seconde fois
                            afficherFenetre(fenetre, plateau);
                            depart = null;
                    
                    } // If destination vide ou pièce adverse
                
                } // If tour du joueur 2

            } // If clic gauche

        } // While ( true )

    } // Main
} // Class

//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //