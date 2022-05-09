import matplotlib.pyplot as plt
colors = ['blue', 'pink', 'orange', 'purple','red']
labels = ['Кандидат А', 'Кандидат Б', 'Кандидат В', 'Кандидат Г', 'Кандидат Д']
x = [1,2,3,4,5]
y1= [16,18, 20, 22,24]
y2=[20,	20,	18,	22,	20]
y3=[24,	22,	20,	18,	16]

plt.title ('За месяц до выборов (столбчатая)', size = 15)
plt.bar(x, y1, color=colors, edgecolor='k', tick_label=labels)
plt.grid(True, axis='y')
plt.show()


plt.title ('За неделю до выборов (столбчатая)', size = 15)
plt.bar(x, y2, color=colors, edgecolor='k', tick_label=labels)
plt.grid(True, axis='y')
plt.show()

plt.title ('Экзит-полл (столбчатая)', size = 15)
plt.bar(x, y3, color=colors, edgecolor='k', tick_label=labels)
plt.grid(True, axis='y')
plt.show()


plt.title ('За месяц до выборов (круговая)', size = 15)
plt.pie(y1, labels=('А', 'Б', 'В','Г', 'Д'))
plt.show ()

plt.title ('За неделю до выборов (круговая)', size = 15)
plt.pie(y2,  labels=('А', 'Б', 'В','Г', 'Д'))
plt.show()


plt.title ('Экзит-полл (круговая)', size = 15)
plt.pie(y3,  labels=('А', 'Б', 'В','Г', 'Д'))
plt.show()