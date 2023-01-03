filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
filenames_new = []
for filename in filenames:
    filenames_new.append(filename.replace(".", "-", 1).replace(" ", "-"))

print(filenames_new)