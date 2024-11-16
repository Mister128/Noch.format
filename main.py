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
        settings.used_once = data["used_once"]
        settings.show_qiz = data["show_qiz"]

    page.theme_mode = settings.theme

    # Вызов основного класса приложения, отвечающего за маршрутизацию
    Router(page)


if __name__ == '__main__':
    ft.app(target=main)