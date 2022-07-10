from RistoMatic.GestioneAttivita.StatoSala import StatoSala
from RistoMatic.GestioneAttivita.Enum import StatoTavolo
import datetime

class Tavolo():
    counter_n_tavolo = 1

    def __init__(self, posti, riferimento = 0):
        super(Tavolo, self).__init__()
#        self.riferimentoTavolo = Tavolo.counter_n_tavolo
        self.numeroPosti = posti
        self.numeroCoperti = 0
        self.isLibero = True
        if riferimento == 0:
            self.riferimentoTavolo = Tavolo.counter_n_tavolo
            Tavolo.counter_n_tavolo = Tavolo.counter_n_tavolo + 1

        elif riferimento != 0:
            self.riferimentoTavolo = riferimento

        StatoSala.aggiungiTavolo(self)

    def getInfoTavolo(self) -> dict:
        return {
            "riferimentoTavolo": self.riferimentoTavolo,
            "coperti": self.numeroCoperti,
            "libero": self.isLibero
        }


    def getIsLibero(self) -> bool:
        return (not self.isLibero and not self.getIsPrenotato())

    def getIsPrenotato(self) -> bool:
        prenotazioni=StatoSala.getListaPrenotazioni()
        if (not prenotazioni == None):
            now = datetime.datetime.now()
            for prenotazione in prenotazioni:
                tavoloprenotato=prenotazione.getRiferimentoTavolo()
                dataprenotazione= prenotazione.dataPrenotazione
                diff = ( dataprenotazione-now)
                if tavoloprenotato == self.riferimentoTavolo and (diff.total_seconds()/3600 < 4):
                    return True
        return False

    def getNumeroCoperti(self) -> int:
        return self.numeroCoperti

    def getNumeroPosti(self) -> int:
        return self.numeroPosti

    def getRiferimentoTavolo(self) -> int:
        return self.riferimentoTavolo

    def setRiferimentoTavolo(self, riferimento):
        self.riferimentoTavolo = riferimento

    def setIsLibero(self, tavoloLibero : bool):
        self.isLibero=tavoloLibero

    def setNumeroCoperti(self, numeroCoperti: int):
        self.numeroCoperti = numeroCoperti

    def setNumeroPosti(self, numeroPosti : int):
        self.numeroPosti=numeroPosti

    def getStato(self):
        if(not self.isLibero):
            return StatoTavolo.OCCUPATO
        elif(self.getIsPrenotato()):
            return StatoTavolo.PRENOTATO
        return StatoTavolo.UTILIZZABILE
