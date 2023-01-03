my_list = [1, 2, 3, 4, 5]


def hello(my_input):
    match my_input:
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case 5:
            return "five"


my_map = map(hello, my_list)
print(list(my_map))

first_list = [1, 2, 3, 4, 5]
second_list = ["one", "two", "three", "four", "five"]
third_list = ["a", "b", "c", "d", "e"]

zipped_list = zip(first_list, second_list, third_list)
print(list(zipped_list))


def count_down(counter=1, final_digit=15, step=1):
    while True:
        yield counter
        counter += step
        if counter > final_digit:
            break


print(list(count_down(100, 1000, 50)))
