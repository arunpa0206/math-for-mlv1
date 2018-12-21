import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# import seaborn
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(4.5,3)})

# generate random numbersfrom N(0,1)
data_normal = norm.rvs(size=10000,loc=0,scale=1)

ax = sns.distplot(data_normal,
                  bins=100,
                  kde=False,
                  color='skyblue',
                  hist_kws={'alpha':1})
ax.set(xlabel='Normal', ylabel='Frequency')

plt.show()
