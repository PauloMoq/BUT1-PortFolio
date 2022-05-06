### Hurdebourcq Paul ###
##  TD1 TPB || 2022   ##

import sys
from PyQt6.QtWidgets import QApplication
import annuaire, personne, vueAnnuaire
# ~~~~~~~~~~~~~~~~~~~~
class Controller :
    def __init__(self) -> None:
        self.modele = annuaire.Annuaire('anphi.json')
        self.vue = vueAnnuaire.vueAnnuaire()
        p = self.modele.getPersonne()
        if isinstance(p, personne.Personne) : self.vue.updatePersonne(p.prenom, p.nom, p.genre, p.naissance, p.mort, p.bio)
        self.vue.nextClicked.connect(self.next)
        self.vue.previousClicked.connect(self.previous)
        self.vue.openFileClicked.connect(self.openFile)
        self.vue.newClicked.connect(self.new)
        self.vue.personneChanged.connect(self.update)
        self.vue.saveAsClicked.connect(self.saveAs)
# ~~~~~~~~~~~~~~~~~~~~
    def update(self,d) -> None :
        if isinstance(d, personne.Personne):
            self.vue.updatePersonne(d.prenom, d.nom, d.genre, d.naissance, d.mort, d.bio)
# ~~~~~~~~~~~~~~~~~~~~
    def next(self) -> None:
        self.modele.next()
        self.update(self.modele.getPersonne())
# ~~~~~~~~~~~~~~~~~~~~
    def previous(self) -> None:
        self.modele.previous()
        self.update(self.modele.getPersonne())
# ~~~~~~~~~~~~~~~~~~~~
    def new(self) -> None: 
        self.modele.addPersonne(personne.Personne.new())
        self.update(self.modele.getPersonne())
# ~~~~~~~~~~~~~~~~~~~~
    def openFile(self, fname : str) -> None:
        self.modele = annuaire.Annuaire(fname)
        self.update(self.modele.getPersonne)
# ~~~~~~~~~~~~~~~~~~~~     
    def saveAs(self, fname: str) -> None:
        self.modele.save(fname)
# ~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    appli = QApplication(sys.argv)
    screen = appli.screens()[0]
    firstWindow = Controller()
    sys.exit(appli.exec())

### Hurdebourcq Paul ###
##  TD1 TPB || 2022   ##