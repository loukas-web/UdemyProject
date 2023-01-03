import webbrowser

user_term = input("Enter search term: ")

user_term = user_term.replace(" ", "+")

print(user_term)

webbrowser.open("https://google.com/search?q=" + user_term)
