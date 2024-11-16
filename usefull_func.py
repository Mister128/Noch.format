import settings
import json
import os

"""
В этом файле находятся полезные функции для разных частей кода. 
Я вынес их в отдельный файл чтобы не загромождать код в файлах страниц приложения.
"""

# Функция редактирования json-файла для сохранения темы и акцентного цвета после выхода из приложения.
def push_changes_to_json():
    # Удаляем существующий json-файл.
    os.remove("preset.json")

    # Создаем и открываем такой же json-файл.
    with open("preset.json", "w") as f:
        # Словарь который мы преобразуем в json-файл с помощью следующей строчки.
        to_json = {"accent_color": settings.accent_color,
                   "theme": settings.theme,
                   "first_name": settings.first_name,
                   "last_name": settings.last_name,
                   "used_once": settings.used_once,
                   "show_qiz": settings.show_qiz}
        json.dump(to_json, f)
