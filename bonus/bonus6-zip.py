contents = ["Hello",
            "How Are You",
            "GoodBye"]

filenames = ["doc.txt",
             "report.txt",
             "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", "w")
    file.write(content)

a = "I am a string " \
    "on my " \
    "own"
