import java.util.ArrayList;

class Roi extends Piece{
    
    public Roi(){
	super('B', new Position());
    }

    public Roi(char couleur, Position position){
	super(couleur, position);
    }


    public String getType(){
    	return new String("roi");
    }
    

    public ArrayList<Position> getDeplacementPossible(Plateau pl)
    {
	ArrayList<Position> liste = new ArrayList<Position>();
	int positionDepartX = this.getPosition().getX();
	int positionDepartY = this.getPosition().getY();
	
	for(int i=-1 ; i<2 ; i++)
	    for(int j = -1; j<2 ;j++)
		if( i!= 0 || j!=0){
		    int indiceX = positionDepartX+i;
		    int indiceY = positionDepartY+j;
		    if((indiceX >= 0) && (indiceX < 8) && (indiceY >= 0) && (indiceY < 8)){
			Piece pi = pl.getCase(indiceX, indiceY);
			if(pi == null)
			    liste.add(new Position(indiceX, indiceY));
			else{
			    if(pi.getCouleur() != this.getCouleur())
				liste.add(new Position(indiceX, indiceY));
			}
		    }
		}
	
	return liste;
    }


}
