with open("files/doc.txt") as file:  # by default open function opens file as read
    print(file.read())

with open("files/doc.txt") as file:  # by default open function opens file as read
    print("Hello")

# print(file.read()) file closes when using with

with open("files/doc.txt") as file:  # by default open function opens file as read
    content = file.read()
    
print(content)
