public class CouleurPieceException extends RuntimeException {
    
    // cons valeur
    public CouleurPieceException(char couleur){
        super("ERREUR : La couleur ["+couleur+"] de la piece est incorrecte");
    }
}
