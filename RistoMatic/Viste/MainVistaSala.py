from PySide6.QtWidgets import QTabWidget, QVBoxLayout, QScrollArea

from RistoMatic.Viste.VistaComande import VistaComande
from RistoMatic.Viste.VistaPrenotazioni import VistaPrenotazioni
from RistoMatic.Viste.VistaTavoli import VistaTavoli
from PySide6 import QtWidgets


class VistaSala(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vista Sala")
        self.layout = QVBoxLayout(self)

        self.tabTavoli = VistaTavoli()
        self.tabPrenotazioni = VistaPrenotazioni()

        self.tabComande = VistaComande()
        self.areaComande = QScrollArea(widgetResizable=True)
        self.areaComande.setWidget(self.tabComande)

        self.tabAsporto = QtWidgets.QWidget()
        self.tabAmministrazione = QtWidgets.QWidget()

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.South)
        self.tabs.setStyleSheet("QTabBar::tab { height: 100px; width: 200%;}")
        self.tabs.resize(300, 200)
        self.tabs.addTab(self.tabTavoli, "Tavoli")
        self.tabs.addTab(self.tabPrenotazioni, "Prenotazioni")
        self.tabs.addTab(self.areaComande, "Comande")
        self.tabs.addTab(self.tabAsporto, "Asporto")
        self.tabs.addTab(self.tabAmministrazione, "Amministrazione")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)