# import(s)
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QResizeEvent

# -------------- function
def lowerUp(s:str) -> str: 
    """converts uppercase to lowercase and vice versa
    
        @args:
            s : str
        @return :
            str

        @example:
            lowerUp(HeLLo) -> 'hEllO'
    """
    return ''.join(list(map(lambda x: x.lower() if x.isupper() else x.upper(), list(s))))
# -------------- class: encodeGUI
class encodeGUI (QWidget):

    def __init__(self, orientation):
        """"constructor"""
        super().__init__()
        self.orientation = orientation

        if self.orientation == Qt.Orientation.Horizontal:
            self.topLayout = QHBoxLayout()
        else:
            self.topLayout = QVBoxLayout()
        
        self.setLayout(self.topLayout)

        self.input = QLineEdit('saisissez votre texte ici.')
        self.action = QPushButton('encode')
        self.output = QLineEdit('le résultat apparaitra ici.')

        self.topLayout.addWidget(self.input)
        self.topLayout.addWidget(self.action)
        self.topLayout.addWidget(self.output)

        self.action.clicked.connect(self.cbEncode)

    def cbEncode(self):
        """callback called when action is clicked"""
        self.output.setText(lowerUp(self.input.text()))

# -------------- class: GUI
class GUI(QWidget):
    
    def __init__(self):
        """constructor"""
        super().__init__()

        self.topLayout = QVBoxLayout()
        self.setLayout(self.topLayout)

        self.encodeWidget = encodeGUI(Qt.Orientation.Horizontal)

        self.topLayout.addStretch()

        self.topLayout.addWidget(self.encodeWidget)


        self.resize(450,50)
        self.setMinimumWidth(450)


        self.show()

    def rotate(self):
        """callback called when change orientaion is called or widget size ratio exceed threshold"""
        if self.encodeWidget.orientation  == Qt.Orientation.Horizontal: 
            newEncode = encodeGUI(Qt.Orientation.Vertical)
        else:
            newEncode = encodeGUI(Qt.Orientation.Horizontal)

        self.encodeWidget.deleteLater()

        self.encodeWidget = newEncode

        self.topLayout.addWidget(self.encodeWidget)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        """ resize event callback"""
        width = a0.size().width()
        height = a0.size().height()

        if height*4 >= width:
            if self.encodeWidget.orientation == Qt.Orientation.Horizontal:  self.rotate()
        else:
            if self.encodeWidget.orientation == Qt.Orientation.Vertical : self.rotate()

        return super().resizeEvent(a0)  

# -------------- main --------------
if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    t = GUI()

    sys.exit(app.exec())
        



