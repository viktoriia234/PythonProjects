import os

if not os.path.exists('target'):
    os.mkdir('target')

for i in range(1, 11):
    folder_name = str(i)
    folder_path = os.path.join('target', folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
