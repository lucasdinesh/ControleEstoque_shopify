import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QCheckBox
from time import sleep

from design import Ui_MainWindow
from main import executa
import threading


class Planilha(QMainWindow, Ui_MainWindow,QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnenviarnumero.clicked.connect(self.receber_pedido)
        self.btnenviarnumero.clicked.connect(self.show_Popup)
        self.setWindowIcon(QtGui.QIcon('logo.png'))

    def receber_pedido(self):
        self.pedido = self.inputAbrirArquivo.text()
        self.nome_arquivo = self.getnomearquivo.text()
        print(self.pedido, self.nome_arquivo)

    def show_Popup(self):
        sleep(2)
        message=QMessageBox()
        message.setWindowTitle("Aviso")
        message.setText("Aguarde")
        message.setIcon(QMessageBox.Information)
        message.setInformativeText('Estamos gerando a planilha :)')

        x = message.exec_()
        threading.Thread(target=executa, args=(self.pedido, self.nome_arquivo, self.envioemail.isChecked())).start()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Planilha()
    novo.show()
    qt.exec_()