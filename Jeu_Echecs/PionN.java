//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

// Import
import java.util.ArrayList;

public class PionN extends Pion {
    
    // Constructeur par défaut
    public PionN(){
        super();
    }

    // Constructeur par valeurs
    public PionN(char c, Position p){
        super(c, p);
    }

    // Méthode abstraite redéfinie
    @Override
    public String getType(){
        return "pionN";
    }

    @Override
    public ArrayList<Position> getDeplacementPossible(Plateau jeu) {
        ArrayList<Position> DeplaPossibles = new ArrayList<Position>();
        Position position = new Position(this.getPosition());
        // Bas
        // Si je suis sur la ligne de base
        if(position.getY() == 6){
            Position posB1 = new Position(( position.getX()),(position.getY() - 1));
            Position posB2 = new Position(( position.getX()),(position.getY() - 2));
        
            // Si la case 1 est vide
            if(jeu.getCase(posB1) == null){
                DeplaPossibles.add(posB1);
            }

            // Si la case 2 est vide
            if(jeu.getCase(posB2) == null){
                DeplaPossibles.add(posB2);
            } 
        }
        
        else{
            // Si j'ai déjà bougé
            // On regarde la prochaine case
            if (position.getY() - 1 < 8 && position.getY() - 1 >= 0){
                Position posH = new Position(( position.getX()),(position.getY() - 1));
                // Si la case est vide
                if(jeu.getCase(posH) == null){
                        DeplaPossibles.add(posH);
                }
            } 
        }

        // Bas et droite
        // Manger
        if (position.getX() + 1 < 8 && position.getX() + 1 >= 0 && position.getY() - 1 >= 0 && position.getY() - 1 < 8){
            Position posBD = new Position(( position.getX() + 1 ),( position.getY() - 1 ));

            // Si il y a une pièce blanche en bas à droite
            if(jeu.getCase(posBD) != null && jeu.getCase(posBD).getCouleur() != this.getCouleur()){
                DeplaPossibles.add(posBD);
            }
        }   
            
        // Bas et gauche
        // Manger
        if (position.getX() - 1 < 8 && position.getX() - 1 >= 0 && position.getY() - 1 >= 0 && position.getY() - 1 < 8){
            Position posBG = new Position(( position.getX() - 1 ),( position.getY() - 1 ));

            // Si il y a une pièce blanche en bas à gauche
            if (jeu.getCase(posBG) != null && jeu.getCase(posBG).getCouleur() != this.getCouleur()){
                DeplaPossibles.add(posBG);
            }   
        }
        return DeplaPossibles;
    }
}

//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //