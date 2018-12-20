import seaborn as sns;
import numpy as np
import matplotlib.pyplot as plt

sns.set()


uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)
plt.show()
