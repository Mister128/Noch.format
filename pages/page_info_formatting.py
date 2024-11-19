import flet as ft
import settings as setti
from flet_route import Params, Basket

class Info_formattingPage:
    def view(self, page: ft.Page, params, basket: Basket):
        page.title="Канон форматирования"

        upper_panel = ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.ARROW_LEFT,
                                on_click=lambda e: page.go("/"),
                                icon_color=setti.accent_color),
                    ft.Text("Сведения о форматировании", size=25)],
                spacing=125
                )
        info= ft.Row([
            ft.Column([
                ft.Text("Заголовок: "),
                ft.Text("Центровка: слева"),
                ft.Text("Стиль: Заголовок 1"),
                ft.Text(f"Размер: {setti.heading_font_size}"),
                ft.Text(f"Шрифт: {setti.heading_font_name}"),
                ft.Text(""),

                ft.Text("Задание: "),
                ft.Text(f"Центровка: справа, с отступом на {setti.task_left_indent} см."),
                ft.Text("Стиль: Заголовок 2"),
                ft.Text(f"Размер: {setti.task_font_size}"),
                ft.Text(f"Шрифт: {setti.task_font_name}")
            ],
            ),
                
            ft.Column([
            ft.Text("Условие: "),
            ft.Text("Центровка: справа"),
            ft.Text("Стиль: Обычный"),
            ft.Text(f"Размер: {setti.condition_font_size}"),
            ft.Text(f"Шрифт: {setti.condition_font_name}"),
            ft.Text(""),
            
            ft.Text("Подпись под ресунком: "),
            ft.Text("Центровка: по центру"),
            ft.Text(f"Стиль: {setti.picture_description_style}"),
            ft.Text(f"Размер: {setti.picture_description_size}"),
            ft.Text(f"Шрифт: {setti.picture_description_name}"),
            ],
            ),
        ],
        spacing=50
        )

        feedback = ft.Container(
            ft.Text("В случае изменений какона форматирования свяжитесь с нами: nochka_group_feedback@list.ru", selectable=True),
            height=200,
            alignment=ft.alignment.bottom_left,
        )
        
        return ft.View(
            '/',
            controls=[
                upper_panel,
                info,
                feedback
            ]
        )