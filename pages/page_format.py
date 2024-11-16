import flet as ft
import usefull_func
import settings as setti
from flet_route import Params, Basket

from settings import first_name, work_number

"""
В этом файле находится страница(класс страницы) с данными форматирования. 
Здесь используемые функции и элементы управления.
"""

class NochkaPage:
    def view(self, page: ft.Page, params, basket: Basket):

        # Настройка окна приложения.-------------------------------------------

        page.title="Noch.ka 1.4.0"
        page.window_width = 700
        page.window_height = 650
        page.window_visible = True
        page.window_resizable = False
        page.update()

        # ---------------------------------------------------------------------
        # Инициализация переменных.--------------------------------------------

        # Фильтр текста
        _filter = ft.InputFilter(regex_string=r"^[0-9]*$")

        # ---------------------------------------------------------------------
        # Блок создания функций.-----------------------------------------------

        # Сохраняет введенные значения перед переходом в настройки.
        def go_to_settings(e):
            setti.first_name = first_name.content.value
            setti.last_name = last_name.content.value
            setti.type_of_work = type_work.value
            setti.work_number = number_of_work.content.value
            setti.count_of_task = count_of_task.content.value
            setti.start_task = start_task.content.value
            page.go("/settings")
            
        # Изменение темы.
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

        # Проверка заполнения данных в поля.
        def commit_and_check(e):
            filled_data = 0
            if first_name.content.value != "" and last_name.content.value != "":
                setti.first_name = first_name.content.value
                setti.last_name = last_name.content.value
                filled_data += 1

            if type_work.value != None:
                setti.type_of_work = f"{type_work.value}"
                filled_data += 1

            if number_of_work.content.value != "":
                setti.work_number = f"{number_of_work.content.value}"
                filled_data += 1

            if count_of_task.content.value != "":
                setti.count_of_task = int(count_of_task.content.value)
                filled_data += 1

            if start_task.content.value != "":
                setti.start_task = int(start_task.content.value)
                filled_data += 1

            if filled_data == 5 and int(count_of_task.content.value) >= int(start_task.content.value):
                page.go('/tasks')
            else:
                page.open(check_info_alert)

        # ---------------------------------------------------------------------
        # Создание переменных для элементов управления.------------------------

        # Линия с кнопкой выхода из настроек и кнопка смены темы.
        settings = ft.Row([
            ft.IconButton(
                icon=ft.icons.SETTINGS,
                on_click=go_to_settings,
                style=ft.ButtonStyle(color=setti.accent_color)
                ),
            ft.IconButton(
                icon = ft.icons.DARK_MODE,
                selected_icon=ft.icons.SUNNY,
                on_click=theme_changed,
                selected=False,
                style=ft.ButtonStyle(color={"selected": setti.accent_color, "": setti.accent_color})
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        # Уведомление о не введенных данных.
        check_info_alert = ft.AlertDialog(
            title=ft.Row(
                controls=[
                    ft.Icon(ft.icons.WARNING_SHARP,
                            color=setti.accent_color,
                            size=50),
                    ft.Text("Некоторые данные не заполнены\n"
                            "или заполнены неправильно!")]
            )
        )

        # Название
        name = ft.Container(
                ft.Text("Nochka.format", text_align="center", size=50),
                alignment=ft.alignment.top_center,
                bgcolor=setti.accent_color
            )
        
        # Имя и фамилия
        first_name = ft.Container(
                ft.TextField(label="Введите своё имя",
                             border_color=setti.accent_color),
            )

        last_name = ft.Container(
            ft.TextField(label="Введите свою фамилию",
                         border_color=setti.accent_color),
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
            border_color=setti.accent_color,
            hint_text="Выберите тип работы",
            options=[
                ft.dropdown.Option("Занятие"),
                ft.dropdown.Option("Практическая работа"),
                ft.dropdown.Option("Работа в классе"),
            ],
        )

        # Номер работы
        number_of_work = ft.Container(
            ft.TextField(label="Введите номер работы",
                         input_filter=_filter,
                         border_color=setti.accent_color),
            margin=ft.margin.only(top=10),
        )

        # Кол-во заданий
        count_of_task = ft.Container(
            ft.TextField(label="Введите кол-во заданий",
                         input_filter=_filter,
                         max_length=3,
                         border_color=setti.accent_color)
            )

        # Номер начального задания
        start_task = ft.Container(
            ft.TextField(label="Введите номер начального задания",
                         input_filter=_filter,
                         max_length=2,
                         border_color=setti.accent_color),
        )

        # Кнопка создания файла
        create = ft.ElevatedButton(
            "Продолжить",
            style=ft.ButtonStyle(shape=ft.StadiumBorder()),
            color=setti.accent_color,
            on_click=commit_and_check,
            disabled=False
        )

        # ---------------------------------------------------------------------
        # Задание базовых значений.--------------------------------------------

        first_name.content.value = setti.first_name
        last_name.content.value = setti.last_name
        type_work.value = setti.type_of_work
        number_of_work.content.value = setti.work_number
        count_of_task.content.value = setti.count_of_task
        start_task.content.value = setti.start_task

        # ---------------------------------------------------------------------
        # Добавление всех элементов управления на страницу.--------------------

        return ft.View(
            '/',
            controls=[name, first_name, last_name, container_variant, type_work, number_of_work,
                    count_of_task, start_task, create, settings]
            )
