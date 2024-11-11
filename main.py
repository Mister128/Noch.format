import flet as ft
from router import Router

def main(page: ft.Page):

    # Инициализация настроек приложения
    page.theme_mode = ft.ThemeMode.DARK

    # Вызов основного класса приложения, отвечающего за маршрутизацию
    Router(page)


if __name__ == '__main__':
    ft.app(target=main)