import os

print('Операционная система:', os.environ['OS'])
print('Имя компьютера:', os.environ['COMPUTERNAME'])
print('Имя пользователя:', os.getlogin())
