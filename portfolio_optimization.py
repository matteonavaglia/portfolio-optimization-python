"""
Analisi di portafoglio: multi-asset vs S&P 500

Progetto di gruppo per l'esame di Modelli matematici per le scelte di portafoglio
(laurea magistrale IFIR, Sapienza Università di Roma).

Autori: Matteo Navaglia, Angelica Gemma Minutolo, Fabiana Rotunno
"""

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.optimize import minimize
# =====================================================
# DOWNLOAD DATI STORICI
# =====================================================
dati1 = yf.download(["BAC", "KO","ASML.AS","AIR.PA", "GC=F"], start="2007-01-01", end="2009-12-31")
dati2 = yf.download(["BAC", "KO","ASML.AS","AIR.PA", "GC=F"], start="2013-01-01", end="2016-12-31")
dati3 = yf.download(["SPY"], start="2007-01-01", end="2009-12-31")
dati4 = yf.download(["SPY"], start="2013-01-01", end="2016-12-31")

prezzi1 = dati1['Close'].dropna()
prezzi2 = dati2['Close'].dropna()
prezzi3 = dati3['Close'].dropna()
prezzi4 = dati4['Close'].dropna()

# ============================================================
# ESTRAZIONE DEI PREZZI DI CHIUSURA
# ============================================================
rendimenti1_df = dati1['Close'].pct_change(fill_method=None).replace([np.inf, -np.inf], np.nan).dropna()
rendimenti2_df = dati2['Close'].pct_change(fill_method=None).replace([np.inf, -np.inf], np.nan).dropna()
rendimenti3_df = dati3['Close'].pct_change(fill_method=None).replace([np.inf, -np.inf], np.nan).dropna()
rendimenti4_df = dati4['Close'].pct_change(fill_method=None).replace([np.inf, -np.inf], np.nan).dropna()

# ============================================================
# CALCOLO DEI RENDIMENTI GIORNALIERI
# ============================================================
rend_giornaliero_port1 = rendimenti1_df.mean(axis=1)
rend_giornaliero_port2 = rendimenti2_df.mean(axis=1)
rend_giornaliero_port3 = rendimenti3_df.mean(axis=1)
rend_giornaliero_port4 = rendimenti4_df.mean(axis=1)

# ============================================================
# CALCOLO DELLE STATISTICHE SCALARI DI PREZZI E RENDIMENTI
# ============================================================
media_prezzi1 = np.mean(prezzi1.values.flatten())
varianza_rendimenti1 = np.var(rend_giornaliero_port1.values.flatten())
media_prezzi2 = np.mean(prezzi2.values.flatten())
varianza_rendimenti2 = np.var(rend_giornaliero_port2.values.flatten())
media_prezzi3 = np.mean(prezzi3.values.flatten())
varianza_rendimenti3 = np.var(rend_giornaliero_port3.values.flatten())
media_prezzi4 = np.mean(prezzi4.values.flatten())
varianza_rendimenti4 = np.var(rend_giornaliero_port4.values.flatten())

# ============================================================
# CALCOLO DELLA DEVIAZIONE STANDARD DEI RENDIMENTI
# ============================================================
deviazione_standard_rendimenti1 = np.sqrt(varianza_rendimenti1)
deviazione_standard_rendimenti2 = np.sqrt(varianza_rendimenti2)
deviazione_standard_rendimenti3 = np.sqrt(varianza_rendimenti3)
deviazione_standard_rendimenti4 = np.sqrt(varianza_rendimenti4)

#stampa i risultati

# ============================================================
# CALCOLO DEL RENDIMENTO MEDIO GIORNALIERO DEL PORTAFOGLIO
# ============================================================
media_rend_port1 = rend_giornaliero_port1.mean()
media_rend_port2 = rend_giornaliero_port2.mean()
media_rend_port3 = rend_giornaliero_port3.mean()
media_rend_port4 = rend_giornaliero_port4.mean()

# ============================================================
# CALCOLO DEL RENDIMENTO CUMULATIVO DEL PERIODO
# ============================================================
# Formula: (1 + r1) * (1 + r2) * ... - 1
rend_totale_port1 = (1 + rend_giornaliero_port1).prod() - 1
rend_totale_port2 = (1 + rend_giornaliero_port2).prod() - 1
rend_totale_port3 = (1 + rend_giornaliero_port3).prod() - 1
rend_totale_port4 = (1 + rend_giornaliero_port4).prod() - 1

