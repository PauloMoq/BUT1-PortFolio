//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

// Import
import java.util.ArrayList;

public class PionB extends Pion {
    
    // Constructeur par défaut
    public PionB(){
        super();
    }

    // Constructeur par valeurs
    public PionB(char c, Position p){
        super(c, p);
    }
 
    // Méthode abstraite redéfinie
    @Override
    public String getType(){
        return "pionB";
    }

    @Override
    public ArrayList<Position> getDeplacementPossible(Plateau jeu) {
        ArrayList<Position> DeplaPossibles = new ArrayList<Position>();
        Position position = new Position(this.getPosition());
        // Haut
        // Si je suis sur la ligne de base
        if(position.getY() == 1){
            Position posH1 = new Position(( position.getX()), (position.getY() + 1));
            Position posH2 = new Position(( position.getX()), (position.getY() + 2));

            // Si la case 1 est vide
            if(jeu.getCase(posH1) == null){
                DeplaPossibles.add(posH1);
            }    

            // Si la case 2 est vide
            if(jeu.getCase(posH2) == null){
                DeplaPossibles.add(posH2);
            }  
            
        }

        else{
            // Si j'ai déjà bougé
            // On regarde la prochaine case
            if (position.getY() + 1 < 8 && position.getY() + 1 >= 0){
                Position posH = new Position(( position.getX()),(position.getY() + 1));
                // Si la case est vide
                if(jeu.getCase(posH) == null){
                    DeplaPossibles.add(posH);
                }
            } 
        }

        // Haut et droite
        // Manger
        if (position.getX() + 1 < 8 && position.getX() + 1 >= 0 && position.getY() + 1 >= 0 && position.getY() + 1 < 8){
            Position posHD = new Position(( position.getX() + 1 ),( position.getY() + 1 ));
            // Si il y a une pièce blanche en haut à droite
            if(jeu.getCase(posHD) != null && jeu.getCase(posHD).getCouleur() != this.getCouleur()){
                DeplaPossibles.add(posHD);
            }
        }   
            
        // Haut et gauche
        // Manger
        if (position.getX() - 1 < 8 && position.getX() - 1 >= 0 && position.getY() + 1 >= 0 && position.getY() + 1 < 8){
            Position posHG = new Position(( position.getX() - 1 ),( position.getY() + 1 ));
            // Si il y a une pièce blanche en haut à gauche
            if (jeu.getCase(posHG) != null && jeu.getCase(posHG).getCouleur() != this.getCouleur()){
                DeplaPossibles.add(posHG);
            }   
        }

        return DeplaPossibles;
    }
}

//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //