import matplotlib.pyplot as plt
import numpy as np
x1, y1= np.loadtxt('mutant.txt', skiprows=1, usecols=(0,1), unpack=True)
x2, y2= np.loadtxt('wild_type.txt', skiprows=1, usecols=(0,1), unpack=True)

x3 = [1, 2, 3, 4, 5]
y3 = [0.99, 0.49, 0.35, 0.253, 0.18]


x4=np.random.rand(100)
y4=np.random.rand(100)

data = 10 * np.random.rand(100)
x5 = np.sort(data)
epsilon3 = np.random.rand(100)
y5 = (x5-5)**2 / 10 + epsilon3 - 0.5

def correlation(x,y):
    a=[]
    n=len(x)
    for i in range (len(x)):
        summand=((x[i]-np.mean(x))/np.std(x))*((y[i]-np.mean(y))/np.std(y))
        a.append(summand)
    r=np.sum(a)*1/n
    return r

r1=correlation(x1,y1)
r2=correlation(x2,y2)
r3=correlation(x3,y3)
r4=correlation(x4,y4)
r5=correlation(x5,y5)

print('Набор 1 из примера, r=',r3)
print('Набор 2 из примера, r=', r4)
print('Набор 3 из примера, r=', r5)
print('Набор мутантный, r=', r1)
print('Набор дикий, r=', r2)



