import datetime
from RistoMatic.GestioneAmministrativa.Menu import Menu

class StatoSala():
    OrdiniAsporto =[]
    Tavoli = []
    Prenotazioni = []
    Comande = []
    Menu = Menu(2,"summer")

    def __init__(self):
        pass

    @staticmethod
    def aggiungiTavolo(tavolo):
        StatoSala.Tavoli.append(tavolo)

    @staticmethod
    def aggiungiComanda(comanda):
        StatoSala.Comande.append(comanda)

    def aggiungiOrdineAsporto(self,oraConsegna : datetime):
        pass

    def confermaPrenotazione(self, daConfermare):
        pass

    def createPrenotazione(self, daCreare):
        pass

    def getComanda(self) -> dict:
        pass

    def getListaAsporto(self) -> dict:
        pass

    def getListaCodaPrenotazione(self) -> dict:
        pass

    def getListaPrenotazioni(self) -> dict:
        pass

    def getPrenotazione(self,nomeCliente : str, data : datetime):
        pass

    def getTavolo(self,riferimento : int) -> dict:
        pass

    def inviaRisposta(self) :
        pass

    def modificaOrdineAsporto(self,nomeCliente : str):
        pass

    def modificaTavolo(self,riferimentoTavolo : int):
        pass

    def notificaDisponibilita(self,numeroCellulareCliente : str, nomeCliente : str):
        pass

    def ricercaPrenotazione(self, nomeCliente : str, dataPrenotazione : datetime):
        pass

    def ricercaTavolo(self,riferimentoTavolo : int):
        pass

    def rimuoviOrdineAsporto(self,nomeCliente : str):
        pass

    def rimuoviPrenotazioniNonConfermate(self):
        pass

    def rimuoviTavolo(self,riferimentoTavolo : int):
        pass