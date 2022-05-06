//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

import java.util.ArrayList;

abstract class Piece {
    /* Attributs */
    private char couleur;
    private Position position;
    
    /* Constructeur par défaut */
    public Piece(){
        this.couleur = 'B';
        this.position = new Position("A2");
        }

    /* Constructeur par copie */
    public Piece(Piece p){
        this.couleur = p.couleur;
        this.position = p.position;
    }

    /* Constructeur par valeurs (2 entiers) */
    // J'appelle mes paramètres ...1 pour mieux m'y retrouver
    public Piece(char couleur1, int x, int y){
        this.couleur = couleur1;
        this.position = new Position(x,y);
    }

    /* Constructeur par valeurs (Position) */
    public Piece(char couleur2, Position position2){
        this.couleur = couleur2;
        this.position = new Position(position2);
    }
    
    /* Constructeur par valeurs (Position avec chaine) */
    public Piece(char couleur3, String chaine){
        this.couleur = couleur3;
        this.position = new Position(chaine);
    }

    /* Getters */
    // Je précise P_ pour indiquer que la méthode provient de la classe Piece

    /* la méthode est abstraite, donc utilisable dans cette classe, mais à redéfinir dans les sous-classes */
    public abstract String getType();

    public char getCouleur(){
        return this.couleur;
    }

    public Position getPosition(){
        return this.position;
    }

    public int p_GetX(){
        return this.position.getX();
    }

    public int p_GetY(){
        return this.position.getY();
    }



    /* Setters */
    public void p_SetX(int abscisse){
        this.position.setX(abscisse);
    }

    public void p_setY(int ordonnee){
        this.position.setY(ordonnee);
    }

    public void setPosition(Position position){
        this.position = new Position(position);
    }

    public void setCouleur(char couleur){
        this.couleur = couleur;
    }

    /* Nom de type "RoB" pour roi blanc */
    public String getNomCourt(){
        return (""+this.getType().charAt(0)+this.getType().charAt(1)+this.couleur);
    }

    /* Nom de type "roi_B" pour roi blanc */
    public String getNomLong(){
        return (""+this.getType()+'_'+this.couleur);
    }

    /* Equals */
    public boolean equals(Object truc){
        if (truc instanceof Piece == false){
            return false;
            }
        Piece p = (Piece)truc;
        /* == c'est pour les types natifs (int, double, char) alors que equals c'est pour les objects */
        return (this.couleur == p.couleur && this.position.equals(p.position));
    }

    /* toString */
    public String toString(){
        /* ici j'ai du utiliser la méthode abstraite getType() à la place de self.type */
        if (this.couleur == 'B'){
            return (this.getType()+" blanc en "+this.position.toString());
            }
        else {
            return (this.getType()+" noir en "+this.position.toString());
            }
    }

    /* class asbtraite qui sera redéfinie par la suite */
    public abstract ArrayList<Position> getDeplacementPossible(Plateau jeu);

    /*   
      |x| L'attribut type a bien été supprimé de la classe 
    */
}

//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //