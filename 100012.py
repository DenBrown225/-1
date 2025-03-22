import asyncio
from asyncio import WindowsSelectorEventLoopPolicy
import speech_recognition as sr
import os
import torch
import tkinter as tk
from tkinter import *
from tkinter import ttk
import threading
from g4f.client import Client
import json
import base64
import requests
import random
from PIL import Image
import customtkinter  # <- import the CustomTkinter module
import customtkinter as ctk

import time
import webbrowser

from gtts import gTTS

import random

import tkinter as tk
from tkinter import filedialog
import pygame
import wave
# Инициализация Pygame
pygame.mixer.init()
def say2():        
    sav1 = "12345.wav"
    device = torch.device('cpu')
    torch.set_num_threads(4)

# Задаем имя файла модели
    local_file = 'model.pt'

# Загружаем модель, если она еще не загружена
    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                        local_file)

# Загружаем модель TTS
    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

# Пользовательский ввод текста

    example_text = "Да сэр?"
    sample_rate = 24000
    speaker = 'eugene'

# Указываем имя файла для сохранения
         # Здесь задайте желаемое имя файла

# Генерируем аудио и сохраняем в WAV с указанным именем
    audio_path1 = model.save_wav(text=example_text,
                                speaker=speaker,
                                sample_rate=sample_rate,
                                audio_path=sav1
                                 ) 
    
    
                
threading.Thread(target=say2, daemon=True).start()

c = 0
def toggle_rectangle():
    global b
    global b1
    global moving_down
    global c
    global b2
    global b4
    c +=1
    
    if c % 2 != 0 :
        if c > 1:
            b4 = -5
            button54.place(x=a4, y=b4)
        else:
            b4 = 0
            button54.place(x=a4, y=b4)
        
        move_rectangle_down()
        
        
        
    else:# Двигаем прямоугольник вверх
        b4 = 150
        button54.place(x=a4, y=b4)
        move_rectangle_up() 
        
def move_rectangle_down():
    global button2
    global slider
    global button3
    global rectangle_y2
    global button2
    global slider
    global rectangle_y2
    global c5
    global b2
    global a2
    global rectangle_y3
    global b 
    global a
    global b1
    global a1
    global b2
    global a2
    global b3
    global a4
    global b4
    global button54
    button54.configure(state='disabled')
    global rectangle_y
    
    if rectangle_y < 0:
        b2 += 5
        b1 += 5
        b += 5
        b3 += 5
        # Проверка на достижение нижнего предела
        canvas.move(rectangle, 0, 5)
        slider.place(x=a, y=b)  # Двигаем слайдер вниз
        button2.place(x=a1, y=b1)
        button34.place(x=a3, y=b3)
        b4 += 5
        button54.place(x=a4, y=b4)
        canvas.move(rectangle2, 0, 5)
        canvas.move(rectangle3, 0, 5)
        # Двигаем прямоугольник вверх
        rectangle_y += 5
        rectangle_y2 += 5
        rectangle_y3 += 5
        # Двигаем прямоугольник вниз
        button3.place(x=a2, y=b2)
        
        # Запланировать следующий шаг анимации
        root.after(25, move_rectangle_down)  # Каждый 20 мс продолжаем движение
    else:
        moving_down = False  # После достижения нижнего предела переключаем направление
        b4 = 150
        button54.place(x=a4, y=b4)
        button54.configure(state='normal')

