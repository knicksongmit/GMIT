# Sources:
# https://realpython.com/how-to-use-numpy-arange/
# https://gist.github.com/aunyks/44648b839e7c59b47afecca62c9a88de


import numpy as np
import matplotlib.pyplot as plt

# Create functions
x = np.arange(0, 4)  # Start, Stop

f = x
g = x**2
h = x**3

# Plot functions
plt.plot(f, 'r')
plt.plot(g, 'b')
plt.plot(h, 'g')

# Plot configuration
plt.legend(['f(x)=x', 'g(x)=x2', 'h(x)=x3'], loc='upper left')
plt.grid()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Function Plot')
plt.show()