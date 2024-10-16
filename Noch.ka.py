from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm
from docx.shared import Pt
from docx.shared import RGBColor
document = Document()


au = input('Введите имя и фамилию автора (т.е. себя): ')
core_properties = document.core_properties
core_properties.author = au
last_modified_by = document.core_properties
last_modified_by.last_modified_by = au
print('-----')


o = int(input('Введите номер с которого начинаются задания (0 или 1): '))
print('-----')

m = int(input('Введите количество заданий: '))
print('-----')

Indentation = 0

#------------------------------------------------------------Начало корневого заголовка
main_heading = document.add_heading()
g = input('Вставте название главного заголовка целиком: ')
run = main_heading.add_run(g)
font = run.font
font.bold = True
font.name = 'Calibri'
font.size = Pt(18)
font.color.rgb = RGBColor(0, 0, 0)


for i in range(o - 1, m):
    task_heading = document.add_heading(level = 2)
    if (i < 9):
        run = task_heading.add_run('Задание 0' + str(i + 1))
    else:
        run = task_heading.add_run('Задание ' + str(i + 1))
    Indentation += 1
    font = run.font
    font.bold = True
    font.name = 'Calibri'
    font.size = Pt(16)
    font.color.rgb = RGBColor(0, 0, 0)
    paragraph_format = task_heading.paragraph_format
    paragraph_format.left_indent
    paragraph_format.left_indent = Cm(1.5 * Indentation)
    paragraph_format.left_indent

#------------------------------------------------------------Начало условий
    con = input(f'Введите условие {i + 1}: ')
    print('-----')
    if_paragraph = document.add_paragraph()
    run = if_paragraph.add_run(f'Условие: {con}')
    font = run.font
    font.italic = True
    font.name = 'Century'
    font.size = Pt(14)

#------------------------------------------------------------Начало основного текста
    text = input(f'Введите основной текст задания {i + 1} (При создании шаблона, оставить пустым): ')
    print('-----')
    text_paragraph = document.add_paragraph()
    run = text_paragraph.add_run(f'{text}')
    font = run.font
    font.italic = False
    font.name = 'Century'
    font.size = Pt(14)

#------------------------------------------------------------Начало описаний рисунков
    c = input(f'Описание {i + 1} рисунка (Если рисунка нет, оставить поле пустым): ')
    print('-----')
    if not(not c):#Не спрашивайте почему not(not c). В голову только это =)
        picture_description = document.add_paragraph()
        picture_description.style = 'Quote'
        run = picture_description.add_run(f'Рис {str(i + 1)}. "{c}"')
        font = run.font
        font.name = 'Century'
        font.size = Pt(12)

        
v = g.split('.')[0]
document.save(f'{v}.docx')