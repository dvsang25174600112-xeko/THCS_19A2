import os
root = "my_project"
os.makedirs(os.path.join(root, "src"), exist_ok=True)
os.makedirs(os.path.join(root, "docs"), exist_ok=True)
os.makedirs(os.path.join(root, "data"), exist_ok=True)
open(os.path.join(root, "src", "main.py"), "w", encoding="utf-8").close()
open(os.path.join(root, "docs", "README.md"), "w", encoding="utf-8").close()
open(os.path.join(root, "data", "input.txt"), "w", encoding="utf-8").close()
#In cấu trúc (dùng os.listdir)
print(root + "/")
for folder in os.listdir(root):
    path_folder = os.path.join(root, folder)
    if os.path.isdir(path_folder):
        print("  " + folder + "/")
        for item in os.listdir(path_folder):
            print("    " + item)