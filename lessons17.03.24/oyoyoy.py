import numpy as np
import matplotlib.pyplot as plt

phi = np.linspace(0, 2.*np.pi, 100)
plt.plot(phi, np.sin(phi))
plt.plot(phi, np.cos(phi))

plt.show()

x = np.linspace(0, 1, 100)
f1 = 0.25 - (x - 0.5)**2
f2 = x**3
plt.plot(x, f1, ':b')    # пунктирная синяя линия
plt.plot(x, f2, '--r')   # штрихованная красная линия
plt.plot(x, f1+f2, 'k')  # черная непрерывная линия

import numpy as np
import matplotlib.pyplot as plt

rg = np.random.Generator(np.random.PCG64(5))
data = rg.poisson(145, 10000)
plt.hist(data, bins=40)
# для краткости мы опускаем код для настройки осей, сетки и т.д.

rg = np.random.Generator(np.random.PCG64(5))
data1 = rg.poisson(145, 10000)
data2 = rg.poisson(140, 2000)

# левая гистограмма
plt.hist([data1, data2], bins=40)
# центральная гистограмма
plt.hist([data1, data2], bins=40, histtype='step')
# правая гистограмма
plt.hist([data1, data2], bins=40, stacked=True)

def poisson_hist(data, bins=60, lims=None):
    """ Гистограмма в виде набора значений с ошибками """
    hist, bins = np.histogram(data, bins=bins, range=lims)
    bins = 0.5 * (bins[1:] + bins[:-1])
    return (bins, hist, np.sqrt(hist))

rg = np.random.Generator(np.random.PCG64(5))
data = rg.poisson(145, 10000)

x, y, yerr = poisson_hist(data, bins=40, lims=(100, 190))
plt.errorbar(x, y, yerr=yerr, marker='o', markersize=4,
             linestyle='none', ecolor='k', elinewidth=0.8,
             capsize=3, capthick=1)

rg = np.random.Generator(np.random.PCG64(5))

means = (0.5, 0.9)
covar = [
    [1., 0.6],
    [0.6, 1.]
]
data = rg.multivariate_normal(means, covar, 5000)

plt.scatter(data[:,0], data[:,1], marker='o', s=1)

rg = np.random.Generator(np.random.PCG64(4))

data = rg.uniform(-1, 1, (50, 2))
col = np.arctan2(data[:, 1], data[:, 0])
size = 100*np.sum(data**2, axis=1)

plt.scatter(data[:,0], data[:,1], marker='o', s=size, c=col)


plt.show()

rg = np.random.Generator(np.random.PCG64())
plt.plot(rg.binomial(10, 0.3, 6), 'ob')  # синие круги
plt.plot(rg.poisson(7, 6), 'vr')         # красные треугольники
plt.plot(rg.integers(0, 10, 6), 'Dk')    # черные ромбы

plt.show()

rg = np.random.Generator(np.random.PCG64(5))
x = np.arange(6)
y = rg.poisson(149, x.size)
plt.errorbar(x, y, yerr=np.sqrt(y), marker='o', linestyle='none')
plt.show()

rg = np.random.Generator(np.random.PCG64(5))
N = 6
x = rg.poisson(169, N)
y = rg.poisson(149, N)
plt.errorbar(x, y, xerr=np.sqrt(x), yerr=np.sqrt(y), marker='o', linestyle='none')
plt.show()

rg = np.random.Generator(np.random.PCG64(11))
N = 6
x = np.arange(N)
y = rg.poisson(149, N)
yerr = [
    0.7*np.sqrt(y),
    1.2*np.sqrt(y)
]
plt.errorbar(x, y, yerr=yerr, marker='o', linestyle='none')
plt.show()

plt.errorbar(x, y, yerr=yerr, marker='o', linestyle='none',
    ecolor='k', elinewidth=0.8, capsize=4, capthick=1)
plt.show()

plt.xlabel('run number', fontsize=16)
plt.ylabel(r'average current ($\mu A$)', fontsize=16)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# задаем размер шрифта
matplotlib.rcParams.update({'font.size': 12})

rg = np.random.Generator(np.random.PCG64(11))
x = np.arange(6)
y = rg.poisson(149, x.size)
yerr = [
    0.7*np.sqrt(y),
    1.2*np.sqrt(y)
]
plt.errorbar(x, y, yerr=yerr, marker='o', linestyle='none',
    ecolor='k', elinewidth=0.8, capsize=4, capthick=1)

# добавляем подписи к осям и заголовок диаграммы
plt.xlabel('run number', fontsize=16)
plt.ylabel(r'average current ($\mu A$)', fontsize=16)
plt.title(r'The $\alpha^\prime$ experiment. Season 2020-2021')

# задаем диапазон значений оси y
plt.ylim([0, 200])
# оптимизируем поля и расположение объектов
plt.tight_layout()

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 12})

x = np.linspace(0, 1, 100)
f1 = 0.25 - (x - 0.5)**2
f2 = x**3

# указываем в аргументе label содержание легенды
plt.plot(x, f1, ':b', label='1st component')
plt.plot(x, f2, '--r', label='2nd component')
plt.plot(x, f1+f2, 'k', label='total')

plt.xlabel(r'$x$', fontsize=16)
plt.ylabel(r'$f(x)$', fontsize=16)

plt.xlim([0, 1])
plt.ylim([0, 1])

# выводим легенду
plt.legend(fontsize=14)

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 12})

x = np.linspace(-1, 1, 250)
plt.plot(x, x, label=r'$x$')
plt.plot(x, x**2, label=r'$x^2$')
plt.plot(x, x**3, label=r'$x^3$')
plt.plot(x, np.cbrt(x), label=r'$x^{1/3}$')
plt.legend(fontsize=16)

# включаем дополнительные отметки на осях
plt.minorticks_on()
plt.xlabel(r'$x$', fontsize=16)

plt.xlim([-1., 1.])
plt.ylim([-1., 1.])
# включаем основную сетку
plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.tight_layout()

plt.show()

from scipy import stats

means = (0.5, 0.9)
covar = [
    [1., 0.6],
    [0.6, 1.]
]

mvn = stats.multivariate_normal(means, covar)
x, y = np.meshgrid(
    np.linspace(-3, 3, 80),
    np.linspace(-2, 4, 80)
)
data = np.dstack((x, y))

# левая диаграмма — без заливки цветом
plt.contour(x, y, mvn.pdf(data), levels=10)
# правая диаграмма — с заливкой цветом
plt.contourf(x, y, mvn.pdf(data), levels=10)

cs = plt.contourf(x, y, mvn.pdf(data), levels=15,
                  cmap=matplotlib.cm.magma_r)
cbar = plt.colorbar(cs)

import numpy as np
import matplotlib.pyplot as plt

exno = 26

rg = np.random.Generator(np.random.PCG64(5))
x1 = rg.exponential(10, 5000)
x2 = rg.normal(10, 0.1, 100)

# Строим основную гистограмму
plt.hist([x1, x2], bins=150, range=(0, 60), stacked=True)
plt.minorticks_on()
plt.xlim((0, 60))
plt.grid(which='major')
plt.grid(which='minor', linestyle=':')

# Строим вторую гистограмму в отдельных осях
plt.axes([.5, .5, .4, .4])
plt.hist([x1, x2], bins=100, stacked=True, range=(9, 11))
plt.grid(which='major')

plt.tight_layout()

# сохраняем диаграмму в файл
plt.savefig('histograms.png')
plt.show()
