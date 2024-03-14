import networkx as nx
import matplotlib.pyplot as plt
import random
from pyswip import Prolog
import random
#-------------------------------------------------------------------------------------------#
#------------------------------------------INPUT DATI---------------------------------------#
#-------------------------------------------------------------------------------------------# 

def codice_random():
    # Valori ammissibili per ogni parte del codice
    valori_d = ["1015", "3025", "5030", "6060"]
    valori_k = ["004", "010", "050", "100"]
    valori_f = ["F", "N"]
    valori_x = ["P", "R", "D", "A"]
    valori_CAP = ['16010', '10010', '11010', '20001', '39010', '34010', '37010', '43010', 
                  '50012', '60010', '06010', '00010', '65010', '09012', '80010', '86010', 
                  '70056', '85010', '88020', '90010']

    # Combinazioni non ammesse
    combinazioni_non_ammesse = [
    "1015004FD", "1015004ND", "1015010FP", "1015010FD", "1015010NP", "1015010ND",
    "1015050FP", "1015050FR", "1015050FD", "1015050FA", "1015050NP", "1015050NR",
    "1015050ND", "1015050NA", "1015100FP", "1015100FR", "1015100FD", "1015100FA",
    "1015100NP", "1015100NR", "1015100ND", "1015100NA", "3025004FP", "3025004FD",
    "3025004NP", "3025010FP", "3025010NP", "3025050FP", "3025050NP", "3025100FP",
    "3025100FR", "3025100FD", "3025100FA", "3025100NP", "3025100NR", "3025100ND",
    "3025100NA", "5030004FP", "5030004FR", "5030004NP", "5030004NR", "5030010FP",
    "5030010FR", "5030010NP", "5030010NR", "5030050FP", "5030050FR", "5030050NP",
    "5030050NR", "5030100FP", "5030100FR", "5030100NP", "5030100NR", "6060004FP",
    "6060004FR", "6060004NP", "6060004NR", "6060010FP", "6060010FR", "6060010NP",
    "6060010NR", "6060050FP", "6060050FR", "6060050NP", "6060050NR", "6060100FP",
    "6060100FR", "6060100NP", "6060100NR"]

    valido = False
    while not valido:
        # Generazione casuale di ogni parte del codice
        d = random.choice(valori_d)
        k = random.choice(valori_k)
        f = random.choice(valori_f)
        x = random.choice(valori_x)
        cap = random.choice(valori_CAP)

        combinazione = d + k + f + x

        # Controlla se la combinazione è ammessa
        valido = combinazione not in combinazioni_non_ammesse

    # Creazione del dizionario con i valori generati
    risultati = {
        'd': d,
        'k': k,
        'f': f,
        'x': x,
        'cap': cap
    }
    return risultati

def estrai_valore(dizionario, chiave):
    # Verifica se la chiave è nel dizionario
    if chiave in dizionario:
        return dizionario[chiave]
    else:
        return "Chiave non trovata"

# Funzione per ottenere il valore appropriato
def ottieni_valore(lista, posizione, campo):
    try:
        elemento = lista[posizione]
        return elemento.get(campo)
    except IndexError:
        return None

#-------------------------------------------------------------------------------------------#
#----------------------------------ALGORITMO NAIVE BAYAS------------------------------------#
#-------------------------------------------------------------------------------------------# 

def ottieni_valore(chiave, scelta):
    frequenza = {
        "1015": [0.0714, 0.2580],  # Valori per D
        "3025": [0.1785, 0.3870],
        "5030": [0.25, 0.2903],
        "6060": [0.5, 0.0645],
        "004": [0.2142, 0.4193],   # Valori per K
        "010": [0.25, 0.3548],
        "050": [0.2857, 0.1935],
        "100": [0.25, 0.0322],
        "F": [0.75, 0.2580],     # Valori per F
        "N": [0.25, 0.7419],
        "P": [0, 0.0645],     # Valori per X
        "R": [0.1785, 0.1612],
        "D": [0.5357, 0.1935],
        "A": [0.2857, 0.5806]
    }
    if chiave in frequenza:
        if scelta == 'y':
            return frequenza[chiave][0]
        elif scelta == 'n':
            return frequenza[chiave][1]
        else:
            return "Scelta non valida. Inserire 'y' o 'n'."
    else:
        return "Chiave non trovata nel dizionario."
           
