from scipy.stats import binom
import seaborn as sns
import matplotlib.pyplot as plt


#Let us generate 10000 from binomial distribution and plot the distribution.
data_binom = binom.rvs(n=10,p=0.5,size=10000)
ax = sns.distplot(data_binom,
                  kde=False,
                  color='skyblue',
                  hist_kws={'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')
plt.show()
