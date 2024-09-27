import matplotlib.pyplot as plt

x = [i for i in range(-6, 5)]
y = [elem ** 2 for elem in x]
plt.plot(x, y, color='#4D9B8E', markersize=10, marker='o')
plt.xlabel("Ось x")
plt.ylabel("Ось y")
plt.title("Это график y = x^2")
plt.savefig("/home/packletka/PycharmProjects/BotMaker/matplotlib/Beauty.png")
