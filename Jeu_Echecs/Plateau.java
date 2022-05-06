//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

import java.util.ArrayList;

class Plateau {
    /*Attributs*/
    private ArrayList<Piece> plateau = new ArrayList<Piece>();

    /*Constructeur par défaut*/
    public Plateau(){

        /*Pieces blanches*/
        this.plateau.add(new Tour('B', new Position(0, 0)));
        this.plateau.add(new Cavalier('B', new Position(1, 0)));
        this.plateau.add(new Fou('B', new Position(2, 0)));
        this.plateau.add(new Dame('B', new Position(3, 0)));
        this.plateau.add(new Roi('B', new Position(4, 0)));
        this.plateau.add(new Fou('B', new Position(5, 0)));
        this.plateau.add(new Cavalier('B', new Position(6, 0)));
        this.plateau.add(new Tour('B', new Position(7, 0)));

        /*Pions blancs*/
        for (int i = 0; i<8; i++){
            this.plateau.add(new PionB('B', new Position(i, 1)));
        }

        /*Pieces noires*/
        this.plateau.add(new Tour('N', new Position(0, 7)));
        this.plateau.add(new Cavalier('N', new Position(1, 7)));
        this.plateau.add(new Fou('N', new Position(2, 7)));
        this.plateau.add(new Dame('N', new Position(3, 7)));
        this.plateau.add(new Roi('N', new Position(4, 7)));
        this.plateau.add(new Fou('N', new Position(5, 7)));
        this.plateau.add(new Cavalier('N', new Position(6, 7)));
        this.plateau.add(new Tour('N', new Position(7, 7)));

        /*Pions noirs*/
        for (int i = 0; i<8; i++){
            this.plateau.add(new PionN('N', new Position(i, 6)));
        }   
    }

    /*GetCase deux entiers*/
    public Piece getCase(int x, int y){
        for (Piece p : this.plateau){ /*parcours du plateau*/
            if (p.p_GetX() == x && p.p_GetY() == y){
                return p;
            }
        }
        return null;
    }

    /*GetCase Position*/
    public Piece getCase(Position pos){
        for (Piece p : this.plateau){
            if (p.getPosition().equals(pos)){
                return p;
            }
        }
        return null;
    }

    /*GetCase chaine de caractères*/
    public Piece getCase(String chaine){
        for (Piece p : this.plateau){
            if (p.getPosition().equals(new Position(chaine))){
                return p;
            }
        }
        return null;
    }

    /*toString*/
    public String toString(){
        String affichage = new String(" |---|---|---|---|---|---|---|---|\n");
        for (int i = 7; i >= 0; i --){
            affichage += String.valueOf(i) + "|";
            for (int j = 0; j <= 7; j ++){
                if (getCase(j, i) == null){
                    affichage += "   |";
                }
                else{
                    affichage += getCase(j, i).getNomCourt() + "|";
                }
            }
            affichage = affichage + String.valueOf(i) + "\n |---|---|---|---|---|---|---|---|\n";
        }
        affichage = affichage + "   A   B   C   D   E   F   G   H   \n";
        return affichage;
    }

    /*Toutes les pieces blanches*/
    public ArrayList<Piece> getPiecesBlanches(){
        ArrayList<Piece> res = new ArrayList<Piece>();
        for (int i = 0; i < plateau.size(); i++){
            if (plateau.get(i).getCouleur() == 'B'){
                res.add(plateau.get(i));
            }
        }
        return res;
    }

    /*Toutes les pieces noires*/
    public ArrayList<Piece> getPiecesNoires(){
        ArrayList<Piece> res = new ArrayList<Piece>();
        for (int i = 0; i < plateau.size(); i++){
            if (plateau.get(i).getCouleur() == 'N'){
                res.add(plateau.get(i));
            }
        }
        return res;
    }

    // Utile pour la méthode boolean deplacer
    public void remove(Piece p){
        this.plateau.remove(p);
    }

    // Utile pour la méthode boolean deplacer
    public void add(Piece p){
        this.plateau.add(p);
    }

    /* Deplacement de la pièce */
    public boolean deplacer(Position from, Position to){
        Piece pieceFrom = this.getCase(from); // On récupère le type de la position from
        Piece pieceDestination = this.getCase(to); // On 
        ArrayList<Position> deplaPossibles = pieceFrom.getDeplacementPossible(this); // On récupère les déplacements possibles de la pièce de position from
        for(int i = 0; i < deplaPossibles.size(); i++){ // On parcourt cette liste
            if(deplaPossibles.get(i).equals(to)){ // Si un déplacement possible correspond à ma destination to
                if (pieceDestination != null){
                    this.remove(pieceDestination); // on enlève du plateau la pièce mangée (si il y en a une)
                }
                pieceFrom.setPosition(to); // On affecte les nouvelles coordonnées à la pièce from
                return true; // Renvoi de true
            }
        }
        return false; // Renvoi de false
    }

    public Position getRoi(char couleur){
        for (int i = 0; i < plateau.size(); i++){
            if (plateau.get(i).getCouleur() == couleur && plateau.get(i).getType() == "roi"){
                return plateau.get(i).getPosition();
            }
        }
        return null;
    }

    public boolean estEchec(char couleur){

        Position posRoi = getRoi(couleur);
        ArrayList<Piece> piecesAdverses = new ArrayList<Piece>();
        boolean echec = false;


        if (couleur == 'N'){
            piecesAdverses = getPiecesBlanches();
        }

        else {
            piecesAdverses = getPiecesNoires();
        }

        ArrayList<Position> deplaPossibles = new ArrayList<Position>();

        for (int i = 0; i < piecesAdverses.size(); i++) {
            deplaPossibles = new ArrayList<Position>(piecesAdverses.get(i).getDeplacementPossible(this));
            for (int j = 0; j < deplaPossibles.size(); j++) {
                if (deplaPossibles.get(j).equals(posRoi)){
                    echec = true;
                    break;
                } 
            }
        }
        
        return echec;
    }
}

//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //