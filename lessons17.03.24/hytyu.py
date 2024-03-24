import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
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
plt.rcParams.update(params)
plt.style.use('fast')
sns.set_style("white")

df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

plt.figure(figsize= (16, 10), dpi= 80)
sns.kdeplot(df.loc[df['cyl'] == 4, "cty"], shade= True, color= "g", label= "Cyl=4", alpha= 0.7)
sns.kdeplot(df.loc[df['cyl'] == 5, "cty"], shade= True, color= "deeppink", label= "Cyl=5", alpha= 0.7)
sns.kdeplot(df.loc[df['cyl'] == 6, "cty"], shade= True, color= "dodgerblue", label= "Cyl=6", alpha= 0.7)
sns.kdeplot(df.loc[df['cyl'] == 8, "cty"], shade= True, color= "orange", label= "Cyl=8", alpha= 0.7)

plt.title('Dinsity Plot of City Mileage by n_Cylinders', fontsize= 22)
plt.legend()
plt.show()

import joypy
mpg = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

plt.figure(figsize= (16, 10), dpi= 80)
fig, axes = joypy.joyplot(mpg, column= ['hwy', 'cty'], by= "class", ylim= 'own', figsize= (14, 10))

plt.title('Joy Plot of City and Highway Mileage by Class', fontsize= 22)
plt.show()

df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mpg_ggplot2.csv")

plt.figure(figsize= (13, 10), dpi= 80)
sns.boxplot(x= 'class', y= 'hwy', data= df, notch= False)

def add_n_obs(df,group_col,y):
    medians_dict = {grp[0]:grp[1][y].median() for grp in df.groupby(group_col)}
    xticklabels = [x.get_text() for x in plt.gca().get_xticklabels()]
    n_obs = df.groupby(group_col)[y].size().values
    for (x, xticklabel), n_ob in zip(enumerate(xticklabels), n_obs):
        plt.text(x, medians_dict[xticklabel]*1.01, "#obs : "+str(n_ob), horizontalalignment= 'center', fontdict= {'size':14}, color= 'white')

add_n_obs(df,group_col='class', y='hwy')

plt.title('Box Plot of Highway Mileage by Vehicle Class', fontsize= 22)
plt.ylim(10, 40)
plt.show()
