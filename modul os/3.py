import os

def rename_folders(folder_path):
    for folder_name in os.listdir(folder_path):
        if folder_name.isdigit():
            folder_num = int(folder_name)
            if folder_num % 2 == 0:
                new_name = 'new_folder_' + str(folder_num)
                os.rename(os.path.join(folder_path, folder_name),
                          os.path.join(folder_path, new_name))

target_path = 'target'
if os.path.exists(target_path):
    rename_folders(target_path)
