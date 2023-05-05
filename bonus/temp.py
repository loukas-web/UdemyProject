import random as r

a = [r.randint(0, 100)]
a.append(r.randint(0, 100 - sum(a)))
a.append(r.randint(0, 100 - sum(a)))
a.append(100 - sum(a))
a.sort(reverse=True)

print(a)

joker_list = list(range(1, 46))
joker = list(range(1, 21))
print(joker_list, joker)

print(r.choice(joker))