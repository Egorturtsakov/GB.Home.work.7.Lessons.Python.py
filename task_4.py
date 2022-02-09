import os

directory = r'.'
groups = [1000, 10000, 100000, 1000000]  # размеры, на какие группы разбивать
groups += [float("inf")]                 # последняя группа для "меньше бесконечности"
result = dict.fromkeys(groups, 0)

# обходим всю иерархию подкаталогов
for path_from_top, subdirs, files in os.walk(directory):
    for file in files:
        path = os.path.join(path_from_top, file)
        size = os.path.getsize(path)
        # вычисляем ближайшее большее число из groups, куда и посчитаем файл
        to_group = min(filter(lambda x: size < x, groups))
        result[to_group] += 1

prev_size = 0
for size in groups:
    print(f"Файлов размером (байт) от {prev_size:10} до {size:10} : {result[size]}")
    prev_size = size