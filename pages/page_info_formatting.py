import flet as ft
import settings as setti
import usefull_func
from flet_route import Params, Basket

class Info_formattingPage:
    def view(self, page: ft.Page, params, basket: Basket):
        page.title="Правила форматирования"

        # Блок создания функций.-----------------------------------------------

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
                    ft.Text("Сведения о форматировании", size=25),
                    ft.IconButton(
                        icon=ft.icons.DARK_MODE,
                        selected_icon=ft.icons.SUNNY,
                        on_click=theme_changed,
                        selected=False,
                        style=ft.ButtonStyle(color={"selected": setti.accent_color, "": setti.accent_color})
                    ),
                ],
                spacing=125
            ),
            ft.Divider()
        ]) 
        
        # Инормация о форматировании
        info= ft.Row([
                ft.Column([
                    ft.Text("Заголовок: ", color=setti.accent_color),
                    ft.Text("Центровка: слева"),
                    ft.Text("Стиль: Заголовок 1"),
                    ft.Text(f"Размер: {setti.heading_font_size}"),
                    ft.Text(f"Шрифт: {setti.heading_font_name}"),
                    ft.Text(""),

                    ft.Text("Задание: ", color=setti.accent_color),
                    ft.Text(f"Центровка: слева,\n с отступом на {setti.task_left_indent} см."),
                    ft.Text("Стиль: Заголовок 2"),
                    ft.Text(f"Размер: {setti.task_font_size}"),
                    ft.Text(f"Шрифт: {setti.task_font_name}")
                ],
                ),
                    
                ft.Column([
                ft.Text("Условие: ", color=setti.accent_color),
                ft.Text("Центровка: слева"),
                ft.Text("Стиль: Обычный"),
                ft.Text(f"Размер: {setti.condition_font_size}"),
                ft.Text(f"Шрифт: {setti.condition_font_name}"),
                ft.Text(""),
                
                ft.Text("Подпись под рисунком: ", color=setti.accent_color),
                ft.Text("Центровка: по центру"),
                ft.Text(f"Стиль: {setti.picture_description_style}"),
                ft.Text(f"Размер: {setti.picture_description_size}"),
                ft.Text(f"Шрифт: {setti.picture_description_name}"),
                ],
                ),
            ],
            height=400,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=200,
            )
        
        # Почта
        feedback = ft.Container(
            ft.Text("В случае изменений правил форматирования свяжитесь с нами: nochka_group_feedback@list.ru", selectable=True),
            height=110,
            alignment=ft.alignment.bottom_left
        )
        
        # ---------------------------------------------------------------------
        # Добавление элементов управления на страницу.-------------------------

        return ft.View(
            '/',
            controls=[
                upper_panel,
                info,
                feedback
            ]
        )