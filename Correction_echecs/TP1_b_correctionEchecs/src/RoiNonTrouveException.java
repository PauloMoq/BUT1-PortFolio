public class RoiNonTrouveException extends RuntimeException{

    // cons valeur
    public RoiNonTrouveException(char couleur){
        super("ERREUR : Le roi ["+couleur+"] est introuvable");
    }
}
