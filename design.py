# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designematue.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(286, 212)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputAbrirArquivo = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAbrirArquivo.setGeometry(QtCore.QRect(10, 10, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputAbrirArquivo.setFont(font)
        self.inputAbrirArquivo.setMouseTracking(True)
        self.inputAbrirArquivo.setInputMask("")
        self.inputAbrirArquivo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.inputAbrirArquivo.setDragEnabled(False)
        self.inputAbrirArquivo.setReadOnly(False)
        self.inputAbrirArquivo.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.inputAbrirArquivo.setClearButtonEnabled(True)
        self.inputAbrirArquivo.setObjectName("inputAbrirArquivo")
        self.btnenviarnumero = QtWidgets.QPushButton(self.centralwidget)
        self.btnenviarnumero.setGeometry(QtCore.QRect(70, 170, 141, 31))
        self.btnenviarnumero.setObjectName("btnenviarnumero")
        self.getnomearquivo = QtWidgets.QLineEdit(self.centralwidget)
        self.getnomearquivo.setGeometry(QtCore.QRect(10, 60, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.getnomearquivo.setFont(font)
        self.getnomearquivo.setMouseTracking(True)
        self.getnomearquivo.setInputMask("")
        self.getnomearquivo.setAlignment(QtCore.Qt.AlignCenter)
        self.getnomearquivo.setDragEnabled(False)
        self.getnomearquivo.setReadOnly(False)
        self.getnomearquivo.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.getnomearquivo.setClearButtonEnabled(True)
        self.getnomearquivo.setObjectName("getnomearquivo")
        self.envioemail = QtWidgets.QCheckBox(self.centralwidget)
        self.envioemail.setEnabled(False)
        self.envioemail.setGeometry(QtCore.QRect(20, 120, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.envioemail.setFont(font)
        self.envioemail.setObjectName("envioemail")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerador de Planilhas"))
        self.inputAbrirArquivo.setText(_translate("MainWindow", "Numero pedido de parada"))
        self.btnenviarnumero.setText(_translate("MainWindow", "Enviar"))
        self.getnomearquivo.setText(_translate("MainWindow", "Nome do arquivo"))
        self.envioemail.setText(_translate("MainWindow", "Email cliente end. errado"))
