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
                ft.Text("Центровка: справа"),
                ft.Text("Стиль: Заголовок 1"),
                ft.Text("Размер: 18"),
                ft.Text("Шрифт: Arial"),
                ft.Text(""),

                ft.Text("Задание: "),
                ft.Text("Центровка: справа, с отступом на 1.5 см."),
                ft.Text("Стиль: Заголовок 2"),
                ft.Text("Размер: 16"),
                ft.Text("Шрифт: Arial")
            ],
            ),
                
            ft.Column([
            ft.Text("Условие: "),
            ft.Text("Центровка: справа"),
            ft.Text("Стиль: Обычный"),
            ft.Text("Размер: 14"),
            ft.Text("Шрифт: Times New Roman"),
            ft.Text(""),
            
            ft.Text("Подпись под ресунком: "),
            ft.Text("Центровка: по центру"),
            ft.Text("Стиль: Цитата"),
            ft.Text("Размер: 14"),
            ft.Text("Шрифт: Times New Roman"),
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