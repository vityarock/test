import os
path_set = []
count = 0
with open("out.txt", "a") as out:
    for root, dirs, files in os.walk("main"):
        for file in files:
            if file.endswith(".py"):
                count += 1
                file_path = os.path.join(root, file)
                path = os.path.dirname(file_path)
                path = path.replace('\\', '/')
                if path not in path_set and path != "":
                    path_set.append(path)
    path_set.sort()
    for item in path_set:
        out.write(item + '\n')

# import os
# with open("out.txt", "w") as f:
#     for curdir, dirs, files in os.walk("main"):
#         if (any(str.endswith(x, ".py") for x in files)):
#             f.write(curdir + "\n")