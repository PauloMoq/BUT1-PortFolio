//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

import java.util.ArrayList;

public abstract class Pion extends Piece {

    /* Constructeur par défaut */
    public Pion(){
        super(); // appelle le constructeur par défaut de Piece
    }
    
    /* Constructeur par valeurs */
    public Pion(char couleur, Position pos){
        super(couleur, pos);
    }

    /* renvoie le type de la pièce */
    public abstract String getType();

    // à refaire par la suite dans PionB et PionN
    @Override
    public abstract ArrayList<Position> getDeplacementPossible(Plateau jeu);
}

//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //