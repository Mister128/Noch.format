import flet as ft
import json
from flet_route import Params, Basket
import settings as setti

class SettingsPage:
    def view(self, page: ft.Page, params, basket: Basket):
        page.title="Настройки"

        def change_color(e):
            setti.accent_color = setti.colors[e.control.value]
            with open("preset.json", "w") as f:
                to_json = {"accent_color": [setti.accent_color]}
                json.dump(to_json, f)

        # Изменение темы
        def theme_changed(e):
            page.theme_mode = (
                ft.ThemeMode.DARK
                if page.theme_mode == ft.ThemeMode.LIGHT
                else ft.ThemeMode.LIGHT
            )
            e.control.selected = not e.control.selected
            e.control.update()
            page.update()

        theme_button = ft.IconButton(
            icon=ft.icons.DARK_MODE,
            selected_icon=ft.icons.SUNNY,
            on_click=theme_changed,
            selected=False,
            style=ft.ButtonStyle(color={"selected": setti.accent_color, "": setti.accent_color})
        )

        button_color = ft.Dropdown(
            width=700,
            border_color=setti.accent_color,
            label="Акцентный цвет",
            hint_text="Выберите цвет",
            on_change=change_color
        )

        # Добавление всех возможных цветов в варианты
        for color in setti.colors:
            button_color.options.append(ft.dropdown.Option(color))


        return ft.View(
            '/',
            controls= [
                ft.Container(ft.Text("Настройки", size=25),
                        alignment=ft.alignment.top_center),
                button_color,
                ft.Row([
                    ft.ElevatedButton("Назад", on_click=lambda e: page.go('/'), color=setti.accent_color),
                    theme_button],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ]
        )