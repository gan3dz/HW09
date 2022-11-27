import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import pandas as pd


# makes Gaussian fit and histogram
def gauss(data, name, attr, ax):
    # fit data to Gaussian
    mu, sigma = ss.norm.fit(data)
    # print mu and sigma values
    print(f'{name}.{attr}: mu={mu:4.2}, sigma={sigma:4.2} ')
    # return histogram for axes, and normalize it
    bin_values, bins, myart = ax.hist(data, label=f'{name}', alpha=0.5, density=1)
    # make Gaussian fit, and put in graph with mu and sigma in label
    best_fit_line = ss.norm.pdf(bins, mu, sigma)
    ax.plot(bins, best_fit_line, label=f'{name} fit: mu={mu:4.2}, sigma={sigma:4.2}')


def main():
    iris_ds = pd.read_csv('iris.data')
    fig, axs = plt.subplots(4, 4)
    diag = [axs[0,0], axs[1,1], axs[2,2], axs[3,3]]
    colors = ['green', 'orange', 'blue']
    label_species = ['setosa', 'virginica', 'versicolor']
    count = 0
    # range 4
    # enumerate
    for p in iris_ds.columns[:-1]:
        for t in iris_ds.columns[:-1]:
            if p == t:
                gauss(p, )
            else:
                print(1)
                '''
                for species , look in hw8 solution
                
                '''


    print(count)

main()
