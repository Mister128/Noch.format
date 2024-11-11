import flet as ft
from flet_route import Params, Basket

# Акцентный цвет
accent_color = "cyan"

class Settings_Page:
    def view(self, page: ft.Page, params, basket: Basket):
        page.title="Настроечки"
        
        global button_color
        button_color = ft.Dropdown(width=700,
            border_color=accent_color,
            hint_text="Выберите цвет",
            options=[
                ft.dropdown.Option("Циановый"),
                ft.dropdown.Option("Зелёный"),
                ft.dropdown.Option("Фиолетовый"),
            ],)

        return ft.View(
            '/',
            controls= [
                button_color,
                ft.ElevatedButton("Назад", on_click=lambda e: page.go('/'))
            ]
        )