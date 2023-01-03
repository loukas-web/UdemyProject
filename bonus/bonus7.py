filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [filename.replace(".", "-") + ".txt" for filename in filenames]

print(filenames)

names = ["john smith", "jay santi", "eva kuki"]
new_names = [name.title() for name in names]
print(new_names)

usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames_count = [len(username) for username in usernames]
print(usernames_count)

user_entries = ["10", "19.1", "20"]
new_user_entries = [float(entrie) for entrie in user_entries]
print(sum(new_user_entries))
