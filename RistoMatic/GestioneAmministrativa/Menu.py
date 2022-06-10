import datetime
from RistoMatic.GestioneAmministrativa.ElementoMenu import ElementoMenu
from RistoMatic.GestioneAttivita.Enum import Zone
from RistoMatic.GestioneAttivita.StatoSala import StatoSala

class Menu:
    def __init__(self, costo_coperto=0, nome_menu=""):
        self.costoCoperto=costo_coperto
        self.dataCreazione = datetime.datetime.now()
        self.nomeMenu=nome_menu
        self.listaElementi = dict()

        StatoSala.aggiungiMenu(self)

        #dati esempio
        self.aggiungiElementoMenu(ElementoMenu("pizza", Zone.CUCINA, 10))
        self.aggiungiElementoMenu(ElementoMenu("birra", Zone.BAR, 3))
        self.aggiungiElementoMenu(ElementoMenu("pasta", Zone.CUCINA, 6))

    def aggiungiElementoMenu(self, elemento: ElementoMenu):
        if (isinstance(elemento,ElementoMenu)):
            self.listaElementi[elemento.nomeElemento] = elemento
        else:
            raise Exception("Not ElementoMenu")

    def eliminaElementoMenu(self, nome: str):
        del(self.listaElementi[nome])

    def getCostoCoperto(self):
        return self.costoCoperto

    def getDataCreazione(self):
        return self.dataCreazione

    def getInfoMenu(self):
        return {
            "nomeMenu": self.nomeMenu,
            "costoCoperto": self.costoCoperto,
            "dataCreazione": self.dataCreazione
        }

    def getNomeMenu(self):
        return self.nomeMenu

    def getListaElementi(self):
        return self.listaElementi

    def setCostoCoperto(self, costo):
        self.costoCoperto=costo

    def setDataCreazione(self, data):
        try:
            self.dataCreazione = datetime.datetime.strptime(data, "%d/%m/%Y")
        except:
            raise Exception("Not a date")

    def setNomeMenu(self, nome: str):
        self.nomeMenu = nome

    def setActive(self):
        StatoSala.setMenuAttivo(self)