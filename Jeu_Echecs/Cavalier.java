//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

import java.util.ArrayList;

public class Cavalier extends Piece{

    /* Constructeur par défaut */
    public Cavalier(){
        super();
    }

    /* Constructeur par valeurs */
    public Cavalier(char couleur, Position pos){
        super(couleur, pos);
    }

    /* renvoie le type de la pièce */
    @Override
    public String getType() {
        return "cavalier";
    }

    /* renvoie tous les déplacements possibles du cavalier */
    @Override
    public ArrayList<Position> getDeplacementPossible(Plateau jeu) {
        ArrayList<Position> deplaPossibles = new ArrayList<Position>();
        Position position = new Position(this.getPosition());

        // Haut
        /* Haut et droite */
        if(position.getX() + 1 < 8 && position.getX() + 1 >= 0 && position.getY() + 2 < 8 && position.getY() + 2 >= 0){
            /* on vérifie que le déplacement à effectuer est bien contenu dans le plateau */

            Position posHD = new Position((position.getX() + 1), (position.getY() + 2));
            /* on crée une position à l'endroit où l'on veut se déplacer */

            if(jeu.getCase(posHD) == null || jeu.getCase(posHD).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posHD);
            }
            /* on peut déplacer le cavalier si la destination est libre ou si la pièce à manger est bien que la couleure adverse. */
        }

        /* Haut et gauche */
        if(position.getX() - 1 < 8 && position.getX() - 1 >= 0 && position.getY() + 2 < 8 && position.getY() + 2 >= 0){
            Position posHG = new Position((position.getX() - 1), (position.getY() + 2));
            if(jeu.getCase(posHG) == null || jeu.getCase(posHG).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posHG);
            }
        }  
        
        /* Haut et côté gauche */
        if(position.getX() - 2 < 8 && position.getX() - 2 >= 0 && position.getY() + 1 < 8 && position.getY() + 1 >= 0){
            Position posHCG = new Position((position.getX() - 2), (position.getY() + 1));
            if(jeu.getCase(posHCG) == null || jeu.getCase(posHCG).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posHCG);
            }
        } 

        /* Haut et côté droit */
        if(position.getX() + 2 < 8 && position.getX() + 2 >= 0 && position.getY() + 1 < 8 && position.getY() + 1 >= 0){
            Position posHCD = new Position((position.getX() + 2), (position.getY() + 1));
            if(jeu.getCase(posHCD) == null || jeu.getCase(posHCD).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posHCD);
            }
        } 



        // Bas
        /* Bas et droite */
        if(position.getX() + 1 < 8 && position.getX() + 1 >= 0 && position.getY() - 2 < 8 && position.getY() - 2 >= 0){
            Position posBD = new Position((position.getX() + 1), (position.getY() - 2));
            if(jeu.getCase(posBD) == null || jeu.getCase(posBD).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posBD);
            }
        } 


        /* Bas et gauche */
        if(position.getX() - 1 < 8 && position.getX() - 1 >= 0 && position.getY() - 2 < 8 && position.getY() - 2 >= 0){
            Position posBG = new Position((position.getX() - 1), (position.getY() - 2));
            if(jeu.getCase(posBG) == null || jeu.getCase(posBG).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posBG);
            }
        }

        /* Bas et côté gauche */
        if(position.getX() - 2 < 8 && position.getX() - 2 >= 0 && position.getY() - 1 < 8 && position.getY() - 1 >= 0){
            Position posBCG = new Position((position.getX() - 2), (position.getY() - 1));
            if(jeu.getCase(posBCG) == null || jeu.getCase(posBCG).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posBCG);
            }
        }

        /* Bas et côté droit */
        if(position.getX() + 2 < 8 && position.getX() + 2 >= 0 && position.getY() - 1 < 8 && position.getY() - 1 >= 0){
            Position posBCD = new Position((position.getX() + 2), (position.getY() - 1));
            if(jeu.getCase(posBCD) == null || jeu.getCase(posBCD).getCouleur() != this.getCouleur()){
                deplaPossibles.add(posBCD);
            }
        }

        /* on renvoie le tableau contenant les déplacements disponibles du cavalier */
        return deplaPossibles;
    }
}

//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //