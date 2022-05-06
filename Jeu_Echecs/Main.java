//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //

public class Main {
    public static void main(String[] args) {
        Plateau plateau = new Plateau() ;
        System.out.println(plateau.toString());
        System.out.println(plateau.getPiecesBlanches().toString());
        System.out.println(plateau.getPiecesNoires().toString());
    }
}

// javac -cp . .\Piece.java
// si ça trouve pas la classe dans le dossier

// java -cp . Main
// pour lancer si ça galère après le javac

//     Hurdebourcq Paul BUT1 TPB     //
//       --R2.01 TD/TP_Echec--       //
//          03-04/2022 |S2|          //
//  - Utilisation non commerciale -  //