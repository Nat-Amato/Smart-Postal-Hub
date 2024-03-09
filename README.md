# Smart-Postal-Hub
Simulazione di un centro di smistamento postale automatizzato

In un’epoca in cui l’e-commerce è in costante crescita, la gestione efficiente dei pacchi è fondamentale. 

Il nostro team propone di simulare un centro di smistamento postale automatizzato, sfruttando le tecnologie e le tecniche apprese durante il corso.

Cosa accade:

1. Ricezione del pacco: Quando un pacco entra nel centro di smistamento, viene scansionato il suo codice a barre. Questo codice a barre contiene informazioni importanti come il peso, le dimensioni, la destinazione e la priorità del pacco.

2. Ordinamento prioritario: Una volta scansionato, utilizza il classificatore Naive-Bayes per categorizzare il pacco in base ai dettagli forniti generando una classifica di priorità decrescente.

3. Elaborazione del pacco: Successivamente, consulta la base di conoscenza per determinare il percorso da intraprendere, questo percorso viene determinato utilizzando un grafo con pesi e  l’algoritmo IDA* (Iterative-Deepening A*) per determinare il percorso più efficiente in base alla situazione attuale del centro di smistamento.

4. Divisione dei pacchi: Una volta arrivati a destinazione (livello 2), i pacchi vengono divisi in base alla capienza della vettura, questo processo viene gestito da un CSP (Constraint Satisfaction Problem) solver che tiene conto dei vincoli della vettura.

5. Carico delle vetture: Divisi i pacchi, dei robot, addestrati in precedenza, li caricheranno nella vettura, questo processo tiene conto delle informazioni come la grandezza e la fragilità dei pacchi. Ad esempio, i pacchi più grandi o più pesanti potrebbero essere caricati per primi, mentre i pacchi più fragili potrebbero essere posizionati in modo da minimizzare il rischio di danni.

6. Preparazione della bolla di consegna: Una volta terminato il processo di smistamento, il corriere preposto riceverà una bolla con tutte le informazioni utili sui pacchi caricati. Questa bolla viene generata consultando la base di conoscenza.

Durante l’esecuzione del programma, sarà possibile interrogare il sistema del centro di smistamento, ad esempio per sapere quanti pacchi sono attualmente in elaborazione o quali pacchi sono stati caricati sulla vettura. 

