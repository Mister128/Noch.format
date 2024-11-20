import flet as ft
from flet_route import Params, Basket
import settings as setti
import usefull_func

"""
В этом файле находится страница(класс страницы) с настройками. 
Здесь используемые функции и элементы управления.
"""

link = """
Нам нужна обратная связь от пользователей! Так что если не трудно,
то перейдите по [ссылке](https://forms.gle/3AVygRZyKY9sQy7e9) и заполните форму. 
Это не займет больше 3 минут вашего времени. Опрос абсолютно анонимен.
"""

class SettingsPage:
    def view(self, page: ft.Page, params, basket: Basket):
        page.title="Настройки"

        # Блок создания функций.-----------------------------------------------

        def close_and_off(e):
            page.close(google_form_message)
            setti.show_qiz = False
            usefull_func.push_changes_to_json()

        # Закрытие страницы и всех всплывающих элементов.
        def settings_close(e):
            page.open(google_form_message)
            page.close(google_form_message)
            page.go("/")

        # Функция изменения акцентного цвета.
        def change_color(e):
            setti.accent_color = setti.colors[e.control.value]
            usefull_func.push_changes_to_json()
            if setti.show_qiz and setti.used_once:
                page.open(google_form_message)
            page.update()

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

        # Кнопка назад
        upper_panel = ft.Column([
            ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED,
                                on_click=lambda e: page.go("/"),
                                icon_color=setti.accent_color),
                    ft.Text("Настройки", size=25)
                ],
                spacing=220
            ),
            ft.Divider()
        ])

        # Кнопка для смены темы.
        theme_button = ft.Container(
            ft.IconButton(
                icon=ft.icons.DARK_MODE,
                selected_icon=ft.icons.SUNNY,
                on_click=theme_changed,
                selected=False,
                style=ft.ButtonStyle(color={"selected": setti.accent_color, "": setti.accent_color})
            ),
            alignment=ft.alignment.top_right
        )

        # Баннер о просьбе пройти опрос.
        google_form_message = ft.Banner(
            content=ft.Container(
                padding=15,
                content=ft.Column(
                    tight=True,
                    controls=[
                        ft.Markdown(
                            link,
                            selectable=True,
                            on_tap_link=lambda e: page.launch_url(e.data),
                            md_style_sheet=ft.MarkdownStyleSheet(
                                p_text_style=ft.TextStyle(size=17),
                                a_text_style=ft.TextStyle(color=setti.accent_color)
                            )
                        )
                    ],
                ),
            ),
            actions=[
                ft.TextButton(
                    text="Закрыть",
                    on_click=lambda e: page.close(google_form_message),
                    style=ft.ButtonStyle(color=setti.accent_color)
                ),
                ft.TextButton(
                    text="Закрыть и больше не показывать",
                    on_click=close_and_off,
                    style=ft.ButtonStyle(color=setti.accent_color)
                ),
            ],
        )



        # Кнопка для акцентного цвета.
        button_color = ft.Dropdown(
            border_color=setti.accent_color,
            label="Акцентный цвет",
            hint_text="Выберите цвет",
            on_change=change_color,
        )

        # Добавление всех возможных цветов из настроек в варианты.
        for color in setti.colors:
            button_color.options.append(ft.dropdown.Option(color, text_style=ft.TextStyle(color=setti.colors[color])))

        # ---------------------------------------------------------------------
        # Добавление элементов управления на страницу.------------------------

        return ft.View(
            '/',
            controls= [
                upper_panel,
                button_color,
                theme_button
            ]
        )