import flet as ft
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm
from docx.shared import Pt
from docx.shared import RGBColor

def main(page: ft.Page):
    # Окно
    page.title="Noch.ka 2.0"
    page.window_always_on_top
    page.window_width = 700
    page.window_height = 600
    page.window_visible = True
    page.window_resizable = False
    page.update()

    # Цвет
    accent_color = "#05797a"
        
    # Изменение темы на светлую
    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        e.control.selected = not e.control.selected
        e.control.update()
        page.update()
    page.theme_mode = ft.ThemeMode.DARK
    theme = ft.Container(
        ft.IconButton(icon = ft.icons.DARK_MODE, selected_icon=ft.icons.SUNNY,
                    on_click=theme_changed, selected=False),
        alignment=ft.alignment.bottom_right
        )

    # Название
    name = ft.Container(
            ft.Text("Nochka.format", text_align="center", size=50),
            alignment=ft.alignment.top_center,
            bgcolor=accent_color
        )
    
    # Имя и фамилия
    first_name = ft.Container(
            ft.TextField(label="Введите своё имя",
                         border_color=accent_color),
        )

    last_name = ft.Container(
        ft.TextField(label="Введите свою фамилию",
                     border_color=accent_color),
    )
    
    # Текст
    container_variant = ft.Container(
            ft.Text("Выберите вариант работы",
                    size=20),
            margin=ft.margin.only(bottom=-5),
            alignment=ft.alignment.top_center
        )

    # Варианты
    type_work = ft.Dropdown(
        width=700,
        border_color=accent_color,
        hint_text="Выберите тип работы",
        options=[
            ft.dropdown.Option("Занятие"),
            ft.dropdown.Option("Практическая"),
            ft.dropdown.Option("Работа в классе"),
        ],
    )
    
    # Кол-во заданий
    _filter = ft.InputFilter(regex_string=r"^[0-9]*$")
    count_of_task = ft.Container(
        ft.TextField(input_filter=_filter, label="Введите кол-во заданий",
                     border_color=accent_color),
        margin=ft.margin.only(top=10),
        )

    # Есть ли задание 00
    start_task = ft.Container(
        ft.TextField(label="Введите номер начального задания",
                     max_length=2,
                     border_color=accent_color),
    )
    
    # Создать
    # def check_buttons():
        
    create = ft.ElevatedButton("Создать", style=ft.ButtonStyle(shape=ft.StadiumBorder()), disabled=True)
    
    page.add(name, first_name, last_name, container_variant, type_work, count_of_task, start_task, create, theme)


ft.app(main)