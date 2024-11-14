import flet as ft
import document_creater
from flet_route import Params, Basket
import settings as setti


class TasksView:
    def view(self, page: ft.Page, params, basket: Basket):
        page.title="Условия заданий"

        # Блок создания функций

        def commit_and_check(e):
            for textfield in tasks_list.controls:
                setti.tasks_text.append(textfield.value)
            document_creater.create_docx()

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

        tasks_list = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                               auto_scroll=False,
                               scroll=ft.ScrollMode.ALWAYS,
                               width=700)

        for n in range(setti.start_task, setti.count_of_task + 1):
            tasks_list.controls.append(ft.TextField(label=f"Условие задания {n}",
                                                    multiline=True,
                                                    border_color=setti.accent_color))

        theme_button = ft.IconButton(
            icon=ft.icons.DARK_MODE,
            selected_icon=ft.icons.SUNNY,
            on_click=theme_changed,
            selected=False,
            style=ft.ButtonStyle(color={"selected": setti.accent_color, "": setti.accent_color})
        )



        return ft.View(
            '/',
            controls= [
                ft.Container(ft.Text("Задания", size=25),
                        alignment=ft.alignment.top_center
                ),
                tasks_list,
                ft.Row([
                    ft.ElevatedButton("Создать", on_click=commit_and_check, color=setti.accent_color),
                    theme_button],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
            ]
        )