import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
plt.figure(figsize=(5, 5))
y=np.log((x**2+1)*np.exp(-np.abs(x)/10))/np.log(1+np.tan(1/((np.sin(x))**2+1)))
plt.plot(x,y)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()