def move_rectangle_up():
    global button2
    global slider
    global button3
    global rectangle_y2
    global button2
    global slider
    global button3
    global rectangle_y2
    global c5
    global b2
    global a2
    global rectangle_y3
    global b 
    global a
    global b1
    global a1
    global b2
    global a2
    global b3
    global b4
    global a4
    global button54
    button54.configure(state='disabled')
    global rectangle_y
    
    if rectangle_y > -151:
        b2 -= 5
        b1 -= 5
        b -= 5
        b3 -= 5
        # Проверка на достижение верхнего предела
        canvas.move(rectangle, 0, -5)
        slider.place(x=a, y=b)  # Двигаем слайдер вниз
        button2.place(x=a1, y=b1)
        button34.place(x=a3, y=b3)
        canvas.move(rectangle2, 0, -5)
        canvas.move(rectangle3, 0, -5)
        button3.place(x=a2, y=b2)
        b4 -= 5
        button54.place(x=a4, y=b4)
        # Двигаем прямоугольник вверх
        rectangle_y -= 5
        rectangle_y2 -= 5
        rectangle_y3 -= 5
        
        # Запланировать следующий шаг анимации
        root.after(25, move_rectangle_up)  # Каждый 20 мс продолжаем движение
    else:
        moving_down = True  # После достижения верхнего предела переключаем направление
        b4 = -5
        button54.place(x=a4, y=b4)
        button54.configure(state='normal')
        

def sound():
    global c2
    global button2
    button_text = button2.cget("text")
    
    if button_text == "🔊" :
        button2.destroy()
        button2 = ctk.CTkButton(root, text="🔈", command=sound, width=26, height=25, fg_color="dark grey", hover_color="grey54")
        button2.place(x=325, y=101)
        slider.set(0)
        value2 = 0
        w(value2)
    if button_text == "🔈" :
        button2.destroy()
        button2 = ctk.CTkButton(root, text="🔊", command=sound, width=20, height=25, fg_color="dark grey", hover_color="grey54")
        button2.place(x=325, y=101)# После достижения нижнего предела переключаем направление
        slider.set(50)
        value2 = 50
        w(value2)
value2 = 0
pygame.mixer.music.set_volume(value2)
def w(value1):
    global button2
    global value2
    value2 = int(value1)
    value1 = value1 / 100
    pygame.mixer.music.set_volume(value1)
    if value2 > 0:
        button2.destroy()
        button2 = ctk.CTkButton(root, text="🔊", command=sound, width=20, height=25, fg_color="dark grey", hover_color="grey54")
        button2.place(x=325, y=101)
    else:
        button2.destroy()
        button2 = ctk.CTkButton(root, text="🔈", command=sound, width=26, height=25, fg_color="dark grey", hover_color="grey54")
        button2.place(x=325, y=101)
        
    print(value2)
def documentation():
    # URL для открытия
    url = "https://docs.google.com/presentation/d/17UeY4yW-GUTbcuSApVlCDRqIaByRzo4j/edit?usp=sharing&ouid=109776666387041742162&rtpof=true&sd=true"

# Открыть URL в новой вкладке
    webbrowser.open_new_tab(url)
    
# Создаем главное окно
# Устанавливаем политику для Windows
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

canvas1 = None

class Text2ImageAPI:
    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }
        
    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']
    
    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }
        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']
    
    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']
            attempts -= 1
            time.sleep(delay)



def gbt(text1):#Создаём функцию которая будет воспроизводить ответ с помощью библиотеки g4f.client 
    global jk
    
    jk = True
    label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 o \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 O \n",text_color="black")
    label2.place(x=605, y=200)
    client = Client()# Создаем экземпляр клиента для работы с библиотекой g4f
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text1 + ", ответь на русском языке"}],# Формируем сообщение от пользователя, добавляя '?' в конец текста для уточнения
    )
    label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 O \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 o \n",text_color="black")
    label2.place(x=605, y=200)
    
    
    text2 = response.choices[0].message.content # Возвращаем текст ответа, полученного от модели
      # Получаем ввод пользователя
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, text2)  # Вставляем пользовательский ввод
    text3 = text_widget.get("1.0", tk.END)  # Получаем весь текст из виджета
    jk = False
    if len(text3) > 3:  # Проверяем длину текста
                # Запускаем say в отдельном потоке
            root.after(100, lambda: threading.Thread(target=say, args=(True,text2, value2), daemon=True).start())
        
