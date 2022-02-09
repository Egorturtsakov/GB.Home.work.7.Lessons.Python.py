import os

path = 'C:/Folder1'
for dirs,folder,files in os.walk(path):
    print('Выбранный каталог: ', dirs)
    print('Вложенные папки: ', folder)
    print('Файлы в папке: ', files)
    print('\n')
    # Отобразит только корневую папку и остановит цикл
    break

# Отобразит первый итерируемый объект
directory = os.walk(path)
print(next(directory))