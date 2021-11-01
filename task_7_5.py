import os
import json
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append((file_path.split('.')[-1], os.stat(file_path).st_size))
max_size = max(files, key=lambda x: x[1])[1]
n = 1
my_list = {}
for _ in range(len(str(max_size))):
    n *= 10
    my_list[n] = (0, [])
for file in files:
    num, ext_list = my_list[10 ** len(str(file[1]))]
    ext_list.append(file[0])
    ext_list = list(set(ext_list))
    my_list[10 ** len(str(file[1]))] = (num + 1, ext_list)
print(my_list)
with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as f_json:
    json.dump(my_list, f_json)