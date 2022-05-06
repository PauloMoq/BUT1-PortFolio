//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

import java.util.ArrayList;

public class Tour extends Piece{

    /* Constructeur par défaut */
    public Tour(){
        super();
    }

    /* Constructeur par valeurs */
    public Tour(char couleur, Position pos){
        super(couleur, pos);
    }

    @Override
    public String getType() {
        return "tour";
    }

    /* renvoie tous les déplacements possibles de la tour */
    @Override
    public ArrayList<Position> getDeplacementPossible(Plateau jeu) {
        ArrayList<Position> deplaPossibles = new ArrayList<Position>();
        Position position = new Position(this.getPosition());

        // Droite 
        for (int i=1; i < 9; i++){
            if (position.getX() + i < 8 && position.getX() + i >= 0 ){
                Position posD = new Position(( position.getX() + i), (position.getY()));
                if (jeu.getCase(posD) != null && jeu.getCase(posD).getCouleur() == this.getCouleur()){
                    break;
                }
                if(jeu.getCase(posD) == null){
                    deplaPossibles.add(posD);
                }
                if(jeu.getCase(posD) != null && jeu.getCase(posD).getCouleur() != this.getCouleur()){
                    deplaPossibles.add(posD);
                    break;
                } 
            }   
        }

        // Gauche 
        for (int i=1; i < 9; i++){
            if (position.getX() - i < 8 && position.getX() - i >= 0 ){
                Position posG = new Position(( position.getX() - i), (position.getY()));
                if (jeu.getCase(posG) != null && jeu.getCase(posG).getCouleur() == this.getCouleur()){
                    break;
                }
                if(jeu.getCase(posG) == null){
                    deplaPossibles.add(posG);
                }
                if(jeu.getCase(posG) != null && jeu.getCase(posG).getCouleur() != this.getCouleur()){
                    deplaPossibles.add(posG);
                    break;
                } 
            }   
        }

        // Bas
        for (int i=1; i < 9; i++){
            if (position.getY() - i < 8 && position.getY() - i >= 0 ){
                Position posB = new Position(( position.getX()), (position.getY() - i));
                if (jeu.getCase(posB) != null && jeu.getCase(posB).getCouleur() == this.getCouleur()){
                    break;
                }
                if(jeu.getCase(posB) == null){
                    deplaPossibles.add(posB);
                }
                if(jeu.getCase(posB) != null && jeu.getCase(posB).getCouleur() != this.getCouleur()){
                    deplaPossibles.add(posB);
                    break;
                } 
            }   
        }

        // Haut
        for (int i=1; i < 9; i++){
            if (position.getY() + i < 8 && position.getY() + i >= 0 ){
                Position posH = new Position(( position.getX()), (position.getY() + i));
                if (jeu.getCase(posH) != null && jeu.getCase(posH).getCouleur() == this.getCouleur()){
                    break;
                }
                if(jeu.getCase(posH) == null){
                    deplaPossibles.add(posH);
                }
                if(jeu.getCase(posH) != null && jeu.getCase(posH).getCouleur() != this.getCouleur()){
                    deplaPossibles.add(posH);
                    break;
                } 
            }   
        }

        /* on renvoie le tableau contenant les déplacements disponibles de la tour */
        return deplaPossibles;
    } 
}

//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //