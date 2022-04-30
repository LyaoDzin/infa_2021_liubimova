import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-3, 4.01, 0.01)
plt.plot(x, x*x-x-6)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()