public class ErreurCoordonneesException extends RuntimeException{

    //cons valeurs
    public ErreurCoordonneesException(int a, int b){
        super("ERREUR : Les coordonnees sont incorrectes (x : "+a+", y : "+b+")");
    }

    //cons texte
    public ErreurCoordonneesException(String chaine){
        super("ERREUR : La position : ["+chaine+"] est incorrecte");
    }

    //cons valeur
    public ErreurCoordonneesException(int a){
        super("ERREUR : La coordonnee : ["+a+"] est incorrecte");
    }

}