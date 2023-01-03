import matplotlib.pyplot as plt

my_dict = {}

for a in range(101):
    for b in range(101):
        if abs(a - b) > 12:
            for c in range(101):
                temp = sorted([a, b, c])
                my_sum = sum(temp[1:])
                if my_sum in my_dict:
                    my_dict[my_sum] += 1
                else:
                    my_dict[my_sum] = 1
        else:
            my_sum = a + b
            if my_sum in my_dict:
                my_dict[my_sum] += 1
            else:
                my_dict[my_sum] = 1

print(my_dict)

plt.plot(my_dict.keys(), my_dict.values(), marker="X")
plt.show()
