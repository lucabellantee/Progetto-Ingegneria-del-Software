from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Cliente import Cliente
from RistoMatic.GestioneAttivita.OrdineAsporto import OrdineAsporto
from RistoMatic.GestioneAttivita.Prenotazione import Prenotazione

class VistaAggiungiOrdineAsporto(QWidget):

    def __init__(self, callback):
        super(VistaAggiungiOrdineAsporto, self).__init__()

        self.callback = callback

        self.vLayout = QVBoxLayout()
        self.qlines = {}
        self.addInfoText("nome", "Nome")
        self.addInfoText("recapitoTelefonico", "Recapito Telefonico")
        self.addInfoText("oraConsegna", "Ora consegna")
   #     self.addInfoText("oraOrdine", "oraOrdine")

        okButton = QPushButton("OK")
        ordine = okButton.clicked.connect(self.aggiungiOrdine)
        self.qlines["okButton"] = okButton
        self.vLayout.addWidget(okButton)
        self.setLayout(self.vLayout)
        #self.callback()

    def addInfoText(self, nome, label):
        self.vLayout.addWidget(QLabel(label))
        testo = QLineEdit(self)
        self.qlines[nome] = testo
        self.vLayout.addWidget(testo)


    def aggiungiOrdine(self):
        self.cliente = Cliente("", "")
        self.ordine = OrdineAsporto(None, None, self.cliente)

        self.nome = self.qlines["nome"].text()
        self.recapitoTelefonico = self.qlines["recapitoTelefonico"].text()
        self.oraConsegna = self.qlines["oraConsegna"].text()

        nOrdini = 0
        for i in StatoSala.OrdiniAsporto:
            if i.oraConsegna == self.oraConsegna:
                nOrdini += 1

            if nOrdini >= 4:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERRORE!")
                msg.setInformativeText("Ci sono già troppi ordini per quell'ora")
                msg.exec_()
                return


        self.ordine.setOraConsegna(self.oraConsegna)
        self.ordine.cliente.setNomeCliente(self.nome)
        self.ordine.cliente.setRecapitoTelefonico(self.recapitoTelefonico)

        StatoSala.aggiungiOrdineAsporto(self.ordine)
        self.callback()
        self.close()
