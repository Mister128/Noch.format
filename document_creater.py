import re
import settings
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm
from docx.shared import Pt
from docx.shared import RGBColor

"""
В этом файле находятся функции для создания ворд файла. 
Я вынес их в отдельный файл чтобы не загромождать код в файлах страниц приложения.
"""

# Функция форматирования текста задания, которая убирает лишние пробелы и переносы строк.
def text_formater(text):
    text = re.sub(r'\s+', ' ', text)
    return text

# Основная функция создания ворд файла.
def create_docx():
    document = Document()

    # Инициализация.------------------------------------------------------

    # fln = f"{first_name.content.value} {last_name.content.value}"
    # tow = str(type_work.value)
    # now = str(number_of_work.content.value)
    # cot = int(count_of_task.content.value)
    # st = int(start_task.content.value)

    # ---------------------------------------------------------------------
    # Автор.---------------------------------------------------------------

    # Кто создал документ.
    core_properties = document.core_properties
    core_properties.author = settings.first_and_last_name

    # Кто редактировал документ.
    last_modified_by = document.core_properties
    last_modified_by.last_modified_by = settings.first_and_last_name

    # Комментарий.
    comments = document.core_properties
    comments.comments = " "

    # ---------------------------------------------------------------------
    # Разметка страницы.---------------------------------------------------

    sections = document.sections

    # Цикл для изменения формата каждой страницы.
    for section in sections:
        # Изменения формата листа на A4 для каждой страницы.
        section.page_height = Cm(29.7)
        section.page_width = Cm(21)
        # Изменение полей листа.
        section.top_margin = Cm(2)
        section.bottom_margin = Cm(2)
        section.left_margin = Cm(3)
        section.right_margin = Cm(1.5)

    # ---------------------------------------------------------------------
    # Заглавие.------------------------------------------------------------

    main_heading = document.add_heading()
    # Добавление заголовка с типом работы и ее номером.
    run = main_heading.add_run(f"{settings.type_of_work} {settings.work_number}")

    # Указание стиля шрифта.

    font = run.font
    # Жирный шрифт или нет.
    font.bold = False
    # Название шрифта.
    font.name = "Arial"
    # Размер шрифта.
    font.size = Pt(18)
    # Цвет шрифта.
    font.color.rgb = RGBColor(0, 0, 0)

    # ---------------------------------------------------------------------
    # Создание заданий.----------------------------------------------------

    # Счетчик итераций цикла.
    inter = 0

    # Цикл для создания и форматирования заданий.
    for i in range(settings.start_task - 1, settings.count_of_task):
        # Установка уровня заголовка для задания.
        task_heading = document.add_heading(level=2)
        # Указание номера задания в нужном формате в зависимости от значения.
        if i < 9:
            run = task_heading.add_run("Задание 0" + str(i + 1))
        else:
            run = task_heading.add_run("Задание " + str(i + 1))

        # Указание стиля шрифта.-----------------------------------------------

        font = run.font
        # Жирный шрифт или нет.
        font.bold = False
        # Название шрифта.
        font.name = "Arial"
        # Размер шрифта.
        font.size = Pt(16)
        # Цвет шрифта.
        font.color.rgb = RGBColor(0, 0, 0)

        paragraph_format = task_heading.paragraph_format
        # Добавление отступа для заголовка задания.
        paragraph_format.left_indent = Cm(1.5)

        # ---------------------------------------------------------------------
        # Условие.-------------------------------------------------------------

        if_paragraph = document.add_paragraph()
        # Разметка текста по ширине.
        if_paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        # Добавление текста с условием задания.
        run = if_paragraph.add_run(f"Условие: {text_formater(settings.tasks_text[inter])}")

        # Стиль шрифта.

        font = run.font
        # Название шрифта.
        font.name = "Times New Roman"
        # Размер шрифта.
        font.size = Pt(14)

        # ---------------------------------------------------------------------
        # Описание картинки.---------------------------------------------------

        picture_description = document.add_paragraph()
        # Присвоение стиля для текста.
        picture_description.style = "Quote"
        # Разметка текста по центру.
        picture_description.alignment = WD_ALIGN_PARAGRAPH.CENTER
        # Добавление текста подписи рисунка.
        run = picture_description.add_run("Рис " + str(i + 1) + ". ")

        # Стиль шрифта.

        font = run.font
        # Название шрифта.
        font.name = "Times New Roman"
        # Размер шрифта.
        font.size = Pt(12)

        # ---------------------------------------------------------------------

        # Увеличение счетчика итераций цикла на 1.
        inter += 1

    # ---------------------------------------------------------------------
    # Сохранения документа.------------------------------------------------

    # Сохраняет туда же, где находится и сам этот файл
    document.save(f"{settings.type_of_work} {settings.work_number}.docx")
