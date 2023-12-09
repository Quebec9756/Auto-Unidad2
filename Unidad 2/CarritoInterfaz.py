import sys
import serial as conecta
from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "interCar.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.btn_accion.clicked.connect(self.toggle_connection)
        self.arduino = None
        self.btnAvanza.clicked.connect(self.avanza)
        self.btnReversa.clicked.connect(self.reversa)
        self.btnIzquierda.clicked.connect(self.izquierda)
        self.btnDerecha.clicked.connect(self.derecha)
        self.btnAlto.clicked.connect(self.alto)

    def toggle_connection(self):
        try:
            txt_btn = self.btn_accion.text()
            puerto = "COM" + self.txt_puerto.text()

            if txt_btn == "CONECTAR":
                self.btn_accion.setText("DESCONECTAR")
                self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=10)
            elif txt_btn == "DESCONECTAR":
                self.btn_accion.setText("RECONECTAR")
                self.arduino.close()
            else:
                self.btn_accion.setText("DESCONECTAR")
                self.arduino.open()
                self.arduino.port = puerto
                self.arduino = conecta.Serial(puerto, baudrate=9600, timeout=10)
        except Exception as error:
            print(error)



    def avanza(self):
        self.arduino.write("0".encode())
        print("Avanza")
    def reversa(self):
        self.arduino.write("1".encode())
        print("Reversa")
    def izquierda(self):
        self.arduino.write("2".encode())
        print("Izquierda")
    def derecha(self):
        self.arduino.write("3".encode())
        print("Derecha")
    def alto(self):
        self.arduino.write("4".encode())
        print("Alto")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
