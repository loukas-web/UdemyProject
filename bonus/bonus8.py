date = input("Enter today's date: ")
mood = input("Mood 1 to 10: ")
thougths = input("Thoughts:\n")

with open(f"files/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thougths)

count_heads = 0
count = 0

while True:
    counter = input("Throw the coin head or tail : ")
    
    match counter:
        case "heads":
            count_heads += 1
            count += 1
        case "tails":
            count += 1
        case "exit":
            break
    
    print(f"Heads: {count_heads * 100 / count}%")
