from PIL import Image
import random
import os
import pyautogui as pg
import PySimpleGUI as sg
from tkinter import messagebox as mb
import pyautogui as pg


def create_rgb_image(width, height, name, ext):
    image = Image.new("RGB", (width, height))
    pixels = []
    for _ in range(height):
        for _ in range(width):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            pixels.append((r, g, b))
    image.putdata(pixels)
    #image.save(f"{path}\\{name}.{ext}")
    image.save(f"{name}.{ext}")

sg.theme('darkblue17')
layout = [ [sg.Text('ДеГенератор картинок!', font=('YEARBOOK', 20))],
            [sg.Push(), sg.Text("Ширина: "), sg.InputText("1000", size=(10)), sg.Push()],
            [sg.Push(), sg.Text("Высота: "), sg.InputText("1000", size=(10)), sg.Push()],
            [sg.Push(), sg.Text("Имя: "), sg.InputText("image", size=(10)), sg.Push()],
            [sg.Push(), sg.Text("Расширение: "), sg.Combo(['png', 'jpg', 'WebP', 'ico', 'bmp'], default_value='png'), sg.Push()],
            [sg.Button('Отмена', button_color='#613434'), sg.Push(), sg.Button('ДеГенерировать', button_color='#128700')]]
            #[sg.Button('Отмена', button_color='#613434'), sg.Push(), sg.Button('Путь сохранения'), sg.Push(), sg.Button('ДеГенерировать', button_color='#128700')]]

# Create the Window
window = sg.Window('ДеГенератор картинок', layout)
#with open('save_path.txt', 'r') as file:
#        path = file.read()

while True:
    event, values = window.read()
    if event == 'ДеГенерировать': 
        width = int(values[0])
        height = int(values[1])
        name = values[2]
        ext = values[3]
        create_rgb_image(width, height, name, ext)
        mb.showinfo(title="ДеГенератор", message=f'Файл {name}.{ext} с разрешением {height}x{width} сгенерирован и сохранен')

    elif event == 'Отмена' or event == sg.WIN_CLOSED:
        break

    else:
        mb.showerror(title='Пизда', message='Что то сломалось, я хз, не мои проблемы')

window.close()