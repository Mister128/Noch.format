import flet as ft
import usefull_func
import document_creater
from flet_route import Params, Basket
import settings as setti

"""
В этом файле находится страница(класс страницы) с условиями заданий. 
Здесь используемые функции и элементы управления.
"""

class TasksView:
    def view(self, page: ft.Page, params, basket: Basket):
        page.title="Условия заданий"

        # Блок создания функций.-----------------------------------------------

        # Добавления всех условий заданий в список и создание ворд-файла.
        def commit_and_check(e):
            for textfield in tasks_list.controls:
                setti.tasks_text.append(textfield.value)
            usefull_func.push_changes_to_json()
            print(f"first_name - {setti.first_name}, last_name - {setti.last_name}")
            document_creater.create_docx()
            page.open(file_save_alert)


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

        # ---------------------------------------------------------------------
        # Создание переменных для элементов управления.------------------------

        # Колонка с текстовыми полями заданий.
        tasks_list = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            auto_scroll=False,
            scroll=ft.ScrollMode.ALWAYS
        )

        # Уведомление о сохранении файла.
        file_save_alert = ft.AlertDialog(
            title=ft.Row(
                controls=[
                    ft.Icon(ft.icons.SAVE_ALT,
                            color=setti.accent_color),
                    ft.Text("Файл сохранен в этой же папке!")]
            )
        )

        # Добавление текстовых полей в соответствии с кол-вом заданий.
        for n in range(setti.start_task, setti.count_of_task + 1):
            tasks_list.controls.append(ft.TextField(label=f"Условие задания {n}",
                                                    multiline=True,
                                                    border_color=setti.accent_color))

        # Кнопка смены темы.
        theme_button = ft.IconButton(
            icon=ft.icons.DARK_MODE,
            selected_icon=ft.icons.SUNNY,
            on_click=theme_changed,
            selected=False,
            style=ft.ButtonStyle(color={"selected": setti.accent_color, "": setti.accent_color})
        )

        # Верхняя панель с кнопкой назад и текстом.
        upper_panel = ft.Row(
            controls=[ft.IconButton(icon=ft.icons.ARROW_LEFT,
                                    on_click=lambda e: page.go("/"),
                                    icon_color=setti.accent_color),
                      ft.Text("Задания", size=25)],
            spacing=245
            )


        # ---------------------------------------------------------------------
        # Добавление всех элементов управления на страницу.--------------------

        return ft.View(
            '/',
            controls= [
                upper_panel,
                tasks_list,
                ft.Row([ft.ElevatedButton(
                            "Создать",
                            on_click=commit_and_check,
                            color=setti.accent_color
                        ),
                        theme_button
                        ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
            ]
        )