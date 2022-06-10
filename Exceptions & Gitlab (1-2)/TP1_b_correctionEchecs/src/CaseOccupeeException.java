public class CaseOccupeeException extends RuntimeException{

    // cons valeurs
    public CaseOccupeeException(Piece p){
        super("ERREUR : Impossible d'ajouter ["+p+"] sur une case occupee");
    }
}
