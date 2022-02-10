import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6 import uic
import metodo as calcular


class Ejemplo01(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("formulario2-1.ui",self)
        self.initUi()

    def initUi(self):
        self.breset.clicked.connect(self.resetear)
        self.bsalir.clicked.connect(self.salir)
        self.boton_a.clicked.connect(self.categoriaA)
        self.boton_b.clicked.connect(self.categoriaB)
        self.boton_c.clicked.connect(self.categoriaC)
        self.boton_d.clicked.connect(self.categoriaD)
        self.boton_e.clicked.connect(self.categoriaE)


    def resetear(self):
        self.lb_ocupacion.setText("")
        self.lb_sueldo.setText("")
        self.lb_descuento1.setText("")
        self.lb_descuento2.setText("")
        self.lb_bonificacion1.setText("")
        self.lb_bonificacion2.setText("")
    
    def categoriaA (self):
        self.lb_ocupacion.setText("Analista")
        self.lb_sueldo.setText("2500 S/.")
        self.lb_descuento1.setText(str(calcular.descuento1(2500,1)))
        self.lb_descuento2.setText(str(calcular.descuento2(2500,1)))
        self.lb_bonificacion1.setText(str(calcular.bonificacion1(2500,1)))
        self.lb_bonificacion2.setText(str(calcular.bonificacion2(2500,1)))

    def categoriaB (self):
        self.lb_ocupacion.setText("Programador")
        self.lb_sueldo.setText("1500 S/.")
        self.lb_descuento1.setText(str(calcular.descuento1(1500,2)))
        self.lb_descuento2.setText(str(calcular.descuento2(1500,2)))
        self.lb_bonificacion1.setText(str(calcular.bonificacion1(1500,2)))
        self.lb_bonificacion2.setText(str(calcular.bonificacion2(1500,2)))
    def categoriaC (self):
        self.lb_ocupacion.setText("Asistente")
        self.lb_sueldo.setText("1000 S/.")
        self.lb_descuento1.setText(str(calcular.descuento1(1000,3)))
        self.lb_descuento2.setText(str(calcular.descuento2(1000,3)))
        self.lb_bonificacion1.setText(str(calcular.bonificacion1(1000,3)))
        self.lb_bonificacion2.setText(str(calcular.bonificacion2(1000,3)))
    def categoriaD (self):
        self.lb_ocupacion.setText("Tecnico")
        self.lb_sueldo.setText("700 S/.")
        self.lb_descuento1.setText(str(calcular.descuento1(700,4)))
        self.lb_descuento2.setText(str(calcular.descuento2(700,4)))
        self.lb_bonificacion1.setText(str(calcular.bonificacion1(700,4)))
        self.lb_bonificacion2.setText(str(calcular.bonificacion2(700,4)))
    def categoriaE (self):
        self.lb_ocupacion.setText("Operador")
        self.lb_sueldo.setText("500 S/.")
        self.lb_descuento1.setText(str(calcular.descuento1(500,5)))
        self.lb_descuento2.setText(str(calcular.descuento2(500,5)))
        self.lb_bonificacion1.setText(str(calcular.bonificacion1(500,5)))
        self.lb_bonificacion2.setText(str(calcular.bonificacion2(500,5)))

    def salir(self):
        self.close()




if __name__=='__main__':
    app = QApplication(sys.argv)
    ventana1=Ejemplo01()
    ventana1.show()
    sys.exit(app.exec())
    