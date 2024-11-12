import flet as ft
from router import Router
import settings as setti
import json

def main(page: ft.Page):

    # Инициализация настроек приложения
    page.theme_mode = ft.ThemeMode.DARK

    with open("preset.json") as f:
        data = json.load(f)
        setti.accent_color = str(data["accent_color"])[2:-2:]

    # Вызов основного класса приложения, отвечающего за маршрутизацию
    Router(page)


if __name__ == '__main__':
    ft.app(target=main)