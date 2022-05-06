class Position{
    private int x, y;

    public Position(){
	this.x = 0;
	this.y = 0;
    }

    public Position(int x, int y) throws ErreurCoordonneesException{
	if(x < 0 || x > 7 || y < 0 || y > 7){
	    throw new ErreurCoordonneesException(x, y);
	}
	this.x = x;
	this.y = y;
    }

    public Position(String position) throws ErreurCoordonneesException{
	if(position.length()!=2){
	    throw new ErreurCoordonneesException(position);
	}
	if(position.charAt(0)<'A' || position.charAt(0)>'H'){
		throw new ErreurCoordonneesException(position);
	}
	if(position.charAt(1)<'1' || position.charAt(1)>'8'){
		throw new ErreurCoordonneesException(position);
	}
	this.x = (int)(position.charAt(0)-'A');
	this.y = (int)(position.charAt(1)-'1');
    }

    public Position(Position position){
	this.x = position.x;
	this.y = position.y;
    }

    

    public int getX(){
	return this.x;
    }

    public int getY(){
	return this.y;
    }

    public void setX(int x) throws ErreurCoordonneesException{
	if(x < 0 || x > 7){
	    throw new ErreurCoordonneesException(x);
	}
	this.x = x;
    }

    public void setY(int y) throws ErreurCoordonneesException{
	if(y < 0 || y > 7){
	    throw new ErreurCoordonneesException(y);
	}
	this.y = y;
    }


    public boolean equals(Object o) {
        if (o == this) { 
            return true; 
        } 
  
        if (!(o instanceof Position)) {
            return false; 
        } 
	
        Position p = (Position) o; 
          
        return (this.x == p.x) && (this.y == p.y);
    }
    

    public String toString(){
	return "("+(char)(x+'A')+""+(y+1)+")";
    }

    

    public static void main(String[] args){
	Position p = new Position();
	System.out.println(p);
	p = new Position(3,2);
	System.out.println(p);
	p = new Position("F6");
	System.out.println(p);
	p = new Position(9,5);
	System.out.println(p);
	p = new Position("T2");
	System.out.println(p);
	p = new Position(5,12);
	System.out.println(p);
	p = new Position("A9");
	System.out.println(p);
    }
}
