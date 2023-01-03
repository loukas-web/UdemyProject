import random
import matplotlib.pyplot as plt

lst = sorted(list(random.randint(0, 10) for _ in range(4000)))

d = {}

for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1


xpoints = d.keys()
ypoints = d.values()

# plt.plot(xpoints, ypoints, marker="X")
# plt.bar(xpoints, ypoints)
# plt.hist(xpoints)
plt.pie(ypoints, labels=xpoints)
plt.show()
