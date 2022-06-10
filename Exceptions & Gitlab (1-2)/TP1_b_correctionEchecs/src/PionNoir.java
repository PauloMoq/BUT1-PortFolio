import java.util.ArrayList;

class PionNoir extends Pion{
    
    public PionNoir(){
	super('N', new Position());
    }

    public PionNoir(Position position){
	super('N', position);
    }
    

    public ArrayList<Position> getDeplacementPossible(Plateau pl)
    {
	ArrayList<Position> liste = new ArrayList<Position>();
	// Test s'il peut avancer d'une case
	if(this.getPosition().getY() != 0){ // Si le pion n'est pas arrivé au bout - Est ce vraiment éncessaire ? Car les pions se transforment en autre chose au bout du plateau.
	    if(pl.getCase(this.getPosition().getX(),this.getPosition().getY()-1)==null) // s'il n'y a rien devant lui, il peut avancer.
		liste.add(new Position(this.getPosition().getX(),this.getPosition().getY()-1));

	    // Test s'il peut avancer de deux cases
	    if(this.getPosition().getY() == 6 && liste.size()==1){ // le pion n'a pas encore bougé et qu'il n'y a pas de pièce devant lui donc que le test précédent est passé
		if(pl.getCase(this.getPosition().getX(),this.getPosition().getY()-2)==null)
		    liste.add(new Position(this.getPosition().getX(),this.getPosition().getY()-2));
	    }

	    // Test des prises
	    // On vérifie si on est sur un bord donc une seule prise à tester
	    if(this.getPosition().getX() == 0){ // le pion est à gauche
		Piece bd = pl.getCase(this.getPosition().getX()+1,this.getPosition().getY()-1);
		if(bd != null)
		    if(bd.getCouleur()!=this.getCouleur())
			liste.add(new Position(this.getPosition().getX()+1,this.getPosition().getY()-1));
	    }
	    else if(this.getPosition().getX() == 7){ // le pion est à droite
		Piece bg = pl.getCase(this.getPosition().getX()-1,this.getPosition().getY()-1);
		if(bg != null)
		    if(bg.getCouleur()!=this.getCouleur())
			liste.add(new Position(this.getPosition().getX()-1,this.getPosition().getY()-1));
	    }
	    else{ // le pion est "au centre"
		Piece bg = pl.getCase(this.getPosition().getX()-1,this.getPosition().getY()-1);
		Piece bd = pl.getCase(this.getPosition().getX()+1,this.getPosition().getY()-1);
		if(bg != null)
		    if(bg.getCouleur()!=this.getCouleur())
			liste.add(new Position(this.getPosition().getX()-1,this.getPosition().getY()-1));
		
		if(bd != null)
		    if(bd.getCouleur()!=this.getCouleur())
			liste.add(new Position(this.getPosition().getX()+1,this.getPosition().getY()-1));
	    }
	}
	return liste;
    }
    

}
