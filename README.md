# Ottimizzazione di portafoglio: multi-asset vs S&P 500
Progetto di gruppo sviluppato per l'esame di **Modelli matematici per le scelte di portafoglio** (laurea magistrale IFIR, Sapienza Università di Roma), in Python. È pubblicato nella versione consegnata per l'esame.

## Cosa fa
Confronta le performance di un portafoglio multi-asset e dell'S&P 500 (tramite SPY) in due fasi di mercato opposte: la crisi finanziaria 2007-2009 e la ripresa 2013-2016. Per ciascun periodo costruisce la frontiera efficiente di Markowitz, il portafoglio a minima varianza e il portafoglio di tangenza (massimo Sharpe).

## Titoli analizzati
| Ticker | Descrizione |
|---|---|
| BAC | Bank of America |
| KO | Coca-Cola |
| ASML.AS | ASML (Amsterdam) |
| AIR.PA | Airbus (Parigi) |
| GC=F | Future sull'oro |
| SPY | ETF sull'S&P 500 (benchmark) |

## Metodologia
- Dati storici giornalieri scaricati da Yahoo Finance con `yfinance`.
- Statistiche descrittive (rendimento medio, varianza, deviazione standard, rendimento cumulato) per il portafoglio equipesato e per l'S&P 500.
- Rendimenti logaritmici, annualizzati su 252 giorni di mercato.
- Ottimizzazione con `scipy.optimize` (SLSQP): portafoglio a minima varianza, portafoglio di tangenza e frontiera efficiente.

## Come eseguirlo
Servono Python 3 e queste librerie:
```
pip install numpy pandas yfinance matplotlib scipy
```

Poi:
```
python analisi_di_portafoglio_matteo_navaglia,_angelica_gemma_minutolo,_fabiana_rotunno.py
```

Lo script stampa le statistiche e i confronti a console e mostra i grafici dei prezzi e delle frontiere efficienti.

## Note e limiti
- Il portafoglio usato per le statistiche descrittive è equipesato, con ribilanciamento giornaliero.
- L'ottimizzazione è long-only (pesi tra 0 e 1) e lo Sharpe ratio è calcolato con tasso risk-free pari a 0.
- La media dei prezzi è calcolata su titoli in valute diverse (USD ed EUR), quindi ha valore solo descrittivo.
- Il confronto con l'S&P 500 è riportato nelle statistiche stampate a console, non nei grafici.
- `GC=F` è una serie continua di future, quindi include i rollover dei contratti.
- I dati sono scaricati da Yahoo Finance al momento dell'esecuzione: i risultati possono variare leggermente nel tempo.

## Autori
Progetto di gruppo sviluppato da Matteo Navaglia, Angelica Gemma Minutolo e Fabiana Rotunno, laurea magistrale IFIR, Sapienza Università di Roma.
