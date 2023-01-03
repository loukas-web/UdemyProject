import os

filenames = []
path = "/mnt/usb-WD_My_Passport_25E2_575834314442384B44593955-0:0-part1/Movies/"

files = sorted(os.listdir(path))

for name in files:
    filenames.append(name.replace(".mkv", "").replace("-1", ""))

for i in range(len(filenames) - 1):
    if filenames[i] in filenames[i+1]:
        print(filenames[i])
    