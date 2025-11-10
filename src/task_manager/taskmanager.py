#region Imports
from task import Task
import re
#endregion

class TaskManager:
    def __init__(self, file_path: str = None):
        self.file_path = file_path
        self.task_list: list[Task] = []
        
    def addTask(self, task: Task) -> None:
        self.task_list.append(task)
    
    def revoveTask(self, index: int) -> Task:
        self.task_list.pop(index)
    
    def completa(self, index: int) -> None:
        self.task_list[index].toogle_completa()
    
    def modifica(self, index: int, titolo: str = None, descrizione: str = None) -> None:
        self.task_list[index].titolo = titolo
        self.task_list[index].descrizione = descrizione
    
    def mostra_tutte(self,solo_non_completate: bool = False) -> list[Task]:
        # return [task for task in self.task_list if task._completato == solo_non_completate]
        return list(filter(lambda task: task == solo_non_completate, self.task_list))
    
    def cerca(self, parola_chiave: str) -> list[Task]:
        # return list(filter(lambda task: re.search(parola_chiave, task.titolo, flags = re.IGNORECASE) or re.search(parola_chiave, task.descrizione, flags = re.IGNORECASE) ,self.task_list))
        return list(filter(lambda task: parola_chiave.lower() in task.titolo.lower() or parola_chiave.lower() in task.descrizione.lower(), self.task_list))  
    
    def salva_su_file(self) -> None:
        pass
    
    def carica_su_file(self) -> None:
        pass
    
    def to_dict(self) -> dict:
        return {task.to_dict() for task in self.task_list}