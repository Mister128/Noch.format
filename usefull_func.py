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
                   "show_qiz": settings.show_qiz,
                   "format_file": settings.format_file}
        json.dump(to_json, f)

# Функция выдающая список всех json файлов в папке format_settings.
def files_list(directory):
    return os.listdir(directory)

# Функция загружает параметры форматирования из json в settings.
def load_new_format():
    with open(f"format_settings/{settings.format_file}") as f:
        data = json.load(f)
        settings.list_format_height = float(data["list_format_height"])
        settings.list_format_width = float(data["list_format_width"])

        settings.list_top_margin = float(data["list_top_margin"])
        settings.list_bottom_margin = float(data["list_bottom_margin"])
        settings.list_left_margin = float(data["list_left_margin"])
        settings.list_right_margin = float(data["list_right_margin"])

        settings.heading_font_bold = data["heading_font_bold"]
        settings.heading_font_name = str(data["heading_font_name"])
        settings.heading_font_size = float(data["heading_font_size"])

        settings.task_font_bold = data["task_font_bold"]
        settings.task_font_name = str(data["task_font_name"])
        settings.task_font_size = float(data["task_font_size"])
        settings.task_left_indent = float(data["task_left_indent"])

        settings.condition_font_name = str(data["condition_font_name"])
        settings.condition_font_size = float(data["condition_font_size"])

        settings.picture_description_style = str(data["picture_description_style"])
        settings.picture_description_name = str(data["picture_description_name"])
        settings.picture_description_size = float(data["picture_description_size"])
