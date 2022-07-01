import sys
from PySide6.QtWidgets import QTabWidget, QVBoxLayout, QScrollArea , QWidget, QGridLayout, QLabel, QLineEdit,QPushButton, QMessageBox
from RistoMatic.Viste.MainVistaSala import VistaSala


class VistaUnlockAmministratore(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Accesso Amministratore')
        self.resize(500, 120)

        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Inserisci il nome-utente')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Inserisci la tua password')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Accedi')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)


    def check_password(self):
        msg = QMessageBox()
        if self.lineEdit_username.text()=='a' and self.lineEdit_password.text()=='a':
            self.close()
            msg.setText('Autenticazione effettuata ! Buon lavoro')
            msg.exec()
            self.vistaSala = VistaSala()
            self.vistaSala.resize(1280,720)
            self.vistaSala.show()


            #self.destroy(True)

        else:
             msg.setText('Ops ! Qualcosa è andato storto , riprova !')
             msg.exec()


