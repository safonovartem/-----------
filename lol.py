import os
import csv

# Путь к директории с изображениями
images_dir = 'images'

# Путь к результирующему CSV-файлу
output_file = 'result.csv'

# Заголовки для CSV
header = [
    'Имя директории с изображениями',
    'Кол-во коробок типа laptop',
    'Кол-во коробок типа tablet',
    'Кол-во коробок типа group_box'
]

# Открываем CSV-файл для записи
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)

    # Перебираем все папки в директории
    for folder in os.listdir(images_dir):
        if folder.startswith('pallet_'):
            try:
                # Извлекаем числа из имени папки
                _, laptop, tablet, group_box = folder.split('_')
                writer.writerow([folder, int(laptop), int(tablet), int(group_box)])
            except ValueError:
                print(f"Пропущена папка с неверным форматом имени: {folder}")
