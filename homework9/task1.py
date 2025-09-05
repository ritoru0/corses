import os
import shutil

print(f"Операционная система: {os.name}")  

current_dir = os.getcwd()  
print(f"Текущая рабочая директория: {current_dir}")

files = []
for f in os.listdir(current_dir): 
    if os.path.isfile(os.path.join(current_dir, f)):  
        files.append(f)

extensions = {}
for file in files:
    ext = os.path.splitext(file)[1].lstrip('.').lower()  
    if not ext:
        ext = 'no_extension'  
    if ext not in extensions:
        extensions[ext] = []
    extensions[ext].append(file)

for ext in extensions:
    folder = f"{ext}_files" if ext != 'no_extension' else "no_extension_files"
    folder_path = os.path.join(current_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  
    total_size = 0
    for file in extensions[ext]:
        src = os.path.join(current_dir, file)
        dst = os.path.join(folder_path, file)
        shutil.move(src, dst)  
        total_size += os.path.getsize(dst)  
    print(f"В папке с {ext} файлами перемещено {len(extensions[ext])} файлов, суммарный размер - {total_size / 1024:.2f} КБ")



if extensions:
    first_ext = next(iter(extensions))
    folder = f"{first_ext}_files" if first_ext != 'no_extension' else "no_extension_files"
    folder_path = os.path.join(current_dir, folder)
    files_in_folder = os.listdir(folder_path)
    if files_in_folder:
        old_name = files_in_folder[0]
        new_name = f"some_{old_name}"
        os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))
        print(f"Файл {old_name} был переименован в {new_name}")
