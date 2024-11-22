import flet as ft
import usefull_func
import document_creater
from flet_route import Params, Basket
import settings as setti

"""
В этом файле находится страница(класс страницы) с условиями заданий. 
Здесь используемые функции и элементы управления.
"""

link = """
Нам нужна обратная связь от пользователей! Так что если не трудно,
то перейдите по [ссылке](https://forms.gle/3AVygRZyKY9sQy7e9) и заполните форму. 
Это не займет больше 3 минут вашего времени. Опрос абсолютно анонимен.
"""

class TasksView:
    def view(self, page: ft.Page, params, basket: Basket):
        page.title="Условия заданий"

        # Блок создания функций.-----------------------------------------------

        def close_and_off(e):
            page.close(google_form_message)
            setti.show_qiz = False
            usefull_func.push_changes_to_json()

        # Добавления всех условий заданий в список и создание ворд-файла.
        def commit_and_check(e):
            for textfield in tasks_list.controls:
                setti.tasks_text.append(textfield.value)
            setti.used_once = True
            setti.work_theme = work_theme.content.value
            usefull_func.push_changes_to_json()
            document_creater.create_docx()
            page.open(file_save_alert)
            if setti.show_qiz and setti.used_once:
                page.open(google_form_message)


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

        work_theme = ft.Container(
            ft.TextField(label="Введите тему работы",
                         border_color=setti.accent_color),
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

        # Колонка с текстовыми полями заданий.
        tasks_list = ft.ListView(
            height=340,
            spacing=15,
            padding=10,
            auto_scroll=False
        )

        # Уведомление о сохранении файла.
        file_save_alert = ft.AlertDialog(
            title=ft.Row(
                controls=[
                    ft.Icon(ft.icons.SAVE_ALT,
                            color=setti.accent_color,
                            size=50),
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
        upper_panel = ft.Column([
            ft.Row(
                controls=[ft.IconButton(icon=ft.icons.ARROW_BACK_ROUNDED,
                                        on_click=lambda e: page.go("/"),
                                        icon_color=setti.accent_color),
                        ft.Text("Задания", size=25)],
                spacing=245
            ),
            ft.Divider()
        ]) 
            

        # ---------------------------------------------------------------------
        # Добавление всех элементов управления на страницу.--------------------

        return ft.View(
            '/',
            controls= [
                upper_panel,
                work_theme,
                ft.Divider(),
                ft.Text("Условия заданий:", size=20),
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
