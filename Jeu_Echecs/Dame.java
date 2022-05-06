//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

import java.util.ArrayList;

public class Dame extends Piece{

    /* Constructeur par défaut */
    public Dame(){
        super();
    }

    /* Constructeur par valeurs */
    public Dame(char couleur, Position pos){
        super(couleur, pos);
    }

    @Override
    public String getType() {
        return "dame";
    }

    /* renvoie tous les déplacements possibles de la dame */
    @Override
    public ArrayList<Position> getDeplacementPossible(Plateau jeu) {
        ArrayList<Position> deplaPossibles = new ArrayList<Position>();
        Position position = new Position(this.getPosition());

        // /!\ Fou /!\

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


        // /!\ Tour /!\

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

        /* on renvoie le tableau contenant les déplacements disponibles du fou */
        return deplaPossibles;
    }
}

//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //