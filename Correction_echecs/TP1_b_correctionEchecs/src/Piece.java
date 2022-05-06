import java.util.ArrayList;

abstract class Piece{
    private char couleur;
    private Position position;
    

    public Piece(){
	this.position = new Position(0,0);
	this.couleur = 'B';
    }

    
    public Piece(char couleur, Position position) throws CouleurPieceException{
	if(!this.verificationCouleur(couleur)){
	    throw new CouleurPieceException(couleur);
	}
	this.position = new Position(position);
	this.couleur = couleur;
    }

    public Piece(char couleur, int x, int y){
	this(couleur, new Position(x,y));
    }

    public Piece(char couleur, String position){
	this(couleur, new Position(position));
    }

    
    public Piece(Piece p){
	this.position = new Position(p.position);
    }


    private boolean verificationCouleur(char c){
	return (c == 'B' || c == 'N');
    }


    
    public char getCouleur(){
	return this.couleur;
    }

    public void setCouleur(char couleur) throws CouleurPieceException{
	if(this.verificationCouleur(couleur)){
	    this.couleur = couleur;
	}else{
	    throw new CouleurPieceException(couleur);
	}
    }

    public Position getPosition(){
	return new Position(this.position);
    }

    public void setPosition(Position position){
	this.position = new Position(position);
    }

    
    abstract public String getType();
    
    public String getNomCourt(){
	String initiale = this.getType().substring(0,1).toUpperCase();
	String secondeLettre = this.getType().substring(1,2);
	return initiale+secondeLettre+this.couleur;
    }
    
    public String getNomLong(){
	return this.getType()+"_"+this.couleur;
    }


    abstract public ArrayList<Position> getDeplacementPossible(Plateau pl);


    public boolean equals(Object o){
	if (o == this) { 
            return true; 
        } 
  
        if (!(o instanceof Piece)) {
            return false; 
        }

	Piece p = (Piece) o;

	return (this.position.equals(p.position)) && (this.couleur == p.couleur);
    }
    
    
    public String toString(){
	if(this.couleur == 'N')
	    return this.getType() + " noir en " + this.position;
	return this.getType() + " blanc en " + this.position;
    }
}
