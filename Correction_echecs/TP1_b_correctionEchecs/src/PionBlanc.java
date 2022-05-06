import java.util.ArrayList;

class PionBlanc extends Pion{
    
    public PionBlanc(){
	super('B', new Position());
    }

    public PionBlanc(Position position){
	super('B', position);
    }
    

    public ArrayList<Position> getDeplacementPossible(Plateau pl)
    {
	ArrayList<Position> liste = new ArrayList<Position>();
	// Test s'il peut avancer d'une case
	if(this.getPosition().getY() != 7){ // Si le pion n'est pas arrivé au bout - Est ce vraiment éncessaire ? Car les pions se transforment en autre chose au bout du plateau.
	    if(pl.getCase(this.getPosition().getX(),this.getPosition().getY()+1)==null) // s'il n'y a rien devant lui, il peut avancer.
		liste.add(new Position(this.getPosition().getX(),this.getPosition().getY()+1));

	    // Test s'il peut avancer de deux cases
	    if(this.getPosition().getY() == 1 && liste.size()==1){ // le pion n'a pas encore bougé et qu'il n'y a pas de pièce devant lui donc que le test précédent est passé
		if(pl.getCase(this.getPosition().getX(),this.getPosition().getY()+2)==null)
		    liste.add(new Position(this.getPosition().getX(),this.getPosition().getY()+2));
	    }

	    // Test des prises
	    // On vérifie si on est sur un bord donc une seule prise à tester
	    if(this.getPosition().getX() == 0){ // le pion est à gauche
		Piece hd = pl.getCase(this.getPosition().getX()+1,this.getPosition().getY()+1);
		if(hd != null)
		    if(hd.getCouleur()!=this.getCouleur())
			liste.add(new Position(this.getPosition().getX()+1,this.getPosition().getY()+1));
	    }
	    else if(this.getPosition().getX() == 7){ // le pion est à droite
		Piece hg = pl.getCase(this.getPosition().getX()-1,this.getPosition().getY()+1);
		if(hg != null)
		    if(hg.getCouleur()!=this.getCouleur())
			liste.add(new Position(this.getPosition().getX()-1,this.getPosition().getY()+1));
	    }
	    else{ // le pion est "au centre"
		Piece hg = pl.getCase(this.getPosition().getX()-1,this.getPosition().getY()+1);
		Piece hd = pl.getCase(this.getPosition().getX()+1,this.getPosition().getY()+1);
		if(hg != null)
		    if(hg.getCouleur()!=this.getCouleur())
			liste.add(new Position(this.getPosition().getX()-1,this.getPosition().getY()+1));
		
		if(hd != null)
		    if(hd.getCouleur()!=this.getCouleur())
			liste.add(new Position(this.getPosition().getX()+1,this.getPosition().getY()+1));
	    }
	}
	return liste;
    }
    

}
