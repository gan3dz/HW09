import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss


def main():
    a = np.random.normal(0, 3, 10000)
    b = np.random.normal(0, 4, 10000)
    c = a + b

    mu_a, sigma_a = ss.norm.fit(a)
    plt.figure()
    bin_values, bins, myart = plt.hist(a, label='a', alpha=0.5, density=1, bins=50)
    centers = 0.5 * (bins[:-1] + bins[1:])
    best_fit_line = ss.norm.pdf(centers, mu_a, sigma_a)
    plt.plot(centers, best_fit_line, label=f' $\mu$={mu_a:4.2} \n $\sigma$={sigma_a:4.2}')
    plt.legend()
    plt.show()

main()