# ============================================================
# STAMPA DELLE STATISTICHE DESCRITTIVE DEI PORTAFOGLI
# ============================================================
print("-" * 30)
print("STATISTICHE PREZZI PORTAFOGLIO 1:")
print(f"Media prezzi (Portafoglio 1): ${media_prezzi1:.2f}")
print(f"Varianza rendimenti (Portafoglio 1): {varianza_rendimenti1:.6f}")
print(f"Rendimento medio giornaliero (P1): {media_rend_port1:.6f}")
print(f"Rendimento TOTALE del periodo (P1): {rend_totale_port1*100:.2f}%")
print(f"Deviazione Standard (Portafoglio 1): {deviazione_standard_rendimenti1:.2f}")
print("-" * 30)
print("STATISTICHE PREZZI PORTAFOGLIO 2:")
print(f"Media prezzi (Portafoglio 2): ${media_prezzi2:.2f}")
print(f"Varianza rendimenti (Portafoglio 2): {varianza_rendimenti2:.6f}")
print(f"Rendimento medio giornaliero (P2): {media_rend_port2:.6f}")
print(f"Rendimento TOTALE del periodo (P2): {rend_totale_port2*100:.2f}%")
print(f"Deviazione Standard (Portafoglio 2): {deviazione_standard_rendimenti2:.2f}")
print("-" * 30)
print("STATISTICHE PREZZI PORTAFOGLIO 3:")
print(f"Media prezzi (Portafoglio 3): ${media_prezzi3:.2f}")
print(f"Varianza rendimenti (Portafoglio 3): {varianza_rendimenti3:.6f}")
print(f"Rendimento medio giornaliero (P3): {media_rend_port3:.6f}")
print(f"Rendimento TOTALE del periodo (P3): {rend_totale_port3*100:.2f}%")
print(f"Deviazione Standard (Portafoglio 3): {deviazione_standard_rendimenti3:.2f}")
print("-" * 30)
print("STATISTICHE PREZZI PORTAFOGLIO 4:")
print(f"Media prezzi (Portafoglio 4): ${media_prezzi4:.2f}")
print(f"Varianza rendimenti (Portafoglio 4): {varianza_rendimenti4:.6f}")
print(f"Rendimento medio giornaliero (P4): {media_rend_port4:.6f}")
print(f"Rendimento TOTALE del periodo (P4): {rend_totale_port4*100:.2f}%")
print(f"Deviazione Standard (Portafoglio 4): {deviazione_standard_rendimenti4:.2f}")


# =====================================================
# PARAMETRI GENERALI
# =====================================================
NUM_TRADING_DAYS = 252
tickers = ["BAC", "KO", "ASML.AS", "AIR.PA", "GC=F"]

# =====================================================
# DOWNLOAD DATI
# =====================================================
def download_data(tickers, start, end):
    data = yf.download(
        tickers,
        start=start,
        end=end,
        auto_adjust=True,
        progress=False
    )["Close"]
    return data.dropna()

# =====================================================
# GRAFICO PREZZI
# =====================================================
def plot_prices(prices, title):
    plt.figure(figsize=(14, 15))
    for col in prices.columns:
        plt.plot(prices.index, prices[col], label=col)
    plt.title(title)
    plt.xlabel("Data")
    plt.ylabel("Prezzo ($)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

# =====================================================
# RENDIMENTI LOGARITMICI
# =====================================================
def compute_log_returns(prices):
    return np.log(prices / prices.shift(1)).dropna()

# =====================================================
# MVP – PORTAFOGLIO A VARIANZA MINIMA
# =====================================================
def minimum_variance_portfolio(cov_matrix):
    n = cov_matrix.shape[0]

    def portfolio_volatility(w):
        return np.sqrt(w.T @ cov_matrix @ w)

    constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1}
    bounds = [(0, 1)] * n
    w0 = np.ones(n) / n

    res = minimize(
        portfolio_volatility,
        w0,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )

    return res.x

# =====================================================
# FRONTIERA EFFICIENTE
# =====================================================
def efficient_frontier(expected_returns, cov_matrix, n_points=100):
    n_assets = len(expected_returns)

    def portfolio_volatility(w):
        return np.sqrt(w.T @ cov_matrix @ w)

    target_returns = np.linspace(
        expected_returns.min(),
        expected_returns.max(),
        n_points
    )

    vols, rets = [], []

    for target in target_returns:
        constraints = (
            {"type": "eq", "fun": lambda w: np.sum(w) - 1},
            {"type": "eq", "fun": lambda w: w @ expected_returns - target}
        )
        bounds = [(0, 1)] * n_assets
        w0 = np.ones(n_assets) / n_assets

        res = minimize(
            portfolio_volatility,
            w0,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints
        )

        if res.success:
            vols.append(res.fun)
            rets.append(target)

    return np.array(vols), np.array(rets)

# =====================================================
# PORTAFOGLIO DI TANGENZA (MAX SHARPE)
# =====================================================
def tangency_portfolio(expected_returns, cov_matrix):
    n = len(expected_returns)

    def neg_sharpe(w):
        ret = w @ expected_returns
        vol = np.sqrt(w.T @ cov_matrix @ w)
        return -ret / vol

    constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1}
    bounds = [(0, 1)] * n
    w0 = np.ones(n) / n

    res = minimize(
        neg_sharpe,
        w0,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )

    return res.x

# =====================================================
# STATISTICHE PORTAFOGLIO
# =====================================================
def portfolio_stats(weights, expected_returns, cov_matrix):
    ret = weights @ expected_returns
    vol = np.sqrt(weights.T @ cov_matrix @ weights)
    sharpe = ret / vol
    return ret, vol, sharpe

