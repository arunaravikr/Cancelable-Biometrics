import matplotlib.pyplot as plt
import numpy as np

far = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
frr = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

plt.plot(far) 
plt.plot(frr[::-1])
plt.axvline(x=3, color='r', linestyle='--')
plt.axhline(y=25, color='r', linestyle='--')
plt.show()
