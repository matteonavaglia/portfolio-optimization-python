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

## Risultati
Portafoglio equipesato (BAC, KO, ASML, AIR, oro) a confronto con l'S&P 500 (SPY).
| Periodo | Metrica | Portafoglio | S&P 500 |
|---|---|---|---|
| Crisi 2007-2009 | Rendimento totale | +4,22% | -15,07% |
| | Rendimento medio giornaliero | 0,000229 | -0,000040 |
| | Varianza dei rendimenti | 0,000343 | 0,000354 |
| Ripresa 2013-2016 | Rendimento totale | +47,50% | +65,95% |
| | Rendimento medio giornaliero | 0,000440 | 0,000535 |
| | Varianza dei rendimenti | 0,000069 | 0,000065 |

Nella crisi il portafoglio chiude in positivo mentre l'S&P 500 perde oltre il 15%, con una varianza dei rendimenti simile. Nella ripresa l'S&P 500 fa meglio, con un rischio analogo: il portafoglio diversificato è pensato per proteggere nelle fasi di stress, non per massimizzare il rendimento nei mercati rialzisti. Il ruolo dell'oro e di Coca-Cola come componenti difensive è un'interpretazione di noi autori.

### Portafogli efficienti (long-only, tasso risk-free = 0)
| | Rendimento | Volatilità | Sharpe |
|---|---|---|---|
| Minima varianza, 2007-2009 | 0,115 | 0,166 | 0,690 |
| Minima varianza, 2013-2016 | 0,025 | 0,098 | 0,261 |
| Tangenza, 2007-2009 | 0,155 | 0,180 | 0,860 |
| Tangenza, 2013-2016 | 0,164 | 0,179 | 0,917 |

[Confronto delle frontiere efficienti nei due periodi](frontiere_efficienti.png)

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
