import flet as ft
import json
from flet_route import Params, Basket
import settings as setti
import usefull_func

"""
В этом файле находится страница(класс страницы) с настройками. 
Здесь используемые функции и элементы управления.
"""

class SettingsPage:
    def view(self, page: ft.Page, params, basket: Basket):
        page.title="Настройки"

        # Блок создания функций.-----------------------------------------------

        # Функция изменения акцентного цвета.
        def change_color(e):
            setti.accent_color = setti.colors[e.control.value]
            with open("preset.json", "w") as f:
                to_json = {"accent_color": [setti.accent_color]}
                json.dump(to_json, f)

        # Изменение темы
        def theme_changed(e):
            page.theme_mode = (
                "dark"
                if page.theme_mode == "light"
                else "light"
            )
            setti.theme = page.theme_mode
            usefull_func.push_changes_to_json()
            e.control.selected = not e.control.selected
            e.control.update()
            page.update()

        # ---------------------------------------------------------------------
        # Создание переменных для элементов управления.------------------------

        # Кнопка для смены темы.
        theme_button = ft.IconButton(
            icon=ft.icons.DARK_MODE,
            selected_icon=ft.icons.SUNNY,
            on_click=theme_changed,
            selected=False,
            style=ft.ButtonStyle(color={"selected": setti.accent_color, "": setti.accent_color})
        )

        # Кнопка для акцентного цвета.
        button_color = ft.Dropdown(
            border_color=setti.accent_color,
            label="Акцентный цвет",
            hint_text="Выберите цвет",
            on_change=change_color
        )

        # Добавление всех возможных цветов из настроек в варианты.
        for color in setti.colors:
            button_color.options.append(ft.dropdown.Option(color))

        # ---------------------------------------------------------------------
        # Добавление элементов управления на страницу.------------------------

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