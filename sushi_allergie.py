import json

# --- Caricamento dati ---
with open("menu_sakura.json", "r", encoding="utf-8") as f:
    data = json.load(f)

piatti = data["piatti"]
menu_tipici = data["menu_tipici"]


# --- Funzioni base ---
def piatti_con_allergene(allergene):
    risultato = []
    for p in piatti:
        if allergene in p["allergeni"]:
            risultato.append(p)
    return risultato


def menu_con_allergene(allergene):
    menu_non_permessi = []

    for m in menu_tipici:
        for pid in m["composizione"]:
            piatto = next((p for p in piatti if p["id"] == pid), None)
            
            if piatto and allergene in piatto["allergeni"]:
                menu_non_permessi.append(m)
                break  # basta un piatto per escludere il menu

    return menu_non_permessi


# --- Input utente ---
allergene = input("Inserisci allergene: ").strip().lower()


# --- Logica ---
piatti_vietati = piatti_con_allergene(allergene)
menu_vietati = menu_con_allergene(allergene)


# --- Output ---
print("\n🚫 PIATTI NON CONSENTITI:")
if piatti_vietati:
    for p in piatti_vietati:
        print(f"- {p['nome']} ({p['categoria']})")
else:
    print("Nessun piatto contiene questo allergene.")

print("\n🚫 MENU NON ORDINABILI:")
if menu_vietati:
    for m in menu_vietati:
        print(f"- {m['nome']}")
else:
    print("Tutti i menu sono sicuri.")