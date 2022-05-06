abstract class Pion extends Piece{
    
    public Pion(){
	super('B', new Position());
    }

    public Pion(char couleur, Position position){
	super(couleur, position);
    }
    
    public String getType(){
    	return new String("pion");
    }
}