def calcola_rapporto(n1, n2, n3, n4, n5, n6, n7, n8):
    # Moltiplicazione dei primi quattro numeri
    primo_risultato = n1 * n2 * n3 * n4

    # Moltiplicazione degli ultimi quattro numeri
    secondo_risultato = n5 * n6 * n7 * n8

    # Calcolo del rapporto
    rapporto = primo_risultato / (primo_risultato + secondo_risultato)

    # Arrotonda a un massimo di 4 cifre decimali
    rapporto_arrotondato = round(rapporto, 4)

    return rapporto_arrotondato

#-------------------------------------------------------------------------------------------#
#-----------------------------------ALGORITMO MERGE SORT------------------------------------#
#-------------------------------------------------------------------------------------------# 

def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left_half = lista[:mid]
        right_half = lista[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i]['priorità'] > right_half[j]['priorità']: 
                lista[k] = left_half[i]
                i += 1
            else:
                lista[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lista[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lista[k] = right_half[j]
            j += 1
            k += 1

#-------------------------------------------------------------------------------------------#
#--------------------------------------CREAZIONE GRAFO--------------------------------------#
#-------------------------------------------------------------------------------------------#
def create_graph():
    G = nx.DiGraph()

    root_node = "Root"
    level1_nodes = [f"L1_{i}" for i in range(6)]
    level2_nodes = [f"L2_{i}" for i in range(6)]
    level3_nodes = ["NORD", "CENTRO", "SUD"]

    G.add_node(root_node)
    G.add_nodes_from(level1_nodes)
    G.add_nodes_from(level2_nodes)
    G.add_nodes_from(level3_nodes)

    for l1_node in level1_nodes:
        G.add_edge(root_node, l1_node, weight=1, usage_count=0)
        target_l3_node = level3_nodes[level1_nodes.index(l1_node) % 3]
        G.add_edge(l1_node, target_l3_node, weight=1, usage_count=0)
        target_l2_node = level2_nodes[level1_nodes.index(l1_node)]
        G.add_edge(l1_node, target_l2_node, weight=1, usage_count=0)

    for l2_node in level2_nodes:
        source_l1_node = level1_nodes[level2_nodes.index(l2_node)]
        linked_l3_node = next(G.successors(source_l1_node))
        unlinked_l3_nodes = [node for node in level3_nodes if node != linked_l3_node]
        for target_l3_node in unlinked_l3_nodes:
            G.add_edge(l2_node, target_l3_node, weight=1, usage_count=0)

    return G

def update_edge_weight(G, source, target):
    if G.has_edge(source, target):
        G[source][target]['usage_count'] += 1
        if G[source][target]['usage_count'] % 5 == 0:
            G[source][target]['weight'] += 1

def heuristic(G, node, goal):
    try:
        # Calcola il percorso più breve in termini di peso
        path = nx.shortest_path(G, source=node, target=goal, weight='weight')
        # Somma i pesi degli archi lungo il percorso
        return sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
    except nx.NetworkXNoPath:
        return float('inf')  # Restituisce infinito se non esiste un percorso

def cost(G, node, node_succ):
    if G.has_edge(node, node_succ):
        return G[node][node_succ]['weight']
    else:
        return float('inf')  # Restituisce infinito se non esiste un arco diretto

def neighbors(G, node):
    return list(G.successors(node))

def draw_graph(G):
    pos = {}
    root_node = "Root"
    level1_nodes = [f"L1_{i}" for i in range(6)]
    level2_nodes = [f"L2_{i}" for i in range(6)]
    level3_nodes = ["NORD", "CENTRO", "SUD"]

    # Posizione del nodo radice
    pos[root_node] = (0, 3)

    # Posizioni dei nodi di livello 1
    for i, node in enumerate(level1_nodes):
        pos[node] = (i - 2.5, 2)  # Distribuzione orizzontale

    # Posizioni dei nodi di livello 2
    for i, node in enumerate(level2_nodes):
        pos[node] = (i - 2.5, 1)  # Distribuzione orizzontale

    # Posizioni dei nodi di livello 3
    for i, node in enumerate(level3_nodes):
        pos[node] = (i - 1, 0)  # Distribuzione orizzontale

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color="skyblue")
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
    
#----------------------------------------------------------------------------------------------#
#--------------------------------------DIZIONARIO REGIONI--------------------------------------#
#----------------------------------------------------------------------------------------------#
def trova_regione(cap):
    dizionario_regioni = {
        "16010": "NORD",  # Genova
        "10010": "NORD",  # Torino
        "11010": "NORD",  # Aosta
        "20001": "NORD",  # Milano
        "39010": "NORD",  # Bolzano
        "34010": "NORD",  # Trieste
        "37010": "NORD",  # Verona
        "43010": "CENTRO", # Parma
        "50012": "CENTRO", # Firenze
        "60010": "CENTRO", # Ancona
        "06010": "CENTRO", # Perugia
        "00010": "CENTRO", # Roma
        "65010": "CENTRO", # Pescara
        "09012": "SUD",    # Cagliari
        "80010": "SUD",    # Napoli
        "86010": "SUD",    # Campobasso
        "70056": "SUD",    # Molfetta
        "85010": "SUD",    # Potenza
        "88020": "SUD",    # Catanzaro
        "90010": "SUD",    # Palermo
    }

    return dizionario_regioni.get(cap, "CAP non trovato")

#-------------------------------------------------------------------------------------------#
#--------------------------------------ALGORITMO IDA*---------------------------------------#
#-------------------------------------------------------------------------------------------#
def ida_star(G, root, goal):
   def search(path, g, bound):
       node = path[-1]
       f = g + heuristic(G, node, goal)
       if f > bound:
           return f
       if node == goal:
           return True
       min_bound = float('inf')
       for succ in neighbors(G, node):
           if succ not in path:
               path.append(succ)
               t = search(path, g + cost(G, node, succ), bound)
               if t == True:
                   return True
               if t < min_bound:
                   min_bound = t
               path.pop()
       return min_bound

   bound = heuristic(G, root, goal)
   path = [root]
   while True:
       t = search(path, 0, bound)
       if t == True:
           return path
       if t == float('inf'):
           return None
       bound = t
  
def update_weights_along_path(G, path):
    for i in range(len(path) - 1):
        source = path[i]
        target = path[i + 1]
        update_edge_weight(G, source, target)
  
#-------------------------------------------------------------------------------------------#
#---------------------------------SMISTAMENTO LV 1------------------------------------------#
#-------------------------------------------------------------------------------------------#

def distribuisci_dizionari(item, lista_nord, lista_centro, lista_sud):
    
    mappa_cap = {
        "16010": "NORD", "10010": "NORD", "11010": "NORD", "20001": "NORD", 
        "39010": "NORD", "34010": "NORD", "37010": "NORD", "43010": "CENTRO", 
        "50012": "CENTRO", "60010": "CENTRO", "06010": "CENTRO", "00010": "CENTRO", 
        "65010": "CENTRO", "09012": "SUD", "80010": "SUD", "86010": "SUD", 
        "70056": "SUD", "85010": "SUD", "88020": "SUD", "90010": "SUD"
    }

    cap = item.get("cap")
    regione = mappa_cap.get(cap)

    if regione == "NORD":
        lista_nord.append(item)
    elif regione == "CENTRO":
        lista_centro.append(item)
    elif regione == "SUD":
        lista_sud.append(item)    

#-------------------------------------------------------------------------------------------#
#---------------------------------SMISTAMENTO LV 2------------------------------------------#
#-------------------------------------------------------------------------------------------#

def distribuisci_regioni_nord(lista, lista_liguria, lista_piemonte, lista_valledaosta, lista_lombardia, lista_trentino, lista_friuli, lista_veneto):
    
    mappa_cap = {
        "16010": "Liguria", "10010": "Piemonte", "11010": "Valle d'Aosta", "20001": "Lombardia", 
        "39010": "Trentino Alto Adige", "34010": "Friuli Venezia Giulia", "37010": "Veneto"}
    for dizionario in lista:
        cap = dizionario.get("cap")
        regione = mappa_cap.get(cap)

        if regione == "Liguria":
            lista_liguria.append(dizionario)
        elif regione == "Piemonte":
            lista_piemonte.append(dizionario)
        elif regione == "Valle d'Aosta":
            lista_valledaosta.append(dizionario)
        elif regione == "Lombardia":
            lista_lombardia.append(dizionario)
        elif regione == "Trentino Alto Adige":
            lista_trentino.append(dizionario)
        elif regione == "Friuli Venezia Giulia":
            lista_friuli.append(dizionario)
        elif regione == "Veneto":
            lista_veneto.append(dizionario)            

def distribuisci_regioni_centro(lista, lista_emilia, lista_toscana, lista_marche, lista_umbria, lista_lazio, lista_abruzzo):
    
    mappa_cap = {
        "43010": "Emilia Romagna", "50012": "Toscana", "60010": "Marche", "06010": "Umbria", "00010": "Lazio", "65010": "Abruzzo"}
    for dizionario in lista:
        cap = dizionario.get("cap")
        regione = mappa_cap.get(cap)

        if regione == "Emilia Romagna":
            lista_emilia.append(dizionario)
        elif regione == "Toscana":
            lista_toscana.append(dizionario)
        elif regione == "Marche":
            lista_marche.append(dizionario)
        elif regione == "Umbria":
            lista_umbria.append(dizionario)
        elif regione == "Lazio":
            lista_lazio.append(dizionario)
        elif regione == "Abruzzo":
            lista_abruzzo.append(dizionario) 
  
def distribuisci_regioni_sud(lista, lista_sardegna, lista_campania, lista_molise, lista_puglia, lista_basilicata, lista_calabria, lista_sicilia):
    
    mappa_cap = {"09012": "Sardegna", "80010": "Campania", "86010": "Molise", "70056": "Puglia", "85010": "Basilicata", "88020": "Calabria", "90010": "Sicilia"}
    for dizionario in lista:
        cap = dizionario.get("cap")
        regione = mappa_cap.get(cap)

        if regione == "Sardegna":
            lista_sardegna.append(dizionario)
        elif regione == "Campania":
            lista_campania.append(dizionario)
        elif regione == "Molise":
            lista_molise.append(dizionario)
        elif regione == "Puglia":
            lista_puglia.append(dizionario)
        elif regione == "Basilicata":
            lista_basilicata.append(dizionario)
        elif regione == "Calabria":
            lista_calabria.append(dizionario)
        elif regione == "Sicilia":
            lista_sicilia.append(dizionario) 

#-------------------------------------------------------------------------------------------#
#--------------------------------------CSP Solver-------------------------------------------#
#-------------------------------------------------------------------------------------------#   

def convertitore_dizionario(dizionario):
    # Imposta il valore per 'f'
    if dizionario['f'] == 'F':
        valore_f = 'si'
    elif dizionario['f'] == 'N':
        valore_f = 'no'
    else:
        valore_f = 'indefinito'  # O un altro valore di default se 'f' non è né 'F' né 'N'
    # Crea la stringa di output
    output = {"id": dizionario['id'], "peso": dizionario['k'], "fragile": valore_f}
    return output
    
def rimuovi_elemento_con_id(lista, id_da_rimuovere):
    elemento_da_rimuovere = None

    # Assicurati che l'ID da rimuovere sia un numero (int)
    id_da_rimuovere = int(id_da_rimuovere)

    # Cerca l'elemento con l'ID specificato
    for elemento in lista:
        if int(elemento['id']) == id_da_rimuovere:
            elemento_da_rimuovere = elemento
            break

    # Se l'elemento è stato trovato, rimuovilo dalla lista
    if elemento_da_rimuovere:
        lista.remove(elemento_da_rimuovere)
    else:
        print(f"Nessun elemento con ID {id_da_rimuovere} trovato nella lista.")

def impila_pacchi(pacchi):
    prolog = Prolog()
    
    # Rimuove tutti i fatti 'pacco', 'fragile', 'tutti_fragili', 'pacco_base' esistenti per evitare conflitti di stato
    prolog.retractall("pacco(_,_,_)")
    prolog.retractall("fragile(_)")
    prolog.retractall("tutti_fragili")
    prolog.retractall("pacco_base(_,_,_)")
    
    # Definizione dei fatti dei pacchi
    for pacco in pacchi:
        prolog.assertz(f"pacco({pacco['id']}, {pacco['peso']}, '{pacco['fragile']}')")

    # Definizione delle regole

    # Regola per considerare un pacco fragile se pesa meno di 50 o è marcato come fragile
    prolog.assertz("fragile(ID) :- pacco(ID, Peso, 'si')")
    prolog.assertz("fragile(ID) :- pacco(ID, Peso, _), Peso < 50")

    # Regola per verificare se tutti i pacchi sono fragili
    prolog.assertz("tutti_fragili :- \+ (pacco(ID, _, _), \+ fragile(ID))")

    # Regola per trovare il pacco base tenendo conto della fragilità
    prolog.assertz("pacco_base(ID, Peso, Fragile) :- pacco(ID, Peso, Fragile), (tutti_fragili; \+ fragile(ID)), \+ (pacco(_, P2, _), P2 > Peso, (tutti_fragili; \+ fragile(_)))")

    # Query per trovare il pacco base
    pacco_base = list(prolog.query("pacco_base(ID, Peso, Fragile)"))

    return pacco_base[0] if pacco_base else None

#-------------------------------------------------------------------------------------------#
#----------------------------------Riempimento furgone--------------------------------------#
#-------------------------------------------------------------------------------------------#  
 
def gestisci_pacchi_modificato(regione, lista_regionale, furgone, pila, capienza_furgone):
    output = ""
    if len(lista_regionale) >= capienza_furgone * 3:
        for i in range(capienza_furgone):
            pacchi = []
            dizionario_appoggio = []

            for j in range(min(3, len(lista_regionale))):
                pacco = convertitore_dizionario(lista_regionale[j])
                pacchi.append(pacco)
                furgone.append(lista_regionale[j])

            lista_regionale = lista_regionale[3:]

            for j in range(min(3, len(pacchi))):
                pacco_base = impila_pacchi(pacchi)
                dizionario_appoggio.append(pacco_base)
                rimuovi_elemento_con_id(pacchi, pacco_base['ID'])

            pila.append(dizionario_appoggio)

        output += f"\nFurgone {regione}\n"
        for i in range(len(pila)):
            output += f"Pila {i + 1}:\n"
            for pacco in pila[i]:
                output += f"{pacco}\n"
    else:
        output += f"\nCi sono {len(lista_regionale)} pacchi in attesa di essere processati in {regione}\n"
    
    return output

#-------------------------------------------------------------------------------------------#
#-----------------------------------------Output--------------------------------------------#
#-------------------------------------------------------------------------------------------#  

nomi = ["Giulia", "Luca", "Maria", "Giovanni", "Francesca", "Marco", "Chiara", "Matteo", "Sara", "Andrea"]
cognomi = ["Rossi", "Ferrari", "Bianchi", "Ricci", "Gallo", "Conti", "De Luca", "Costa", "Bruno", "Romano"]
vie = ["Via Roma", "Corso Italia", "Via Milano", "Viale Regina Margherita", "Corso Garibaldi", "Viale Europa", "Via Torino", "Corso Vittorio Emanuele", "Via Dante", "Viale Kennedy"]

def generatore_persone(num_elementi):
    lista = []
    for i in range(num_elementi):
        id = i
        nome = random.choice(nomi)
        cognome = random.choice(cognomi)
        via = random.choice(vie)
        numero_civico = random.randint(1, 100)
        lista.append((id, nome, cognome, via, numero_civico))
    return lista

def stampa_lista_per_riga(lista):
    for elemento in lista:
        print(elemento)

#stampa per la gui       
def stampa_riga(lista):
    risultato = ""
    for elemento in lista:
        dettagli = f"ID: {elemento['id']}, Dimensioni: {elemento['d']}, Peso: {elemento['k']}, Fragilità: {elemento['f']}, Tipologia di spedizione: {elemento['x']}, CAP: {elemento['cap']}, Priorità: {elemento['priorità']}\n"
        risultato += dettagli
    return risultato


#lista_appoggio = generatore_persone(100)
#modificata per la gui
def stampa_pacco(lista, lista_persone, id_pacco):
    # Verifica che l'ID sia valido
    if id_pacco >= 0 and id_pacco < len(lista) and id_pacco < len(lista_persone):
        persona = lista_persone[id_pacco]
        pacco = lista[id_pacco]

        # Formatta i dettagli della persona
        dettagli_persona = f"ID Persona: {persona[0]}, Nome: {persona[1]}, Cognome: {persona[2]}, Via: {persona[3]}, Civico: {persona[4]}, "

        # Formatta i dettagli del pacco
        dettagli_pacco = f"Dimensioni: {pacco['d']}, Peso: {pacco['k']}, Fragilità: {pacco['f']}, Spedizione: {pacco['x']}, CAP: {pacco['cap']}, Priorità: {pacco['priorità']}\n"

        return dettagli_persona + dettagli_pacco
    else:
        return "ID non valido o fuori range."


def print_path(path):
    for i, node in enumerate(path):
        if i == 0:
            # Stampa l'ID all'interno delle parentesi quadre
            print(f"[ID {node}]", end=' ')
        else:
            # Aggiungi '->' davanti a tutti gli elementi tranne il primo
            print('->', end=' ')

            if isinstance(node, list):
                # Stampa gli elementi della lista separati da ' -> '
                print(' -> '.join(node), end=' ')
            else:
                print(node, end=' ')
                
def percorso_pacco(id, lista):
    for item in lista:
        if isinstance(item, (list, tuple)) and len(item) > 0:
            if id == item[0]:
                print_path(item)
                
def filtra_lista(lista, chiave, valore):
    lista_appoggio = []
    for item in lista:
        if valore == estrai_valore(item, chiave):
            lista_appoggio.append(item)
    return lista_appoggio