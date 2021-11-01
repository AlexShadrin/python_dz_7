import os
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)
n = 1
my_list = {}
for _ in range(len(str(max_size))):
    n *= 10
    my_list[n] = 0
for file in files:
        my_list[10 ** len(str(file))] += 1
print(my_list)