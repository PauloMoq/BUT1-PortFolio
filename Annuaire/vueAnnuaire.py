### Hurdebourcq Paul ###
##  TD1 TPB || 2022   ##

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout,QVBoxLayout
from PyQt6.QtCore import pyqtSignal
import vuePersonne

# ~~~~~~~~~~~~~~~~~~~~
class vueAnnuaire(QWidget):
    newClicked = pyqtSignal()
    openFileClicked = pyqtSignal(str)
    nextClicked = pyqtSignal()
    saveAsClicked =pyqtSignal(str)
    previousClicked = pyqtSignal()
    personneChanged = pyqtSignal(dict)
# ~~~~~~~~~~~~~~~~~~~~
    def __init__(self):
        super().__init__()
        self.setWindowTitle("vue_A")
# ~~~~~~~~~~~~~~~~~~~~
        self.bvLayout = QVBoxLayout()
        self.setLayout(self.bvLayout)
        self.personne = vuePersonne.vuePersonne()
        self.bvLayout.addWidget(self.personne)
        self.tbete = QWidget()
        self.innerlayout = QHBoxLayout()
        self.tbete.setLayout(self.innerlayout)
        self.new : QPushButton = QPushButton("New")
        self.previous : QPushButton = QPushButton("Previous") 
        self.load : QPushButton = QPushButton("Load")
        self.next : QPushButton = QPushButton("Next")
        self.saveas : QPushButton = QPushButton("Save As")
        self.innerlayout.addWidget(self.saveas,1)
        self.innerlayout.addWidget(self.previous,1)
        self.innerlayout.addWidget(self.load,1)
        self.innerlayout.addWidget(self.next,1) 
        self.bvLayout.addWidget(self.tbete)
        self.innerlayout.addWidget(self.new,1)   
        self.previous.clicked.connect(self.precedent)
        self.load.clicked.connect(self.charger)
        self.new.clicked.connect(self.nouveau)
        self.saveas.clicked.connect(self.sauvegarder)
        self.next.clicked.connect(self.suivant)
        self.show()
# ~~~~~~~~~~~~~~~~~~~~
    def updatePersonne(self, prenom,nom, genre, nee, mort, bio):
        self.personne.updatePersonne(prenom, nom, genre, nee, mort, bio)
# ~~~~~~~~~~~~~~~~~~~~
    def precedent(self):
        self.previousClicked.emit()
# ~~~~~~~~~~~~~~~~~~~~
    def nouveau(self):
        self.newClicked.emit()   
# ~~~~~~~~~~~~~~~~~~~~
    def suivant(self):
        self.nextClicked.emit()  
# ~~~~~~~~~~~~~~~~~~~~
    def charger(self):
        self.openFileClicked.emit("json.file")
# ~~~~~~~~~~~~~~~~~~~~
    def sauvegarder(self):
        self.saveAsClicked.emit("json.file") 
# ~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":    
    appli = QApplication(sys.argv)
    vueA = vueAnnuaire()
    sys.exit(appli.exec())

### Hurdebourcq Paul ###
##  TD1 TPB || 2022   ##