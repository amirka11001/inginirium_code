import numpy
import matplotlib
import matplotlib.pyplot
import pandas
import seaborn
import warnings; warnings.filterwarnings(action='once')

large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}

matplotlib.pyplot.rcParams.update(params)
matplotlib.pyplot.style.use('fast')
seaborn.set_style('white')

midwest = pandas.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

categories = numpy.unique(midwest['category'])
colors = [matplotlib.pyplot.cm.tab10(i/float(len(categories) -1)) for i in range(len(categories))]

matplotlib.pyplot.figure(figsize= (16, 10), dpi= 80, facecolor= 'w', edgecolor= 'k')

for i, category in enumerate(categories):
    matplotlib.pyplot.scatter('area', 'poptotal',
                              data = midwest.loc[midwest.category== category, :],
                              s= 20, c= colors[i], label= str(category))

matplotlib.pyplot.gca().set(xlim= (0.0, 0.1), ylim= (0, 90000),
                            xlabel= 'Area', ylabel= 'Population')

matplotlib.pyplot.xticks(fontsize= 12); matplotlib.pyplot.yticks(fontsize= 12)
matplotlib.pyplot.title('Scatterplot of Midwest Area vs Population', fontsize= 22)
matplotlib.pyplot.legend(fontsize= 12)
matplotlib.pyplot.show()

from matplotlib import patches
from scipy.spatial import ConvexHull
import warnings; warnings.simplefilter('ignore')
seaborn.set_style('white')

midwest = pandas.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

categories = numpy.unique(midwest['category'])
colors = [matplotlib.pyplot.cm.tab10(i/float(len(categories) -1)) for i in range(len(categories))]

fig = matplotlib.pyplot.figure(figsize= (16, 10), dpi= 80, facecolor= 'w', edgecolor= 'k')

for i, category in enumerate(categories):
    matplotlib.pyplot.scatter('area', 'poptotal', data = midwest.loc[midwest.category==category, :], s= 'dot_size', c= colors[i], label= str(category), edgecolors= 'black', linewidths= 0.5)

def encircle(x, y, ax= None, **kw):
    if not ax: ax= matplotlib.pyplot.gca()
    p = numpy.c_[x, y]
    hull = ConvexHull(p)
    poly = matplotlib.pyplot.Polygon(p[hull.vertices, :], **kw)
    ax.add_patch(poly)

midwest_encircle_data = midwest.loc[midwest.state== 'IN', :]

encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec= 'k', fc= 'gold', alpha= 0.1)
encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec= 'firebrick', fc= 'none', linewidth= 1.5)

matplotlib.pyplot.gca().set(xlim= (0.0, 0.1), ylim= (0, 90000),
                            xlabel= 'Area', ylabel = 'Population')

matplotlib.pyplot.xticks(fontsize= 12); matplotlib.pyplot.yticks(fontsize= 12)
matplotlib.pyplot.title('Bubble Plot with Encircling', fontsize= 22)
matplotlib.pyplot.legend(fontsize= 12)
matplotlib.pyplot.show()