synonyms = [
    "сгенерировать",
    "нарисуй",
    "нарисовать"
    "картинку",
    "изображение",
    "картину",
    "Нарисуй",
    "Нарисовать"
    "Картинку",
    "Изображение",
    "Картину",
    "Сгенерировать картинку",
    "Сгенерируй картинку"
    ]    




def micro():# 
    global synonyms
    global audio_path1
    global a3
    global button34
    global b3
    try:
        if pygame.mixer.music.get_busy(): 
            pygame.mixer.music.stop()
        pygame.mixer.music.load("12345.wav")
        pygame.mixer.music.play()
        button34.destroy()
        button34 = ctk.CTkButton(root, text="▶", command=not_say, width=25, height=25, fg_color="dark grey", hover_color="grey54")
        button34.place(x=a3, y=b3)
        button34.configure(state='disabled')
    except Exception as e:
        pass
    # Создаем метку для отображения состояния работы помощника
    label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 o \n \n Анализ речи \n \n                 O \n \n Нейросеть \n \n                 o \n",text_color="black")
    label2.place(x=605, y=200)
    
    text4 = ""# Инициализируем переменную для хранения распознанного текста
    recognizer = sr.Recognizer()# Создаем экземпляр распознавателя речи
    try:
        with sr.Microphone() as source:# Используем микрофон в качестве источника звука
            print("Скажите что-нибудь:")
            audio_data = recognizer.listen(source)# Слушаем звук с микрофона
            text4 = recognizer.recognize_google(audio_data, language="ru-RU")# Распознаем речь с помощью Google Speech Recognition
            print("Вы сказали: " + text4)
    except sr.UnknownValueError:# Обработка ошибки, если не удалось распознать речь
        label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 O \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 o \n",text_color="black")
        label2.place(x=605, y=200)
        print("Извините, не могу распознать речь")
    except sr.RequestError as e:# Обработка ошибки запроса, если возникла проблема со связью с сервисом
        print("Ошибка при выполнении запроса к сервису Google Speech Recognition: {0}".format(e))
    except Exception as e: # Обработка любых других возможных ошибок
        print("Произошла ошибка: {0}".format(e))
    text_list = text4.split()
    
    a = False
    for i in range(len(synonyms)):
        if synonyms[i] in text_list:
            label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 o \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 O \n",text_color="black")
            label2.place(x=605, y=200)
            a = True
            gbt_thread = threading.Thread(target=picture, args=(text4,), daemon=True).start()
            
            return ""
            break
    if a == False:
        gbt2(text4)
        
        
       

def micro2():
    
    recognizer = sr.Recognizer()# Создаем экземпляр распознавателя речи
    try:
        with sr.Microphone() as source:# Используем микрофон в качестве источника звука
            print("Скажите Джарвис:")
            audio_data = recognizer.listen(source)# Слушаем звук с микрофона
            text5 = recognizer.recognize_google(audio_data, language="ru-RU")# Распознаем речь с помощью Google Speech Recognition
    except sr.UnknownValueError:# Обработка ошибки, если не удалось распознать речь
        text5 = " "
        print("Извините, не могу распознать речь")
    except sr.RequestError as e:# Обработка ошибки запроса, если возникла проблема со связью с сервисом
        print("Ошибка при выполнении запроса к сервису Google Speech Recognition: {0}".format(e))
    except Exception as e:# Обработка любых других возможных ошибок
        print("Произошла ошибка: {0}".format(e))
    return text5#Возвращаем распознанный текст

def jarvis():
    text9 = " "#Создаём пустую переменную для хранения текста
    while "Джарвис" not in text9 and "джар" not in text9:# Запускаем бесконечный цикл, пока не будет произнесено слово "Джарвис"
        text9 = micro2() # Вызываем функцию micro2(), которая распознает речь и возвращает текст
        print(text9)
    if "Джарвис" in text9 or "джар" in text9:
        text8 = micro()# Вызываем функцию micro(), чтобы продолжить выполнение действий ассистента
        return text8# Возвращаем результат, полученный из функции micro()

