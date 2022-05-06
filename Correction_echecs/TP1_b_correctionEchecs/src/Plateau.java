import java.util.ArrayList;

class Plateau{
    private ArrayList<Piece> pieces;

    public Plateau(){
	pieces = new ArrayList<Piece>();
	this.ajouterPiece(new Tour('B', new Position("A1")));
	this.ajouterPiece(new Cavalier('B', new Position("B1")));
	this.ajouterPiece(new Fou('B', new Position("C1")));
	this.ajouterPiece(new Dame('B', new Position("D1")));
	this.ajouterPiece(new Roi('B', new Position("E1")));
	this.ajouterPiece(new Fou('B', new Position("F1")));
	this.ajouterPiece(new Cavalier('B', new Position("G1")));
	this.ajouterPiece(new Tour('B', new Position("H1")));

	for(char c = 'A'; c < 'I' ; c++){
	    this.ajouterPiece(new PionBlanc(new Position(c+"2")));
	    this.ajouterPiece(new PionNoir(new Position(c+"7")));
	}

	this.ajouterPiece(new Tour('N', new Position("A8")));
	this.ajouterPiece(new Cavalier('N', new Position("B8")));
	this.ajouterPiece(new Fou('N', new Position("C8")));
	this.ajouterPiece(new Dame('N', new Position("D8")));
	this.ajouterPiece(new Roi('N', new Position("E8")));
	this.ajouterPiece(new Fou('N', new Position("F8")));
	this.ajouterPiece(new Cavalier('N', new Position("G8")));
	this.ajouterPiece(new Tour('N', new Position("H8")));
    }


    private boolean ajouterPiece(Piece p) throws CaseOccupeeException{
	// Vérifier si une pièce n'est pas déjà placé sur la case.
	for(Piece item : pieces)
	    if(item.getPosition().equals(p.getPosition())){
			throw new CaseOccupeeException(p);
	    }
	pieces.add(p);
	return true;
    }


    public Piece getCase(Position position){
	for(Piece p : pieces)
	    if(p.getPosition().equals(position))
		return p;

	return null;
    }

    public Piece getCase(int x, int y){
	return this.getCase(new Position(x,y));
    }

    public Piece getCase(String position){
	return this.getCase(new Position(position));
    }


    public ArrayList<Piece> getPiecesBlanches(){
	ArrayList<Piece> liste = new ArrayList<Piece>();
	for(Piece p : pieces)
	    if(p.getCouleur()=='B')
		liste.add(p);

	return liste;
    }

    public ArrayList<Piece> getPiecesNoires(){
	ArrayList<Piece> liste = new ArrayList<Piece>();
	for(Piece p : pieces)
	    if(p.getCouleur()=='N')
		liste.add(p);

	return liste;
    }
    

    public void deplacer(Position from, Position to) throws ErreurDeplacementException{
	Piece aDeplacer = this.getCase(from);
	if(aDeplacer == null){
	    throw new ErreurDeplacementException(from, to);
	}
	if(!aDeplacer.getDeplacementPossible(this).contains(to)){
		throw new ErreurDeplacementException(from, to);
	}
	
	Piece caseArrivee = this.getCase(to);
	
	pieces.remove(caseArrivee);
	
	aDeplacer.setPosition(to);
    }

    public void deplacer(String from, String to){
	this.deplacer(new Position(from), new Position(to));
    }

    public void deplacer(int xf, int yf, int xt, int yt){
	this.deplacer(new Position(xf,yf), new Position(xt,yt));
    }
    

    public Piece getRoi(char couleur) throws RoiNonTrouveException{
	for(Piece p : pieces)
	    if((p.getType().equals("roi")) && (p.getCouleur()==couleur))
		return p;
	
	throw new RoiNonTrouveException(couleur);
    }

    public Piece getRoiBlanc(){
	return this.getRoi('B');
    }

    public Piece getRoiNoir(){
	return this.getRoi('N');
    }
    

    public boolean estEchec(char couleur){
	if(couleur == 'B'){
	    Piece roiBlanc = this.getRoiBlanc();
	    Position positionRoiBlanc = roiBlanc.getPosition();
	    ArrayList<Piece> liste= this.getPiecesNoires();
	    for(Piece p : liste){
		ArrayList<Position> coupPossible = p.getDeplacementPossible(this);
		for(Position pos : coupPossible)
		    if(pos.equals(positionRoiBlanc))
			return true;
	    }
	}else{
	    Piece roiNoir = this.getRoiNoir();
	    Position positionRoiNoir = roiNoir.getPosition();
	    ArrayList<Piece> liste = this.getPiecesBlanches();
	    for(Piece p : liste){
		ArrayList<Position> coupPossible = p.getDeplacementPossible(this);
		for(Position pos : coupPossible)
		    if(pos.equals(positionRoiNoir))
			return true;
	    }
	}
	return false;
    }
    

    public String toString(){
	String retour = "  ";
	for(char c = 'A' ; c < 'I' ; c++)
	    retour = retour + " " + c + "  ";
	retour = retour+"\n";
	for(int j = 8 ; j>=1 ; j--){
	    retour = retour + " |---|---|---|---|---|---|---|---| \n";
	    retour = retour + j + "|";
	    for(int i = 'A' ; i < 'I' ; i++){
		Piece p = this.getCase((char)(i)+""+j);
		if(p==null)
		    retour = retour+"   |";
		else
		    retour = retour+p.getNomCourt()+"|";
	    }
	    retour = retour+j+"\n";
	}
	retour = retour + " |---|---|---|---|---|---|---|---| \n";
	retour = retour + "  ";
	for(char c = 'A' ; c < 'I' ; c++)
	    retour = retour + " " + c + "  ";
	
	return retour;
    }
    

    public static void main(String[] args){
	Plateau p = new Plateau();
	System.out.println(p);
    }
}
