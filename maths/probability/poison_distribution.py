from scipy.stats import poisson

import seaborn as sns
import matplotlib.pyplot as plt

data_poisson = poisson.rvs(mu=3, size=10000)
ax = sns.distplot(data_poisson,
                  kde=False,
                  color='green',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Poisson', ylabel='Frequency')
plt.show()
