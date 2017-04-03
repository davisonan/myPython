# tmp.py

import math
import matplotlib.pyplot as plt

x = list(range(30))
y1 = [x for x in x]
y2 = [x ** 2 for x in x]
y3 = [x ** 3 for x in x]
y4 = [math.exp(x) for x in x]
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)

plt.figure('lin')
plt.plot(x, y1)
plt.ylim(0, 1000)
plt.xlabel('sample points')
plt.ylabel('linear function')

plt.figure('qua')
plt.plot(x, y2)
plt.ylim(0, 1000)
plt.xlabel('sample points')
plt.ylabel('quad function')

plt.figure('cub')
plt.plot(x, y3)
plt.ylim(0, 1000)
plt.xlabel('sample points')
plt.ylabel('cubic function')

plt.figure('exp')
plt.plot(x, y4)
plt.xlabel('sample points')

# To reopen am existing figure and add components
plt.figure('exp')
plt.clf()
plt.plot(x, y4)
plt.xlabel('sample points')
plt.ylabel('exp function')
plt.title('exp function')


plt.figure('lin quad')
plt.clf()
plt.plot(x, y1, 'b-', linewidth = 2, label='linear')
plt.plot(x, y2, 'r--', linewidth = 2, label='quad')
plt.legend(loc='upper left')
plt.title('linear vs quad')

plt.figure('cub exp')
plt.clf()
plt.plot(x, y3, 'g+', linewidth = 1.5, label='cubic')
plt.plot(x, y4, 'y*', linewidth = 0.5, label='exp')
plt.legend()
plt.title('cubic vs exp')


plt.figure('lin quad')
plt.clf()
plt.subplot(121)
plt.ylim(0, 900)
plt.plot(x, y1, 'b-', label='linear', linewidth=2.0)
plt.title('linear vs quad')
plt.subplot(122)
plt.ylim(0, 900)
plt.plot(x, y2, 'r', label='quad', linewidth=3.0)


plt.figure('cub exp log')
plt.clf()
plt.plot(x, y3, 'g--', label='cubic', linewidth = 2.0)
plt.plot(x, y4, 'r', label='exponential', linewidth = 4.0)
plt.yscale('log')
plt.legend()
plt.title('cub vs exp')


