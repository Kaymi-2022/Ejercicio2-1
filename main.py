import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6 import uic


class Ejemplo01(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("formulario2-1.ui",self)
        self.initUi()

    def initUi(self):
        self.breset.clicked.connect(self.resetear)
        self.bcalcular.clicked.connect(self.calcular)
        self.bsalir.clicked.connect(self.salir)

    def resetear(self):
        self.bcategoria_a.clicked.connect(self.resetear)
        self.bcategoria_b.clicked.connect(self.resetear)
        self.bcategoria_c.clicked.connect(self.resetear)
        self.bcategoria_d.clicked.connect(self.resetear)
        self.bcategoria_e.clicked.connect(self.resetear)




if __name__=='__main__':
    app = QApplication(sys.argv)
    ventana1=Ejemplo01()
    ventana1.show()
    sys.exit(app.exec())
    