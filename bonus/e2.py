import csv
from matplotlib import pyplot as plt
from datetime import datetime

stats = {}
lst = []

with open("report.csv", "r") as file:
    data = list(csv.reader(file))

for i in data[1:]:
    lst.append([i[2], int(i[0])])

lst.sort()
for item in lst:
    if item[0] in stats:
        stats[item[0]] += item[1]
    else:
        stats[item[0]] = item[1]

x = list(stats.keys())
y = list(stats.values())

time_str = str(data[1000][5][11:-6])
print(time_str)
print(type(time_str))
time_object = datetime.strptime(time_str, '%H:%M:%S').time()
print(time_object)
print(type(time_object))
date_str = str(data[1000][5][:10])
print(date_str)
date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
print(date_object)
print(type(date_object))

plt.bar(x, y)
plt.show()

