//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

import java.util.ArrayList;

public class Fou extends Piece{

    /* Constructeur par défaut */
    public Fou(){
        super();
    }

    /* Constructeur par valeurs */
    public Fou(char couleur, Position pos){
        super(couleur, pos);
    }

    @Override
    public String getType() {
        return "fou";
    }

    /* renvoie tous les déplacements possibles du fou */
    @Override
    public ArrayList<Position> getDeplacementPossible(Plateau jeu) {
        ArrayList<Position> deplaPossibles = new ArrayList<Position>();
        Position position = new Position(this.getPosition());

        // Diagonales haut
        /* Haut et droite */
        for (int i=1; i < 9; i++){
            if (position.getX() + i < 8 && position.getX() + i >= 0 && position.getY() + i >= 0 && position.getY() + i < 8){
                Position posHD = new Position((position.getX() + i ), (position.getY() + i ));
                if (jeu.getCase(posHD) != null && jeu.getCase(posHD).getCouleur() == this.getCouleur()){
                    break;
                }
                if(jeu.getCase(posHD) == null){
                    deplaPossibles.add(posHD);
                }
                if(jeu.getCase(posHD) != null && jeu.getCase(posHD).getCouleur() != this.getCouleur()){
                    deplaPossibles.add(posHD);
                    break;
                }
                
            }   
        }

        /* Haut et gauche */
        for (int i=1; i < 9; i++){
            if (position.getX() - i < 8 && position.getX() - i >= 0 && position.getY() + i >= 0 && position.getY() + i < 8){
                Position posHG = new Position(( position.getX() - i ),( position.getY() + i ));
                if(jeu.getCase(posHG) != null && jeu.getCase(posHG).getCouleur() == this.getCouleur()){
                    break;
                }
                if(jeu.getCase(posHG) == null){
                    deplaPossibles.add(posHG);
                }
                if (jeu.getCase(posHG) != null && jeu.getCase(posHG).getCouleur() != this.getCouleur()){
                    deplaPossibles.add(posHG);
                    break;
                }
                
            }
        }





        // Diagonales bas
        /* Bas et gauche */
        for (int i=1; i < 9; i++){
            if (position.getX() - i < 8 && position.getX() - i >= 0 && position.getY() - i >= 0 && position.getY() - i < 8){
                Position posBG = new Position(( position.getX() - i ),( position.getY() - i ));
                if(jeu.getCase(posBG) != null && jeu.getCase(posBG).getCouleur() == this.getCouleur()){
                    break;
                } 
                if(jeu.getCase(posBG) == null ){
                    deplaPossibles.add(posBG);
                }   
                if(jeu.getCase(posBG) != null && jeu.getCase(posBG).getCouleur() != this.getCouleur()){
                    deplaPossibles.add(posBG);
                    break;
                }
            }
        }

        /* Bas et droite */
        for (int i=1; i < 9; i++){
            if (position.getX() + i < 8 && position.getX() + i >= 0 && position.getY() - i >= 0 && position.getY() - i < 8){
                Position posBD = new Position(( position.getX() + i ),( position.getY() - i ));
                if(jeu.getCase(posBD) != null && jeu.getCase(posBD).getCouleur() == this.getCouleur()){
                    break;
                }
                if(jeu.getCase(posBD) == null){
                deplaPossibles.add(posBD);
                }
                if (jeu.getCase(posBD) != null && jeu.getCase(posBD).getCouleur() != this.getCouleur()){
                    deplaPossibles.add(posBD);
                    break;
                }
                
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