public class Carre {
    public static void main(String args []) {

        try {
            int i = Integer.parseInt(args[0]);
            int carre = i * i;
            System.out.println("i x i = " + carre);
        } 
        
        catch (ArrayIndexOutOfBoundsException e1) {
            System.out.println("ERREUR : aucun parametre (args)");
        } 
        
        catch (NumberFormatException e2) {
            System.out.println("ERREUR : le parametre doit etre un entier (args)");
        }

    
    } // Main
} // Carre

/*
ex 1 :
Trouvez les entrées qui provoquent des exceptions. Quelle est la classe de ces exceptions ?
(Trouvez en deux !)

 => Si il n'y a pas d'argument OU un argument ayant un type autre que int.
*/

// javac Carre.java
// java Carre 
// java Carre 6
// java Carre ababou