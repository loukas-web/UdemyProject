import csv

with open("weather.csv", "r") as file:
    data = list(csv.reader(file))

print(data[1:])

a, b = zip(*data[1:])

print(a, b)