def gbt2(text6):
    gbt_thread = threading.Thread(target=gbt, args=(text6,), daemon=True).start()

def get_input_text():
    global synonyms
    
     #Объявляем переменную user_input как глобальную для использования в других частях программы
    text7 = entry.get()# Получаем текст, введенный пользователем, из переменной entry_var
    print(text7)
    text_widget.delete("1.0", tk.END)# Очищаем содержимое виджета Text
    text_list = text7.split()
    
    a = False
    for i in range(len(synonyms)):
        if synonyms[i] in text_list:
            a = True
            label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 o \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 O \n",text_color="black")
            label2.place(x=605, y=200)
            gbt_thread = threading.Thread(target=picture, args=(text7,), daemon=True).start()
            break

    if a == False:  # Если ни один из синонимов не найден
    # Запуск gbt() в отдельном потоке
        
          # Запускаем поток
        gbt2(text7)
        

        
    
def picture(text8):
    number = random.randint(1000, 99999)
    if __name__ == '__main__':
        api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '6E1F29727EE466DDD18BB8122CF04C53', 'E3B2F326F6B9FF7FCDC26B1150277CAF')
        model_id = api.get_model()
        uuid = api.generate(text8, model_id)
        images = api.check_generation(uuid)
    
        # Здесь image_base64 - это строка с данными изображения в формате base64
        image_base64 = images[0]  # Получаем первую картинку
        # Декодируем строку base64 в бинарные данные
        image_data = base64.b64decode(image_base64)
        string2 = ".jpg"
        number = str(number)
        combined_string = f"{number}{string2}"  # Убираем пробел для имени файла
        label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 O \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 o \n",text_color="black")
        label2.place(x=605, y=200)
    
    # Открываем файл для записи бинарных данных изображения
        with open(combined_string, "wb") as file:
            file.write(image_data)
    
    # Открываем и показываем сгенерированное изображение
        img = Image.open(combined_string)  # Используем PIL для открытия изображения
        img.show()  # Показываем изображение
    
    
    
def run_jarvis():
    while True:# Запускаем бесконечный цикл, чтобы программа продолжала работать
        global text8# Объявляем переменную text1 как глобальную для использования в других частях программы
        text8 = jarvis()# Вызываем функцию jarvis() и сохраняем полученный текст в text1
        
        # Вставляем полученный текст в конец виджета Text для отображения
        
        

q1 = True       
def say(flag, user_input, value3 ):
    global q1
    if flag == True :
        number1 = random.randint(1000, 99999)
        mp = ".wav"
        sav = f"{number1}{mp}"
        
        
# Синтез речи
        device = torch.device('cpu')
        torch.set_num_threads(4)

# Задаем имя файла модели
        local_file = 'model.pt'

# Загружаем модель, если она еще не загружена
        if not os.path.isfile(local_file):
            torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                             local_file)

# Загружаем модель TTS
        model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
        model.to(device)

# Пользовательский ввод текста

        example_text = user_input
        sample_rate = 24000
        speaker = 'eugene'

# Указываем имя файла для сохранения
         # Здесь задайте желаемое имя файла

# Генерируем аудио и сохраняем в WAV с указанным именем
        audio_path = model.save_wav(text=example_text,
                                     speaker=speaker,
                                     sample_rate=sample_rate,
                                     audio_path=sav
                                     ) 
        print(audio_path)
        
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        while True:
            if pygame.mixer.music.get_busy():  # Проверка, играет ли музыка
                print("Музыка играет...")
                button34.configure(state='normal')
            if q1 != False and not pygame.mixer.music.get_busy():
                print("Музыка не играет.")
                button34.configure(state='disabled')
                pygame.mixer.music.stop()
                break
            time.sleep(1)  # Пауза, чтобы не перегружать процессор

