import matplotlib.pyplot as plt
import numpy as np

x = np.array([range(10)])
y = x/9*5+32

print(x.tolist())
print(y)

plt.plot(x.tolist(), y)
plt.show()
