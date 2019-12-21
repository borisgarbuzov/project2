import random
import matplotlib.pyplot as plt

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
plt.axis([0, 1000, 0, 6])
dots = []
xs = []
sum = 0
for i in range(1, 1000):
    for j in range(i):
        n = random.randint(1, 6)
        sum += n
    dots.append(sum / i)
    xs.append(i)
    sum = 0
plt.plot(xs, dots, color='blue')
fig.savefig('plot.png')