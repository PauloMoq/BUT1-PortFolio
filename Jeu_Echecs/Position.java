//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

public class Position {
    /*Attributs*/
    private int x, y;

    /*Constructeur par défaut*/
    public Position(){
            this.x = 0;
            this.y = 0;
    }

    /*Constructeur par copie*/
    public Position(Position p){
        this.x = p.x;
        this.y = p.y;
    }  

    /*Constructeur par valeurs*/
    public Position(int a, int o){ //a : abscisse ; o : ordonnee
        if(a<0 | o<0 | a>7 | o>7){
            System.exit(-1);
            }
        
        else{
            this.x = a;
            this.y = o;
        }
    }

    /*Constructeur par chaîne de caractères*/
    public Position(String chaine){
        char lettre = chaine.charAt(0);
        int le_x = (int) lettre - 65; //askii
        int le_y = (int) chaine.charAt(1) - 48;
        if(le_x<0 | le_y<0 | le_x>7 | le_y>7){
            System.exit(-1);
            }
        this.x = le_x;
        this.y = le_y;
    }

    /*Getters*/
    public int getX(){ //public int ça renvoie un int gros génie
        return this.x;
    }

    public int getY(){
        return this.y;
    }

    /*Setters*/
    public void setX(int abscisse){ //Abscisse ou x
        this.x = abscisse;
    }

    public void setY(int ordonnee){ //Ordonnee ou y
        this.y = ordonnee;
    }

    /*Equals*/
    public boolean equals(Object truc){
        if (truc instanceof Position == false){
            return false;
            }
        Position p = (Position)truc;
        return (this.x == p.x && this.y == p.y); //Retourne True si et seulement si les deux conditions sont remplies
    }

    /*ToString*/
    public String toString(){
        String ligne = new String("ABCDEFGH");
        String res = new String();
        res = ligne.substring(this.x, this.x + 1) + this.y;
        return res;
    }
}

//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //