#region Imports
from datetime import datetime
#endregion

class Task:
    def __init__(self, titolo: str, descrizione: str = ""):
        self._titolo = titolo
        self._descrizione = descrizione
        self._completato = False
        self._data = datetime.today().date()
    
    #region Properties
    @property
    def titolo(self):
        return self._titolo
    
    @property
    def descrizione(self):
        return self._descrizione
    #endregion
    
    #region Setters
    @titolo.setter
    def titolo(self, value: str):
        self._titolo = value
        
    @descrizione.setter
    def descrizione(self, value: str):
        self._descrizione = value
    #endregion
        
    def toogle_completa(self) -> None:
        self._completato = not self._completato 
        
    def to_dict(self) -> dict:
        return {
            "titolo" : self._titolo,
            "dscrizione": self._descrizione,
            "completato": self._completato,
            "data": str(self._data)
        }
    
    def __str__(self) -> str:
        return f"[{self._titolo.upper()}]: {self._descrizione}\nCopletato: {"✅" if self._completato else "❌"}\n{self._data}\n"