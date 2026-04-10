#Il responsabile vuole uno strumento che, dato il nome di un allergene, mostri immediatamente quali piatti singoli e quali menu tipici un cliente non può ordinare. Per ora l’allergia viene inserita da tastiera: in futuro verrà passata come argomento da terminale.

with open("menu_sakura.json", "r") as file:
    piatti = file.readlines()

    for riga in piatti:
        piatto = riga.strip()   # .strip() rimuove \n e spazi
        if piatto:              # salta righe vuote
            print(f"piatto: {piatto} ")
    print("\n ") 