def not_say():
    global q1
    global button34
    if q1 == True:
        pygame.mixer.music.pause()
        q1 = False
        button34.destroy()
        button34 = ctk.CTkButton(root, text="∎", command=not_say, width=20, height=25, fg_color="dark grey", hover_color="grey54")
        button34.place(x=353, y=101)
    else:
        pygame.mixer.music.unpause()
        q1 = True
        button34.destroy()
        button34 = ctk.CTkButton(root, text="▶", command=not_say, width=25, height=25, fg_color="dark grey", hover_color="grey54")
        button34.place(x=353, y=101)

root = ctk.CTk()
root.title("Джарвис")  # устанавливаем заголовок окна
root.geometry("750x600")
customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("light")
a = 110
b = -45
# Создаем слайдер
a1 = 325
a2 = 714
b1 = -49
b2 = -137
#кнопка для изменения значения виджетов
a3 = 353
b3 = -49
a4 = 5
b4 = -5
canvas = tk.Canvas(root,bg="grey92", width=750, height=150, highlightthickness=0)
canvas.pack(anchor="n")

# Создаем прямоугольник на канвасе
slider = customtkinter.CTkSlider(master=root, from_=0, to=100, command=w)
slider.place(x=a, y=b)
slider.set(0)
button2 = ctk.CTkButton(root, text="🔈", command=sound, width=26, height=25, fg_color="dark grey", hover_color="grey")
button2.place(x=a1, y=b1)# После достижения нижнего предела переключаем направление
button34 = ctk.CTkButton(root, text="▶", command=not_say, width=25, height=25, fg_color="dark grey", hover_color="grey")
button34.place(x=a3, y=b3)
# Создаем прямоугольник на канвасе
# После достижения нижнего предела переключаем направление
button3 = ctk.CTkButton(root, text="?", command=documentation, width=25, height=25, fg_color="dark grey", hover_color="grey")
button3.place(x=a2, y=b2)
rectangle_y = -150  # Начальная позиция Y
rectangle = canvas.create_rectangle(750, rectangle_y, 0, rectangle_y + 149, fill="light grey")

rectangle_y2 = -51  # Начальная позиция Y
rectangle2 = canvas.create_rectangle(390, rectangle_y2, 100, rectangle_y2 + 28, fill="grey93")
rectangle_y3 = -141  # Начальная позиция Y
rectangle3 = canvas.create_rectangle(740, rectangle_y3, 710, rectangle_y3 + 30, fill="grey93")
moving_down = True  # Изначально прямоугольник будет двигаться вниз

custom_font = ("Helvetica", 16)
button54 = ctk.CTkButton(root, text="★", command=toggle_rectangle, width=30, height=30, fg_color="grey96", hover_color="grey100", text_color="red",text_color_disabled="red", font=custom_font)
button54.place(x=a4, y=b4)# После достижения нижнего предела переключаем направление
#текстовый виджет для вывода ответа функции - gbt()
text_widget = ctk.CTkTextbox(root, width=505, height=300)

text_widget.place(x=65, y=250)

#label для помощи в интерфейсе
label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 O \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 o \n",text_color="black")
label2.place(x=605, y=200)

#поле для ввода вопросов
entry = ctk.CTkEntry(root, placeholder_text="Задайте вопрос", width=479, height=25)
entry.place(x=65, y=184)

#кнопка для отправки запросов
button = ctk.CTkButton(root, text="🔍", command=get_input_text, width=25, height=25, fg_color="dark grey", hover_color="grey")
button.place(x=544, y=184)

# Создаем кнопку
button34.configure(state='disabled')

# Запускаем выполнения функций в отдельных потоках
threading.Thread(target=run_jarvis, daemon=True).start()

# Запуск главного цикла приложения
root.mainloop()



