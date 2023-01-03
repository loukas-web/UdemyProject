import random
import matplotlib.pyplot as plt

my_marks = []

for i in range(11000000):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    if abs(a - b) < 13:
        my_marks.append(a + b)
    else:
        c = random.randint(0, 100)
        temp_marks = sorted([a, b, c])
        my_marks.append(sum(temp_marks[:1]))

my_marks = sorted(my_marks)

my_dict = {}
for i in my_marks:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

# print(my_marks)
# print(my_dict)

plt.bar(my_dict.keys(), my_dict.values())
plt.title("Hello World")
plt.show()
