import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout, QWidget, QListWidget, QLineEdit, QLabel, QGraphicsView, QGraphicsScene
import core as hub
import copy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import networkx as nx
import core

def draw_graph(G):
    fig = plt.figure(figsize=(10, 5))
    pos = {
        "Root": (0, 3),
        "L1_0": (-2.5, 2), "L1_1": (-1.5, 2), "L1_2": (-0.5, 2), 
        "L1_3": (0.5, 2), "L1_4": (1.5, 2), "L1_5": (2.5, 2),
        "L2_0": (-2.5, 1), "L2_1": (-1.5, 1), "L2_2": (-0.5, 1),
        "L2_3": (0.5, 1), "L2_4": (1.5, 1), "L2_5": (2.5, 1),
        "NORD": (-1, 0), "CENTRO": (0, 0), "SUD": (1, 0)
    }
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color="skyblue")
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    return fig

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Postal Hub")
        self.G = hub.create_graph()
        self.create_widgets() 
        
        self.output_area.installEventFilter(self) 


    #ciclo di vita del programma, permette di monitorare il flusso ed eventuali errori
    def eventFilter(self, source, event):
        if source == self.output_area:
            print(f"Evento: {event.type()}, Source: {source}")
        return super(MainApp, self).eventFilter(source, event)


    def start_main_app(self):
        n_pacchi = None
        capienza_furgone = None

        if self.num_pacchi_input.text().isdigit():
            n_pacchi = int(self.num_pacchi_input.text())

        if self.capienza_furgone_input.text().isdigit():
            capienza_furgone = int(self.capienza_furgone_input.text())

        if n_pacchi is not None and capienza_furgone is not None:
            # Il codice da eseguire se entrambi i valori sono non nulli
            self.initialize_data(n_pacchi, capienza_furgone)
        else:
            # Crea un'istanza di QMessageBox
            msg_box = QMessageBox()

            # Imposta il tipo di messaggio
            msg_box.setIcon(QMessageBox.Critical)

            # Imposta il testo del messaggio
            msg_box.setText("Attenzione! \n Per favore, riempi entrambi i campi 'Numero di pacchi' e 'Capienza del furgone' e premi 'Conferma' prima di procedere.")

            # Imposta il testo del pulsante di chiusura
            msg_box.setStandardButtons(QMessageBox.Ok)

            # Mostra il messaggio
            msg_box.exec_()
            return
        
        output_text = ""
        output_text += hub.gestisci_pacchi_modificato("Liguria", self.lista_liguria, self.furgone_liguria, self.pila_liguria, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Piemonte", self.lista_piemonte, self.furgone_piemonte, self.pila_piemonte, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Valle d'Aosta", self.lista_valledaosta, self.furgone_valledaosta, self.pila_valledaosta, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Lombardia", self.lista_lombardia, self.furgone_lombardia, self.pila_lombardia, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Trentino-Alto Adige", self.lista_trentino, self.furgone_trentino, self.pila_trentino, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Friuli-Venezia Giulia", self.lista_friuli, self.furgone_friuli, self.pila_friuli, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Veneto", self.lista_veneto, self.furgone_veneto, self.pila_veneto, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Emilia-Romagna", self.lista_emilia, self.furgone_emilia, self.pila_emilia, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Toscana", self.lista_toscana, self.furgone_toscana, self.pila_toscana, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Marche", self.lista_marche, self.furgone_marche, self.pila_marche, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Umbria", self.lista_umbria, self.furgone_umbria, self.pila_umbria, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Lazio", self.lista_lazio, self.furgone_lazio, self.pila_lazio, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Abruzzo", self.lista_abruzzo, self.furgone_abruzzo, self.pila_abruzzo, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Molise", self.lista_molise, self.furgone_molise, self.pila_molise, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Campania", self.lista_campania, self.furgone_campania, self.pila_campania, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Basilicata", self.lista_basilicata, self.furgone_basilicata, self.pila_basilicata, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Puglia", self.lista_puglia, self.furgone_puglia, self.pila_puglia, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Calabria", self.lista_calabria, self.furgone_calabria, self.pila_calabria, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Sicilia", self.lista_sicilia, self.furgone_sicilia, self.pila_sicilia, capienza_furgone)
        output_text += hub.gestisci_pacchi_modificato("Sardegna", self.lista_sardegna, self.furgone_sardegna, self.pila_sardegna, capienza_furgone)

        self.update_output_area(output_text)

    def update_output_area(self, text):
            self.output_area.setText(text)
            self.layout().activate()  # Forza l'aggiornamento del layout
            self.output_area.update()


    def initialize_data(self, n_pacchi, capienza_furgone):
        # Numero di pacchi e capienza del furgone
        #n_pacchi = 400
        #capienza_furgone = 6

        self.lista_persone = hub.generatore_persone(n_pacchi)

        # Liste varie
        self.listaPrioritaria = []
        self.lista = []
        self.lista_path = []
        self.nord = [] 
        self.centro = [] 
        self.sud = [] 

        # Liste di dizionari regionali
        self.lista_liguria = []
        self.lista_piemonte = []
        self.lista_valledaosta = []
        self.lista_lombardia = []
        self.lista_trentino = []
        self.lista_friuli = []
        self.lista_veneto = []
        self.lista_emilia = []
        self.lista_toscana = []
        self.lista_marche = []
        self.lista_umbria = []
        self.lista_lazio = []
        self.lista_abruzzo = []
        self.lista_molise = []
        self.lista_campania = []
        self.lista_basilicata = []
        self.lista_puglia = []
        self.lista_calabria = []
        self.lista_sicilia = []
        self.lista_sardegna = []

        # Liste di dizionari nei furgoni regionali
        self.furgone_liguria = []
        self.furgone_piemonte = []
        self.furgone_valledaosta = []
        self.furgone_lombardia = []
        self.furgone_trentino = []
        self.furgone_friuli = []
        self.furgone_veneto = []
        self.furgone_emilia = []
        self.furgone_toscana = []
        self.furgone_marche = []
        self.furgone_umbria = []
        self.furgone_lazio = []
        self.furgone_abruzzo = []
        self.furgone_molise = []
        self.furgone_campania = []
        self.furgone_basilicata = []
        self.furgone_puglia = []
        self.furgone_calabria = []
        self.furgone_sicilia = []
        self.furgone_sardegna = []

        # Liste di pile contenenti ciscuna 3 pacchi in ordine di posizionamento nei furgoni regionali
        self.pila_liguria = []
        self.pila_piemonte = []
        self.pila_valledaosta = []
        self.pila_lombardia = []
        self.pila_trentino = []
        self.pila_friuli = []
        self.pila_veneto = []
        self.pila_emilia = []
        self.pila_toscana = []
        self.pila_marche = []
        self.pila_umbria = []
        self.pila_lazio = []
        self.pila_abruzzo = []
        self.pila_molise = []
        self.pila_campania = []
        self.pila_basilicata = []
        self.pila_puglia = []
        self.pila_calabria = []
        self.pila_sicilia = []
        self.pila_sardegna = []
              
        self.G = hub.create_graph()

        # Creazione pacchi con priorità
        for i in range(n_pacchi):
            try:
                risultati = hub.codice_random()

                risultato = hub.calcola_rapporto(
                    hub.ottieni_valore(risultati["d"], "y"), 
                    hub.ottieni_valore(risultati["k"], "y"), 
                    hub.ottieni_valore(risultati["f"], "y"), 
                    hub.ottieni_valore(risultati["x"], "y"), 
                    hub.ottieni_valore(risultati["d"], "n"), 
                    hub.ottieni_valore(risultati["k"], "n"), 
                    hub.ottieni_valore(risultati["f"], "n"), 
                    hub.ottieni_valore(risultati["x"], "n")
                )
                id_format = "{:03d}".format(i)

                nuovo_elemento = {
                    'id': id_format,  # id ora è una stringa con tre cifre
                    'd': hub.estrai_valore(risultati, "d"), 
                    'k': hub.estrai_valore(risultati, "k"), 
                    'f': hub.estrai_valore(risultati, "f"), 
                    'x': hub.estrai_valore(risultati, "x"), 
                    'cap': hub.estrai_valore(risultati, "cap"), 
                    'priorità': risultato
                }

                self.lista.append(nuovo_elemento)

            except Exception as e:
                print(f"Si è verificato un errore: {e}")

        self.listaPrioritaria = copy.deepcopy(self.lista)
        hub.merge_sort(self.listaPrioritaria)

        # Smistamento nelle varie aree geografiche tramite l'IDA*
        for item in self.listaPrioritaria:
            lista_appoggio = []
            path = hub.ida_star(self.G, "Root", hub.trova_regione(hub.estrai_valore(item, "cap")))   
            if path is not None:
                lista_appoggio.append(hub.estrai_valore(item, "id"))
                lista_appoggio.append(path)
                self.lista_path.append(lista_appoggio) 
                hub.update_weights_along_path(self.G, path)
                hub.distribuisci_dizionari(item, self.nord, self.centro, self.sud)
            else:
                print("Nessun percorso trovato")

        # Smistamento nelle varie regioni
        hub.distribuisci_regioni_nord(self.nord, self.lista_liguria, self.lista_piemonte, self.lista_valledaosta, self.lista_lombardia, self.lista_trentino, self.lista_friuli, self.lista_veneto)
        hub.distribuisci_regioni_centro(self.centro, self.lista_emilia, self.lista_toscana, self.lista_marche, self.lista_umbria, self.lista_lazio, self.lista_abruzzo)
        hub.distribuisci_regioni_sud(self.sud, self.lista_sardegna, self.lista_campania, self.lista_molise, self.lista_puglia, self.lista_basilicata, self.lista_calabria, self.lista_sicilia)

        self.show_graph()
        self.text_area.clear()


    def create_widgets(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principale orizzontale
        main_layout = QHBoxLayout(central_widget)

        # Layout per i componenti a sinistra (menu e input)
        left_layout = QVBoxLayout()
        self.num_pacchi_input = QLineEdit()
        self.capienza_furgone_input = QLineEdit()
        confirm_button = QPushButton("Conferma")
        left_layout.addWidget(QLabel("Numero di pacchi:"))
        left_layout.addWidget(self.num_pacchi_input)
        left_layout.addWidget(QLabel("Capienza del furgone:"))
        left_layout.addWidget(self.capienza_furgone_input)
        left_layout.addWidget(confirm_button)

        # Inizializzazione dei widget per il layout a sinistra
        self.menu = QListWidget()
        self.id_input = QLineEdit()
        self.search_button = QPushButton("Cerca Pacco")
        self.find_path_button = QPushButton("Trova Percorso")
        self.filter_key_input = QLineEdit()
        self.filter_value_input = QLineEdit()
        self.filter_search_button = QPushButton("Ricerca Filtrata")

        # Aggiunge gli elementi al layout a sinistra
        left_layout.addWidget(self.menu)
        left_layout.addWidget(QLabel("ID Pacco:"))
        left_layout.addWidget(self.id_input)
        left_layout.addWidget(self.search_button)
        left_layout.addWidget(self.find_path_button)
        left_layout.addWidget(QLabel("Ricerca filtrata:"))
        left_layout.addWidget(QLabel("dimensioni, peso, fragilità, spedizione, cap"))
        left_layout.addWidget(self.filter_key_input)
        left_layout.addWidget(QLabel("Valore da ricercare:"))
        left_layout.addWidget(self.filter_value_input)
        left_layout.addWidget(self.filter_search_button)

        # Layout per il grafico e l'area di output
        graph_output_layout = QVBoxLayout()
        self.graphView = QGraphicsView(self)
        self.output_area = QTextEdit()
        graph_output_layout.addWidget(self.graphView)
        graph_output_layout.addWidget(self.output_area)

        # Aggiunge i layout e i widget al layout principale
        main_layout.addLayout(left_layout, 1)
        self.text_area = QTextEdit()
        main_layout.addWidget(self.text_area, 2)
        main_layout.addLayout(graph_output_layout, 3)

        # Connette il pulsante di conferma al metodo di inizializzazione
        confirm_button.clicked.connect(self.start_main_app)

        # Imposta il layout principale sul widget centrale
        central_widget.setLayout(main_layout)

        # Connette gli eventi ai metodi corrispondenti
        self.search_button.clicked.connect(self.search_pacco)
        self.filter_search_button.clicked.connect(self.perform_filtered_search)
        self.menu.itemClicked.connect(self.on_select)
        self.find_path_button.clicked.connect(self.find_package_path)

        self.show_graph()

        # Aggiunge le opzioni al menu
        opzioni = [
            "lista ordinata per priorità",
            "lista ordinata per ID",
            "lista NORD",
            "lista CENTRO",
            "lista SUD",
            "lista Liguria",
            "lista Piemonte",
            "lista Valle d'Aosta",
            "lista Lombardia",
            "lista Trentino-Alto Adige",
            "lista Friuli-Venezia Giulia",
            "lista Veneto",
            "lista Emilia-Romagna",
            "lista Toscana",
            "lista Marche",
            "lista Umbria",
            "lista Lazio",
            "lista Abruzzo",
            "lista Molise",
            "lista Campania",
            "lista Basilicata",
            "lista Puglia",
            "lista Calabria",
            "lista Sicilia",
            "lista Sardegna",
            "furgone Liguria",
            "furgone Piemonte",
            "furgone Valle d'Aosta",
            "furgone Lombardia",
            "furgone Trentino-Alto Adige",
            "furgone Friuli-Venezia Giulia",
            "furgone Veneto",
            "furgone Emilia-Romagna",
            "furgone Toscana",
            "furgone Marche",
            "furgone Umbria",
            "furgone Lazio",
            "furgone Abruzzo",
            "furgone Molise",
            "furgone Campania",
            "furgone Basilicata",
            "furgone Puglia",
            "furgone Calabria",
            "furgone Sicilia",
            "furgone Sardegna",
        ]
        
        for opzione in opzioni:
            self.menu.addItem(opzione)

    # Funzioni per mostrare i dettagli della lista ordinata per priorità
    def show_lista_pr(self):
        self.text_area.clear()
        listaPrioritaria_dettagli = hub.stampa_riga(self.listaPrioritaria)
        self.text_area.setText(listaPrioritaria_dettagli)

    # Funzioni per mostrare i dettagli della lista ordinata per ID
    def show_lista_id(self):
        self.text_area.clear()
        lista_dettagli = hub.stampa_riga(self.lista)
        self.text_area.setText(lista_dettagli)

    # Funzioni per mostrare i dettagli delle liste dei pacchi per area geografica
    def show_lista_nord(self):
        self.text_area.clear()
        lista_nord_dettagli = hub.stampa_riga(self.nord)
        self.text_area.setText(lista_nord_dettagli)
        
    def show_lista_centro(self):
        self.text_area.clear()
        lista_centro_dettagli = hub.stampa_riga(self.centro)
        self.text_area.setText(lista_centro_dettagli)
        
    def show_lista_sud(self):
        self.text_area.clear()
        lista_sud_dettagli = hub.stampa_riga(self.sud)
        self.text_area.setText(lista_sud_dettagli)

    # Funzioni per mostrare i dettagli delle liste dei pacchi ogni regione
    def show_lista_liguria(self):
        self.text_area.clear()
        lista_liguria_dettagli = hub.stampa_riga(self.lista_liguria)
        self.text_area.setText(lista_liguria_dettagli)

    def show_lista_piemonte(self):
        self.text_area.clear()
        lista_piemonte_dettagli = hub.stampa_riga(self.lista_piemonte)
        self.text_area.setText(lista_piemonte_dettagli)

    def show_lista_valledaosta(self):
        self.text_area.clear()
        lista_valledaosta_dettagli = hub.stampa_riga(self.lista_valledaosta)
        self.text_area.setText(lista_valledaosta_dettagli)

    def show_lista_lombardia(self):
        self.text_area.clear()
        lista_lombardia_dettagli = hub.stampa_riga(self.lista_lombardia)
        self.text_area.setText(lista_lombardia_dettagli)

    def show_lista_trentino(self):
        self.text_area.clear()
        lista_trentino_dettagli = hub.stampa_riga(self.lista_trentino)
        self.text_area.setText(lista_trentino_dettagli)

    def show_lista_friuli(self):
        self.text_area.clear()
        lista_friuli_dettagli = hub.stampa_riga(self.lista_friuli)
        self.text_area.setText(lista_friuli_dettagli)

    def show_lista_veneto(self):
        self.text_area.clear()
        lista_veneto_dettagli = hub.stampa_riga(self.lista_veneto)
        self.text_area.setText(lista_veneto_dettagli)

    def show_lista_emilia(self):
        self.text_area.clear()
        lista_emilia_dettagli = hub.stampa_riga(self.lista_emilia)
        self.text_area.setText(lista_emilia_dettagli)

    def show_lista_toscana(self):
        self.text_area.clear()
        lista_toscana_dettagli = hub.stampa_riga(self.lista_toscana)
        self.text_area.setText(lista_toscana_dettagli)

    def show_lista_marche(self):
        self.text_area.clear()
        lista_marche_dettagli = hub.stampa_riga(self.lista_marche)
        self.text_area.setText(lista_marche_dettagli)

    def show_lista_umbria(self):
        self.text_area.clear()
        lista_umbria_dettagli = hub.stampa_riga(self.lista_umbria)
        self.text_area.setText(lista_umbria_dettagli)

    def show_lista_lazio(self):
        self.text_area.clear()
        lista_lazio_dettagli = hub.stampa_riga(self.lista_lazio)
        self.text_area.setText(lista_lazio_dettagli)

    def show_lista_abruzzo(self):
        self.text_area.clear()
        lista_abruzzo_dettagli = hub.stampa_riga(self.lista_abruzzo)
        self.text_area.setText(lista_abruzzo_dettagli)

    def show_lista_molise(self):
        self.text_area.clear()
        lista_molise_dettagli = hub.stampa_riga(self.lista_molise)
        self.text_area.setText(lista_molise_dettagli)

    def show_lista_campania(self):
        self.text_area.clear()
        lista_campania_dettagli = hub.stampa_riga(self.lista_campania)
        self.text_area.setText(lista_campania_dettagli)

    def show_lista_basilicata(self):
        self.text_area.clear()
        lista_basilicata_dettagli = hub.stampa_riga(self.lista_basilicata)
        self.text_area.setText(lista_basilicata_dettagli)

    def show_lista_puglia(self):
        self.text_area.clear()
        lista_puglia_dettagli = hub.stampa_riga(self.lista_puglia)
        self.text_area.setText(lista_puglia_dettagli)

    def show_lista_calabria(self):
        self.text_area.clear()
        lista_calabria_dettagli = hub.stampa_riga(self.lista_calabria)
        self.text_area.setText(lista_calabria_dettagli)

    def show_lista_sicilia(self):
        self.text_area.clear()
        lista_sicilia_dettagli = hub.stampa_riga(self.lista_sicilia)
        self.text_area.setText(lista_sicilia_dettagli)

    def show_lista_sardegna(self):
        self.text_area.clear()
        lista_sardegna_dettagli = hub.stampa_riga(self.lista_sardegna)
        self.text_area.setText(lista_sardegna_dettagli)


    # Funzioni per mostrare i dettagli dei furgoni per ogni regione
    def show_furgone_liguria(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_liguria)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_piemonte(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_piemonte)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_valledaosta(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_valledaosta)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_lombardia(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_lombardia)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_trentino(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_trentino)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_friuli(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_friuli)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_veneto(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_veneto)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_emilia(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_emilia)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_toscana(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_toscana)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_marche(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_marche)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_umbria(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_umbria)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_lazio(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_lazio)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_abruzzo(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_abruzzo)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_molise(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_molise)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_campania(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_campania)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_basilicata(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_basilicata)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_puglia(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_puglia)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_calabria(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_calabria)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_sicilia(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_sicilia)
        self.text_area.setText(dettagli_furgone)

    def show_furgone_sardegna(self):
        self.text_area.clear()
        dettagli_furgone = hub.stampa_riga(self.furgone_sardegna)
        self.text_area.setText(dettagli_furgone)

    def search_pacco(self):
        package_id = self.id_input.text()

        if len(package_id) == 0:
            # Crea un'istanza di QMessageBox
            msg_box = QMessageBox()

            # Imposta il tipo di messaggio
            msg_box.setIcon(QMessageBox.Critical)

            # Imposta il testo del messaggio
            msg_box.setText("Attenzione! \n Per favore, riempi entrambi i campi 'ID Pacco' e premi 'Conferma' prima di procedere.")

            # Imposta il testo del pulsante di chiusura
            msg_box.setStandardButtons(QMessageBox.Ok)

            # Mostra il messaggio
            msg_box.exec_()
            return
        else:
            for i, item in enumerate(self.lista):
                if item['id'] == package_id:
                    output = hub.stampa_pacco(self.lista, self.lista_persone, i)  
                    self.text_area.setText(output)
                    return
            self.text_area.setText(f"Pacco {package_id} non trovato.")

    def find_package_path(self):
            # Ottiene l'ID del pacco dall'input dell'utente
            package_id = self.id_input.text()
            if len(package_id) == 0:
                # Crea un'istanza di QMessageBox
                msg_box = QMessageBox()

                # Imposta il tipo di messaggio
                msg_box.setIcon(QMessageBox.Critical)

                # Imposta il testo del messaggio
                msg_box.setText("Attenzione! \n Per favore, riempi entrambi i campi 'ID Pacco' e premi 'Conferma' prima di procedere.")

                # Imposta il testo del pulsante di chiusura
                msg_box.setStandardButtons(QMessageBox.Ok)

                # Mostra il messaggio
                msg_box.exec_()
                return

            # Trova il percorso del pacco
            for item in self.lista_path:
                if item[0] == package_id:
                    path_str = " -> ".join(item[1])
                    self.text_area.setText(f"Percorso del pacco con ID: {package_id}: {path_str}")
                    return
            
            # Se il pacco non viene trovato
            self.text_area.setText(f"Percorso non trovato per il pacco {package_id}")
    
    def show_graph(self):
        if self.G.number_of_nodes() > 0:
            fig = draw_graph(self.G)
            canvas = FigureCanvas(fig)
            scene = QGraphicsScene()
            scene.addWidget(canvas)
            self.graphView.setScene(scene)
            self.graphView.show()

    def perform_filtered_search(self):
        # Ottiene i valori di input per la chiave e il valore del filtro
        filter_key = self.filter_key_input.text()
        filter_value = self.filter_value_input.text()
        if len(filter_key) == 0 or len(filter_value) == 0:
            # Crea un'istanza di QMessageBox
            msg_box = QMessageBox()

            # Imposta il tipo di messaggio
            msg_box.setIcon(QMessageBox.Critical)

            # Imposta il testo del messaggio
            msg_box.setText("Attenzione! \n Per favore, riempi entrambi i campi per effettuare la ricerca filtrata.")

            # Imposta il testo del pulsante di chiusura
            msg_box.setStandardButtons(QMessageBox.Ok)

            # Mostra il messaggio
            msg_box.exec_()
            return
        

        if filter_key == 'Dimensioni' or filter_key == 'dimensioni':
            filter_key = 'd'
        elif filter_key == 'Peso' or filter_key == 'peso':
            filter_key = 'k'
        elif filter_key == 'Fragilità' or filter_key == 'fragilità':
            filter_key = 'f'
        elif filter_key == 'Spedizione' or filter_key == 'spedizione':
            filter_key = 'x'            
        elif filter_key == 'CAP' or filter_key == 'cap':
            filter_key = 'cap'     
        elif filter_key == 'Priorità' or filter_key == 'priorità':
            filter_key = 'priorità'
      
        # Esegue il filtraggio sulla lista dei pacchi
        filtered_list = core.filtra_lista(self.lista, filter_key, filter_value)

        # Visualizza i risultati nel text_area
        self.text_area.clear()  # Pulisce l'area di testo prima di aggiungere nuovi risultati
        for item in filtered_list:
            self.text_area.append(f"ID: {item['id']}, Dimensioni: {item['d']}, Peso: {item['k']}, Fragilità: {item['f']}, Tipologia di spedizione: {item['x']}, CAP: {item['cap']}, Priorità: {item['priorità']}")

    def on_select(self, item):
        try:
            if item.text() == "stampa grafo con pesi":
                self.show_graph()
            elif item.text() == "percorso di un determinato pacco":
                self.find_package_path()

            elif item.text() == "lista ordinata per priorità":
                self.show_lista_pr()

            elif item.text() == "lista ordinata per ID":
                self.show_lista_id()

            elif item.text() == "lista NORD":
                self.show_lista_nord()
            elif item.text() == "lista CENTRO":
                self.show_lista_centro()
            elif item.text() == "lista SUD":
                self.show_lista_sud()
                
            elif item.text() == "lista Liguria":
                self.show_lista_liguria()
            elif item.text() == "lista Piemonte":
                self.show_lista_piemonte()
            elif item.text() == "lista Valle d'Aosta":
                self.show_lista_valledaosta()
            elif item.text() == "lista Lombardia":
                self.show_lista_lombardia()
            elif item.text() == "lista Trentino-Alto Adige":
                self.show_lista_trentino()
            elif item.text() == "lista Friuli-Venezia Giulia":
                self.show_lista_friuli()
            elif item.text() == "lista Veneto":
                self.show_lista_veneto()
            elif item.text() == "lista Emilia-Romagna":
                self.show_lista_emilia()
            elif item.text() == "lista Toscana":
                self.show_lista_toscana()
            elif item.text() == "lista Marche":
                self.show_lista_marche()
            elif item.text() == "lista Umbria":
                self.show_lista_umbria()
            elif item.text() == "lista Lazio":
                self.show_lista_lazio()
            elif item.text() == "lista Abruzzo":
                self.show_lista_abruzzo()
            elif item.text() == "lista Molise":
                self.show_lista_molise()
            elif item.text() == "lista Campania":
                self.show_lista_campania()
            elif item.text() == "lista Basilicata":
                self.show_lista_basilicata()
            elif item.text() == "lista Puglia":
                self.show_lista_puglia()
            elif item.text() == "lista Calabria":
                self.show_lista_calabria()
            elif item.text() == "lista Sicilia":
                self.show_lista_sicilia()
            elif item.text() == "lista Sardegna":
                self.show_lista_sardegna()
            
            elif item.text() == "furgone Liguria":
                self.show_furgone_liguria()
            elif item.text() == "furgone Piemonte":
                self.show_furgone_piemonte()
            elif item.text() == "furgone Valle d'Aosta":
                self.show_furgone_valledaosta()
            elif item.text() == "furgone Lombardia":
                self.show_furgone_lombardia()
            elif item.text() == "furgone Trentino-Alto Adige":
                self.show_furgone_trentino()
            elif item.text() == "furgone Friuli-Venezia Giulia":
                self.show_furgone_friuli()
            elif item.text() == "furgone Veneto":
                self.show_furgone_veneto()
            elif item.text() == "furgone Emilia-Romagna":
                self.show_furgone_emilia()
            elif item.text() == "furgone Toscana":
                self.show_furgone_toscana()
            elif item.text() == "furgone Marche":
                self.show_furgone_marche()
            elif item.text() == "furgone Umbria":
                self.show_furgone_umbria()
            elif item.text() == "furgone Lazio":
                self.show_furgone_lazio()
            elif item.text() == "furgone Abruzzo":
                self.show_furgone_abruzzo()
            elif item.text() == "furgone Molise":
                self.show_furgone_molise()
            elif item.text() == "furgone Campania":
                self.show_furgone_campania()
            elif item.text() == "furgone Basilicata":
                self.show_furgone_basilicata()
            elif item.text() == "furgone Puglia":
                self.show_furgone_puglia()
            elif item.text() == "furgone Calabria":
                self.show_furgone_calabria()
            elif item.text() == "furgone Sicilia":
                self.show_furgone_sicilia()
            elif item.text() == "furgone Sardegna":
                self.show_furgone_sardegna()
        except:
            # Crea un'istanza di QMessageBox
            msg_box = QMessageBox()

            # Imposta il tipo di messaggio
            msg_box.setIcon(QMessageBox.Critical)

            # Imposta il testo del messaggio
            msg_box.setText("Attenzione! \n Per favore, riempi entrambi i campi 'Numero di pacchi' e 'Capienza del furgone' e premi 'Conferma' prima di procedere.")

            # Imposta il testo del pulsante di chiusura
            msg_box.setStandardButtons(QMessageBox.Ok)

            # Mostra il messaggio
            msg_box.exec_()
            return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = MainApp()
    mainApp.show()
    sys.exit(app.exec_())