# =====================================================
# ANALISI COMPLETA PER UN PERIODO
# =====================================================
def run_analysis(tickers, start_date, end_date, label):

    print(f"\n{'='*60}")
    print(f"ANALISI PERIODO: {label}")
    print(f"{'='*60}")

    prices = download_data(tickers, start_date, end_date)
    plot_prices(prices, f"Prezzi di Chiusura ({label})")

    returns = compute_log_returns(prices)
    expected_returns = returns.mean() * NUM_TRADING_DAYS
    cov_matrix = returns.cov() * NUM_TRADING_DAYS

    # MVP
    w_mvp = minimum_variance_portfolio(cov_matrix)
    mvp_stats = portfolio_stats(w_mvp, expected_returns, cov_matrix)

    # Tangency
    w_tan = tangency_portfolio(expected_returns, cov_matrix)
    tan_stats = portfolio_stats(w_tan, expected_returns, cov_matrix)

    # Frontiera
    frontier = efficient_frontier(expected_returns, cov_matrix)

    return {
        "w_mvp": w_mvp,
        "mvp_stats": mvp_stats,
        "w_tan": w_tan,
        "tan_stats": tan_stats,
        "frontier": frontier
    }

# =====================================================
# MAIN
# =====================================================
if __name__ == "__main__":

    # -------- PERIODO 1 --------
    results_p1 = run_analysis(
        tickers,
        "2007-01-01",
        "2009-12-31",
        "Periodo 1 (2007-2009)"
    )

    # -------- PERIODO 2 --------
    results_p2 = run_analysis(
        tickers,
        "2013-01-01",
        "2016-12-31",
        "Periodo 2 (2013-2016)"
    )

    # =================================================
    # ESTRAZIONE RISULTATI
    # =================================================
    mvp_ret_p1, mvp_vol_p1, mvp_sharpe_p1 = results_p1["mvp_stats"]
    mvp_ret_p2, mvp_vol_p2, mvp_sharpe_p2 = results_p2["mvp_stats"]

    tan_ret_p1, tan_vol_p1, tan_sharpe_p1 = results_p1["tan_stats"]
    tan_ret_p2, tan_vol_p2, tan_sharpe_p2 = results_p2["tan_stats"]

    frontier_vols_p1, frontier_rets_p1 = results_p1["frontier"]
    frontier_vols_p2, frontier_rets_p2 = results_p2["frontier"]

    # =================================================
    # OUTPUT CONFRONTO PORTAFOGLI
    # =================================================
    print("\n" + "="*70)
    print("CONFRONTO PORTAFOGLI A VARIANZA MINIMA")
    print("="*70)

    print(f"{'Metrica':<25} {'MVP P1':<15} {'MVP P2':<15}")
    print("-"*55)
    print(f"{'Rendimento':<25} {mvp_ret_p1:.3f}{'':<8} {mvp_ret_p2:.3f}")
    print(f"{'Volatilità':<25} {mvp_vol_p1:.3f}{'':<8} {mvp_vol_p2:.3f}")
    print(f"{'Sharpe Ratio':<25} {mvp_sharpe_p1:.3f}{'':<8} {mvp_sharpe_p2:.3f}")

    print("\n" + "="*70)
    print("PORTAFOGLIO DI TANGENZA (MAX SHARPE)")
    print("="*70)

    print(f"{'Metrica':<25} {'P1':<15} {'P2':<15}")
    print("-"*55)
    print(f"{'Rendimento':<25} {tan_ret_p1:.3f}{'':<8} {tan_ret_p2:.3f}")
    print(f"{'Volatilità':<25} {tan_vol_p1:.3f}{'':<8} {tan_vol_p2:.3f}")
    print(f"{'Sharpe Ratio':<25} {tan_sharpe_p1:.3f}{'':<8} {tan_sharpe_p2:.3f}")

    # =================================================
    # GRAFICO FRONTIERE EFFICIENTI
    # =================================================
    plt.figure(figsize=(11, 7))

    plt.plot(frontier_vols_p1, frontier_rets_p1,
             label="Frontiera Periodo 1", linewidth=2)

    plt.plot(frontier_vols_p2, frontier_rets_p2,
             label="Frontiera Periodo 2", linewidth=2)

    plt.scatter(mvp_vol_p1, mvp_ret_p1, marker="o", s=80, label="MVP P1")
    plt.scatter(mvp_vol_p2, mvp_ret_p2, marker="o", s=80, label="MVP P2")

    plt.scatter(tan_vol_p1, tan_ret_p1, marker="^", s=90, label="Tangency P1")
    plt.scatter(tan_vol_p2, tan_ret_p2, marker="^", s=90, label="Tangency P2")

    plt.xlabel("Volatilità Annualizzata")
    plt.ylabel("Rendimento Atteso Annualizzato")
    plt.title("Confronto Frontiere Efficienti")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()
