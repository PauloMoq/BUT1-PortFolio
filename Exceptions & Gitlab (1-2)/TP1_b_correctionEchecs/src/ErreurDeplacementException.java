public class ErreurDeplacementException extends RuntimeException{
    
    // cons valeur
    public ErreurDeplacementException(Position from, Position to){
        super("ERREUR : Impossible de se deplacer de ["+from+"] vers ["+to+"]");
    }
}
