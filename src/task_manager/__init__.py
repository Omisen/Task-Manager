from taskmanager import TaskManager
from task import Task

def mostra_menu() -> None:
    menu = """
Gestore Attività - Menu
1) Aggiungi attività
2) Mostra tutte le attività
3) Mostra solo non completate
4) Completa / togli completamento attività
5) Rimuovi attività
6) Modifica attività
7) Cerca attività
8) Esci
"""
    print(menu)

def gestione_input(tm: TaskManager) -> None:
    # Loop principale che legge l'input dell'utente e agisce sul TaskManager.
    # tm: istanza di TaskManager sulla quale operare.
    while True:
        mostra_menu()
        match scelta := input("Seleziona un'opzione (1-8): ").strip():
            
            case "1":
                titolo = input("Titolo: ").strip()
                descrizione = input("Descrizione (opzionale): ").strip()
                if titolo:
                    tm.addTask(Task(titolo, descrizione))
                    print("Attività aggiunta.")
                else:
                    print("Il titolo non può essere vuoto. Operazione annullata.")

            case "2":
                if not tm.task_list:
                    print("Nessuna attività presente.")
                else:
                    for i, t in enumerate(tm.task_list):
                        # status = "✅" if getattr(t, '_completato', False) else "❌"
                        # print(f"[{i}] {t.titolo} - {t.descrizione} {status}")
                        print(f"[{i}] {t}")

            case "3":
                non_comp = [ (i,t) for i,t in enumerate(tm.task_list) if not getattr(t, '_completato', False) ]
                if not non_comp:
                    print("Nessuna attività non completata.")
                else:
                    for i, t in non_comp:
                        print(f"[{i}] {t.titolo} - {t.descrizione}")

            case "4":
                idx = input("Indice attività da (s)toggle: ").strip()
                try:
                    idx = int(idx)
                    if 0 <= idx < len(tm.task_list):
                        tm.completa(idx)
                        print("Stato completamento invertito.")
                    else:
                        print("Indice fuori intervallo.")
                except ValueError:
                    print("Indice non valido.")

            case "5":
                idx = input("Indice attività da rimuovere: ").strip()
                try:
                    idx = int(idx)
                    if 0 <= idx < len(tm.task_list):
                        tm.revoveTask(idx)
                        print("Attività rimossa.")
                    else:
                        print("Indice fuori intervallo.")
                except ValueError:
                    print("Indice non valido.")

            case "6":
                idx = input("Indice attività da modificare: ").strip()
                try:
                    idx = int(idx)
                    if 0 <= idx < len(tm.task_list):
                        new_tit = input("Nuovo titolo (lascia vuoto per non modificare): ").strip()
                        new_desc = input("Nuova descrizione (lascia vuoto per non modificare): ").strip()
                        if new_tit:
                            tm.task_list[idx].titolo = new_tit
                        if new_desc:
                            tm.task_list[idx].descrizione = new_desc
                        print("Attività aggiornata.")
                    else:
                        print("Indice fuori intervallo.")
                except ValueError:
                    print("Indice non valido.")

            case "7":
                parola_chiave = input("Parola chiave di ricerca: ").strip()
                if not parola_chiave:
                    print("Parola chiave vuota.")
                else:
                    risultati = tm.cerca(parola_chiave)
                    if not risultati:
                        print("Nessuna attività trovata.")
                    else:
                        for t in risultati:
                            status = "✅" if getattr(t, '_completato', False) else "❌"
                            print(f"{t.titolo} - {t.descrizione} {status}")

            case "8":
                print("Uscita.")
                break

            case _:
                print("Opzione non valida. Riprova.")

        input("Premi Invio per continuare...")



def main() -> None:
    tm = TaskManager()
    try:
        gestione_input(tm)
    except KeyboardInterrupt:
        print("\nInterruzione ricevuta. Uscita.")

def gestion_input(tm: TaskManager) -> None:
    return gestione_input(tm)

if __name__ == "__main__":
    main()