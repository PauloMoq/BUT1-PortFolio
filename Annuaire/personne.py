# --- import
import json
import datetime, genre as g
# ---------------------------------
# --- class Personne
# ---------------------------------
class Personne:
    # constructor
    def __init__(self, prenom : str, nom : str, 
        genre : g.Genre, 
        dateNaissance : datetime.date, dateMort : (datetime.date | None), 
        bio : str) -> None: 
        self.__prenom : str = prenom
        self.__nom : str = nom
        self.__genre : g.Genre = genre
        self.__naissance : datetime.date = dateNaissance
        self.__mort : (datetime.date | None) = dateMort
        self.__bio = bio
    
    def __repr__(self) -> str:
        res = ""
        if self.__genre == g.Genre.M : res += "M. "
        elif self.__genre == g.Genre.F : res += "Mme "
        else : res += "_ "
        res += self.__prenom +" "+ self.__nom+",("
        res += str(self.__naissance)
        if self.__mort:
            res += "/ "+str(self.__mort)+")"
        else: res += ")"
        res += ':"'+self.__bio+'".'
        return res

    @property
    def prenom(self) -> str: return self.__prenom
    @prenom.setter
    def prenom(self, prenom :str) -> None: self.__prenom = prenom[0].upper()+prenom[1:].lower()  

    @property
    def nom(self) -> str: return self.__nom
    @nom.setter
    def nom(self, nom :str) -> None: self.__nom = nom[0].upper()+nom[1:].lower() 
    
    @property
    def genre(self) -> g.Genre: return self.__genre
    @genre.setter
    def genre(self, genre : g.Genre) -> None: self.__genre = genre 

    @property
    def naissance(self) -> datetime.date : return self.__naissance
    @naissance.setter
    def naissance(self, date : datetime.date) : self.__naissance = date

    @property
    def mort(self) -> (datetime.date | None) : return self.__mort
    @mort.setter
    def mort(self, date : datetime.date) : self.__mort = date

    @property
    def bio(self) -> str : return self.__bio
    @bio.setter
    def bio(self, txt : str) -> None: self.__bio = txt

    # toJSON
    def toJSON(self) -> str:
        dictP = {
            'genre'  : str(self.__genre) ,
            'prenom' : self.__prenom,
            'nom'    : self.__nom,
            'naissance' : str(self.__naissance),
            'mort'      : str(self.__mort),
            'bio'    : self.__bio
        }
        return json.dumps(dictP,ensure_ascii=False)

    # buildFromJson
    @staticmethod
    def buildFromJSon(d: dict):
        # genre
        genreSTR : str = d['genre'] 
        if genreSTR == 'M': genre = g.Genre.M
        elif genreSTR == 'F': genre = g.Genre.F
        else : genre = g.Genre.O
        # prenom
        prenom :str =  d['prenom'] 
        nom : str =  d['nom'] 
        naissanceSTR : str = d['naissance']
        elts = naissanceSTR.split('-')
        dateNaissance = datetime.date(int(elts[0]),int(elts[1]),int(elts[2])) 
        mortSTR : str = d['mort']
        if mortSTR :
            elts = mortSTR.split('-')
            dateMort = datetime.date(int(elts[0]),int(elts[1]),int(elts[2])) 
        else:
            dateMort = None
        bio = d['bio'] 

        return Personne(prenom, nom, genre,dateNaissance,dateMort, bio)

    # new
    @staticmethod
    def new(): return Personne("Prénom", "Nom", g.Genre.O,  datetime.date.today(), None, "biographie") 

# --- main: kind of unit test
if __name__ == "__main__" :
    print('TEST: class Personne')
    print('\t création Personne',  end=': ')
    a : Personne= Personne('prénom','nom',g.Genre.O, datetime.date(2001,2,28), None, 'bla-bla'); a.nom = "xxx"
    b : Personne = Personne.new()
    print(' done!')
    print('\t str(Personne)', end=': ')
    print(a.toJSON())
    print(b.toJSON())
