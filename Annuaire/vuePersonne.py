### Hurdebourcq Paul ###
##  TD1 TPB || 2022   ##

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QTextEdit, QHBoxLayout,QVBoxLayout, QLabel, QComboBox, QDateEdit
from PyQt6.QtCore import QDate, pyqtSignal
import datetime, genre as g
# ~~~~~~~~~~~~~~~~~~~~
class vuePersonne(QWidget): 
    personneChanged : pyqtSignal = pyqtSignal(dict)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("vue_P")        
        self.topLayout = QVBoxLayout()
        self.setLayout(self.topLayout)
        infoWidget = QWidget()
        self.initLayout = QHBoxLayout()
        infoWidget.setLayout(self.initLayout)
        self.genre : QComboBox = QComboBox()
        self.genre.addItems(["M. ", "Mme ", "_ "])
        self.initLayout.addWidget(self.genre, 1)
        self.prenom : QLineEdit = QLineEdit("Prénom")
        self.initLayout.addWidget(self.prenom,3)
        self.nom : QLineEdit = QLineEdit("Nom")
        self.initLayout.addWidget(self.nom,3)         
        self.topLayout.addWidget(infoWidget,1)
# ~~~~~~~~~~~~~~~~~~~~
        dateWidget = QWidget()
        self.dateLayout = QHBoxLayout()
        dateWidget.setLayout(self.dateLayout)        
        date1Widget = QWidget()
        self.date1Layout = QHBoxLayout()
        date1Widget.setLayout(self.date1Layout)
        self.label : QLabel = QLabel("Né le :")
        self.date1Layout.addWidget(self.label, 1)
        self.dateNaissance : QDateEdit = QDateEdit()
        self.dateNaissance.setDateRange(QDate(1,1,1),QDate.currentDate())
        self.date1Layout.addWidget(self.dateNaissance,1)
        self.dateLayout.addWidget(date1Widget,1)
# ~~~~~~~~~~~~~~~~~~~~  
        date2Widget = QWidget()
        self.date2Layout = QHBoxLayout()
        date2Widget.setLayout(self.date2Layout)
        self.label1 : QLabel = QLabel("Mort le :")
        self.date2Layout.addWidget(self.label1, 1)
        self.dateMort : QDateEdit = QDateEdit()
        self.dateMort.setDateRange(QDate(1,1,1),QDate.currentDate())
        self.date2Layout.addWidget(self.dateMort,1)
        self.dateLayout.addWidget(date2Widget,1)
        self.topLayout.addWidget(dateWidget,1)
# ~~~~~~~~~~~~~~~~~~~~
        bioWidget = QWidget()
        self.innerLayout = QHBoxLayout()
        bioWidget.setLayout(self.innerLayout)
        self.bio : QTextEdit = QTextEdit('"biographie"')
        self.innerLayout.addWidget(self.bio,1)
        self.topLayout.addWidget(bioWidget,5)   
# ~~~~~~~~~~~~~~~~~~~~
        self.genre.currentIndexChanged.connect(self.changeGenre)
        self.prenom.editingFinished.connect(self.changePrenom)
        self.nom.editingFinished.connect(self.changeNom)
        self.bio.textChanged.connect(self.changeBiographie)
        self.dateNaissance.dateChanged.connect(self.changeNaissance)
        self.dateMort.dateChanged.connect(self.changeMort)       
        
        self.show()    
# ~~~~~~~~~~~~~~~~~~~~ 
    def updatePersonne(self, prenom: str, nom:str, genre: g.Genre, nee: datetime.date, mort: (datetime.date|None), bio: str) -> None:
        self.nom.setText(nom)
        self.prenom.setText(prenom)
        self.dateNaissance.setDate(nee)
        self.genre.setCurrentText(str(genre))
        if mort != None:
            self.dateMort.setDate(mort)
        self.bio.setText(bio)          
# ~~~~~~~~~~~~~~~~~~~~         
    def getAllInfo(self) -> dict: 
        dic = { 'nom' : self.nom.text(),
                'prenom' : self.prenom.text(),
                'genre' : self.genre.currentText(),
                'Naissance' : self.dateNaissance.date(),
                'Mort' : self.dateMort.date(),
                'Bio' : self.bio.toPlainText()
            }
        return dic  
# ~~~~~~~~~~~~~~~~~~~~  
    def changeNom(self) -> None : self.personneChanged.emit(self.getAllInfo())
# ~~~~~~~~~~~~~~~~~~~~
    def changePrenom(self) -> None : self.personneChanged.emit(self.getAllInfo())   
# ~~~~~~~~~~~~~~~~~~~~
    def changeNaissance(self) -> None : self.personneChanged.emit(self.getAllInfo())   
# ~~~~~~~~~~~~~~~~~~~~
    def changeGenre(self) -> None : self.personneChanged.emit(self.getAllInfo())
# ~~~~~~~~~~~~~~~~~~~~
    def changeMort(self) -> None : self.personneChanged.emit(self.getAllInfo())
# ~~~~~~~~~~~~~~~~~~~~
    def changeBiographie(self) -> None : self.personneChanged.emit(self.getAllInfo())
# ~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    appli = QApplication(sys.argv)
    vueP = vuePersonne()
    sys.exit(appli.exec())
    
### Hurdebourcq Paul ###
##  TD1 TPB || 2022   ##