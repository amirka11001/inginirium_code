import numpy
import matplotlib.pyplot

phi = numpy.linspace(0, 100, 100)
matplotlib.pyplot.plot(phi, numpy.sin(phi))
matplotlib.pyplot.plot(phi, numpy.cos(phi))

matplotlib.pyplot.show()