from pymediainfo import MediaInfo as mi
import matplotlib.pyplot as plt
import os

path = "/run/media/loukas/DOCKER4/Series Full/Fringe/"

init_lst = os.listdir(path)
second_lst = []
duration = []
duration_new = []
my_dict = {}

for movie in init_lst:
    if ".mkv" in movie:
        second_lst.append(path + movie)

for movie in second_lst:
    file = mi.parse(movie)
    file = file.video_tracks
    duration.append(float(file[0].duration))

for movie in duration:
    duration_new.append(round(float(movie) / 60000))

duration_new = sorted(duration_new)
for movie in duration_new:
    if movie in my_dict:
        my_dict[movie] += 1
    else:
        my_dict[movie] = 1

print(sorted(duration))
print(sorted(duration_new))
print(round(sum(duration) / len(duration) / 60000))
print(my_dict)

plt.bar(my_dict.keys(), my_dict.values())
plt.show()
