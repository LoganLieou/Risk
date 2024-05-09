import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

L = 0.2
m = 100
t = 4

def estimate_time(n):
    return n / L

def geom_bm(s0, mu, sigma, T):
    # Drift (mu) and volatility (sigma) are calculated from API data.
    dt = 1/t

    # Analytic solution to the SDE
    St = np.exp(
        (mu - sigma**2 / 2)*dt +
        sigma * np.random.normal(0, np.sqrt(dt), size=(m,int(t*T))).T # run m simulations t*T times
    )
    St = np.vstack([np.ones(m), St])

    return s0 * St.cumprod(axis=0)

def plot_gbm(s0, mu, sigma, T):
    # Parameters from monte carlo.
    St = geom_bm(s0, mu, sigma, T)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    time = np.linspace(0,T,(T*t)+1)
    tt = np.full(shape=(m,(T*t)+1), fill_value=time).T

    ax.set_yscale("log")
    ax.set_title("Asset Realization Expected Frame (t)")
    ax.set_ylabel("price (ISK)")
    ax.set_xlabel("time (min)")
    ax.plot(tt, St)
    fig.savefig("geom-bm.png", dpi=300)

def confidence_interval(s0, mu, sigma, T):
    St = geom_bm(s0, mu, sigma, T)

    ste = np.std(St) / np.sqrt(m)
    z = norm.ppf(0.99)
    x = np.mean(St)

    return [x - z*ste, x + z*ste]

def gank_pdf(sec_levels):
    x = np.tanh(np.mean(sec_levels))
    if x < 0:
        return 1
    else:
        return 1 - x

def death_pdf():
    return 0.5

def failure(sec_levels):
    return gank_pdf(sec_levels) * death_pdf()

if __name__ == "__main__":

    s0 = 954278
    mu = (0.04) / 43830 # over a month
    sigma = np.sqrt(24277) / s0
    T = estimate_time(7)

    print(confidence_interval(s0, mu, sigma, T))

    q = failure([1, 1, 1, 1, .7, .5, .6, .4])
    margin = .2 # varies with the confidence interval
    f = (1 - q) - (q / (1 + margin)) # if successful you gain all capital invested + margin
    print(f)