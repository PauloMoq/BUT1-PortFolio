//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

import java.util.ArrayList;

public class Roi extends Piece{

    /* Constructeur par défaut */
    public Roi(){
        super();
    }

    /* Constructeur par valeurs */
    public Roi(char couleur, Position pos){
        super(couleur, pos);
    }

    @Override
    public String getType() {
        return "roi";
    }

    /* renvoie tous les déplacements possibles de le roi */
    @Override
    public ArrayList<Position> getDeplacementPossible(Plateau jeu) {
        ArrayList<Position> deplaPossibles = new ArrayList<Position>();
        Position position = new Position(this.getPosition());

        // /!\ Fou /!\

        // Diagonales haut
        /* Haut et droite */
        if (position.getX() + 1 < 8 && position.getX() + 1 >= 0 && position.getY() + 1 >= 0 && position.getY() + 1 < 8){
            Position posHD = new Position(( position.getX() + 1 ),( position.getY() + 1 ));
            if(jeu.getCase(posHD) == null){
                deplaPossibles.add(posHD);
            }
            if(jeu.getCase(posHD) != null && jeu.getCase(posHD).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posHD);
            }
        }   
        

        /* Haut et gauche */
        if (position.getX() - 1 < 8 && position.getX() - 1 >= 0 && position.getY() + 1 >= 0 && position.getY() + 1 < 8){
            Position posHG = new Position(( position.getX() - 1 ),( position.getY() + 1 ));
            if(jeu.getCase(posHG) == null){
                deplaPossibles.add(posHG);
            }
            if (jeu.getCase(posHG) != null && jeu.getCase(posHG).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posHG);
            }
        }





        // Diagonales bas
        /* Bas et gauche */
        if (position.getX() - 1 < 8 && position.getX() - 1 >= 0 && position.getY() - 1 >= 0 && position.getY() - 1 < 8){
            Position posBG = new Position(( position.getX() - 1 ),( position.getY() - 1 ));
            if(jeu.getCase(posBG) == null ){
                deplaPossibles.add(posBG);
            }   
            if(jeu.getCase(posBG) != null && jeu.getCase(posBG).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posBG);
            }
        }

        /* Bas et droite */
        if (position.getX() + 1 < 8 && position.getX() + 1 >= 0 && position.getY() - 1 >= 0 && position.getY() - 1 < 8){
            Position posBD = new Position(( position.getX() + 1 ),( position.getY() - 1 ));
            if(jeu.getCase(posBD) == null){
            deplaPossibles.add(posBD);
            }
            if (jeu.getCase(posBD) != null && jeu.getCase(posBD).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posBD);
            }
        }


        // /!\ Tour /!\

        // Droite 
        if (position.getX() + 1 >= 0 && position.getX() + 1 < 8){
            Position posD = new Position(( position.getX() + 1),( position.getY() ));
            if(jeu.getCase(posD) == null){
            deplaPossibles.add(posD);
            }
            if (jeu.getCase(posD) != null && jeu.getCase(posD).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posD);
            }

        }

        // Gauche 
        if (position.getX() - 1 >= 0 && position.getX() - 1 < 8){
            Position posG = new Position(position.getX() - 1,position.getY());
            if(jeu.getCase(posG) == null ){
                deplaPossibles.add(posG);
            }   
            if(jeu.getCase(posG) != null && jeu.getCase(posG).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posG);
          
            }
        }

        // Bas
        if (position.getY() - 1 < 8 && position.getY() - 1 >= 0 ){
            Position posB = new Position(( position.getX()),(position.getY() - 1));
            if(jeu.getCase(posB) == null){
                deplaPossibles.add(posB);
            }
            if (jeu.getCase(posB) != null &&jeu.getCase(posB).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posB);
            }

        }

        // Haut
        if (position.getY() + 1 < 8 && position.getY() + 1 >= 0){
            Position posH = new Position(( position.getX()), (position.getY() + 1));
            if(jeu.getCase(posH) == null){
                deplaPossibles.add(posH);
            }
            if(jeu.getCase(posH) != null && jeu.getCase(posH).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posH);
            }
        }

        /* on renvoie le tableau contenant les déplacements disponibles du fou */
        return deplaPossibles;
    }  
}

//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //