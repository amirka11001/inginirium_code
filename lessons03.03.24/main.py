import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action= "once")

large = 22; med = 16; small = 12
params = {"axes.titlesize": large,
          "legend.fontsize": med,
          "figure.figsize": (16, 10),
          "axes.labelsize": med,
          "axes.titlesize": med,
          "xtick.labelsize": med,
          "ytick.labelsize": med,
          "figure.titlesize": large}
plt.rcParams.update(params)
plt.style.use("fast")
sns.set_style("white")
midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

categories = np.unique(midwest["category"])
colors = [plt.cm.tab10(i/float(len(categories) -1)) for i in range(len(categories))]

plt.figure(figsize=(16, 10), dpi = 80, facecolor="w", edgecolor="k")

for i, category in enumerate(categories):
    plt.scatter("area", "poptotal",
                data=midwest.loc[midwest.category==category, :],
                s=20, c=colors[i], label=str(category))

plt.gca().set(xlim=(0.0, 0,1), ylim=(0, 90000),
              xlabel="Area", ylabel= "Population")

plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)
plt.legend(fontsize=12)
plt.show()



from matplotlib import patches
from scipy.spatial import ConvexHull
import warnings; warnings.simplefilter("ignore")
sns.set_style("white")

midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

categories = np.unique(midwest["category"])
colors = [plt.cv.tab10(i/float(len(categories)-1 )) for i in range(len(categories))]

fig = plt.figure(figsize=(16, 10), dpi=80, facecolor="w", edgecolor="k")

for i, category in enumerate(categories):
    plt.scatter("area", "poptotal", data=midwest.loc[midwest.category==category, :], s="dot_size", c=colors[i], label=str(categecolory), edgecolors="black", linewidths=0.5)

def encircle(x, y, ax=None, **kw):
    if not ax: ax=plt.gca()
    p = np.c_[x,y]
    hull = ConvexHull(p)
    poly = plt.Polygon(p[hull.vertices,:], **kw)
    ax.add_patch(poly)

midwest_encircle_data = midwest.loc[midwest.state=="IN", :]

encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec = 'k', fc="gold", alpha=0.1)
encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec='firebrick', fc="none", linewidth=1.5)

plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
              xlabel="Area", ylabel="Population")




plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Bubble plot with Encircling", fontdize=22)
plt.legend(fontsize=12)
plt.show()

