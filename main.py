import flet as ft
from router import Router
import settings
import json

def main(page: ft.Page):

    # Инициализация настроек приложения
    page.theme_mode = settings.theme

    with open("preset.json") as f:
        data = json.load(f)
        settings.accent_color = str(data["accent_color"])
        settings.theme = str(data["theme"])
        settings.first_name = str(data["first_name"])
        settings.last_name = str(data["last_name"])

    # Инициализация настроек форматирования
    with open("format_settings/preset_format.json") as f:
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

    page.theme_mode = settings.theme

    # Вызов основного класса приложения, отвечающего за маршрутизацию
    Router(page)


if __name__ == '__main__':
    ft.app(target=main)