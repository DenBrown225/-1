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
import customtkinter  # Импортируем модуль CustomTkinter для создания пользовательского интерфейса
import customtkinter as ctk
import time
import webbrowser
from gtts import gTTS  # Импортируем библиотеку для текстового синтеза речи (TTS)
import random
import tkinter as tk
from tkinter import filedialog  # Импортируем для работы с диалогами выбора файлов
import pygame  # Импортируем Pygame для работы с аудио и мультимедиа
import wave

# Инициализация Pygame для работы с аудио
pygame.mixer.init()

def say2():        
    sav1 = "12345.wav"  # Имя файла, в который будет сохранено аудио
    device = torch.device('cpu')  # Устанавливаем устройство (CPU)
    torch.set_num_threads(4)  # Устанавливаем количество потоков

    # Задаем имя файла модели TTS (Text-to-Speech)
    local_file = 'model.pt'

    # Загружаем модель, если она еще не загружена
    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                        local_file)

    # Загружаем модель TTS из локального файла
    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)  # Переносим модель на заданное устройство

    # Текст, который будет озвучен пользователем (можно заменить на ввод пользователя)
    example_text = "Да сэр?"
    sample_rate = 24000  # Частота дискретизации аудио
    speaker = 'eugene'  # Выбор голосового синтезатора

    # Генерируем аудио и сохраняем в WAV файл с указанным именем
    audio_path1 = model.save_wav(text=example_text,
                                  speaker=speaker,
                                  sample_rate=sample_rate,
                                  audio_path=sav1)

# Запускаем функцию say2 в отдельном потоке, чтобы не блокировать основной поток программы 
threading.Thread(target=say2, daemon=True).start()

c = 0  # Счетчик для отслеживания состояния кнопки

def toggle_rectangle():
    global b, b1, moving_down, c, b2, b4  # Объявляем глобальные переменные
    
    c += 1  # Увеличиваем счетчик при каждом вызове функции
    
    if c % 2 != 0:  # Если счетчик нечетный, двигаем прямоугольник вниз 
        if c > 1:
            b4 = -5  # Устанавливаем начальную позицию кнопки вниз 
            button54.place(x=a4, y=b4)  
        else:
            b4 = 0  
            button54.place(x=a4, y=b4)
        
        move_rectangle_down()  # Запускаем движение прямоугольника вниз
        
    else:  # Если счетчик четный, двигаем прямоугольник вверх 
        b4 = 150  
        button54.place(x=a4, y=b4)  
        move_rectangle_up() 

def move_rectangle_down():
    global button2, slider, button3, rectangle_y2, b2, a2, rectangle_y3  
    global b, a1, b1, a3, b3, a4, b4  
    global button54
    
    button54.configure(state='disabled')  # Отключаем кнопку во время движения
    
    global rectangle_y
    
    if rectangle_y < 0:  # Проверяем достиг ли прямоугольник нижнего предела 
        b2 += 5  
        b1 += 5  
        b += 5  
        b3 += 5  

        canvas.move(rectangle, 0, 5)   # Двигаем основной прямоугольник вниз 
        slider.place(x=a, y=b)          # Двигаем слайдер вниз 
        button2.place(x=a1, y=b1)       # Двигаем кнопку вниз 
        button34.place(x=a3, y=b3)      # Двигаем другую кнопку вниз 
        b4 += 5  
        button54.place(x=a4, y=b4)      # Двигаем кнопку вниз 
        
        canvas.move(rectangle2, 0, 5)   # Двигаем второй прямоугольник вниз 
        canvas.move(rectangle3, 0, 5)   # Двигаем третий прямоугольник вниз 
        
        rectangle_y += 5                 # Обновляем координаты прямоугольников 
        rectangle_y2 += 5  
        rectangle_y3 += 5  

        button3.place(x=a2, y=b2)       # Двигаем третью кнопку 

        root.after(25, move_rectangle_down)   # Запланировать следующий шаг анимации через каждые 25 мс 
    else:
        moving_down = False   # После достижения нижнего предела переключаем направление движения 
        b4 = 150  
        button54.place(x=a4, y=b4)  
        button54.configure(state='normal')   # Включаем кнопку обратно после завершения движения
def move_rectangle_up():
    # Объявляем глобальные переменные, которые будут использоваться в функции
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
    
    # Отключаем кнопку во время движения прямоугольника вверх
    button54.configure(state='disabled')
    
    # Проверяем, не достиг ли прямоугольник верхнего предела (в данном случае -151)
    if rectangle_y > -151:
        # Уменьшаем координаты кнопок и слайдера для движения вверх
        b2 -= 5  
        b1 -= 5  
        b -= 5  
        b3 -= 5  

        # Двигаем основной прямоугольник вверх на 5 пикселей 
        canvas.move(rectangle, 0, -5)  
        
        # Обновляем положение слайдера и кнопок на экране 
        slider.place(x=a, y=b)  
        button2.place(x=a1, y=b1)  
        button34.place(x=a3, y=b3)  
        
        # Двигаем второй и третий прямоугольники вверх 
        canvas.move(rectangle2, 0, -5)  
        canvas.move(rectangle3, 0, -5)  
        
        # Обновляем положение третьей кнопки 
        button3.place(x=a2, y=b2)  
        
        # Уменьшаем координаты кнопки для ее движения вверх 
        b4 -= 5  
        button54.place(x=a4, y=b4)  

        # Обновляем координаты прямоугольников 
        rectangle_y -= 5  
        rectangle_y2 -= 5  
        rectangle_y3 -= 5  

        # Запланировать следующий шаг анимации через каждые 25 мс 
        root.after(25, move_rectangle_up)  
        
    else:
        moving_down = True  # После достижения верхнего предела переключаем направление движения вниз 
        b4 = -5  # Устанавливаем начальную позицию кнопки вниз 
        button54.place(x=a4, y=b4)  
        
        # Включаем кнопку обратно после завершения движения 
        button54.configure(state='normal')

def sound():
    # Объявляем глобальные переменные для управления звуком и кнопками
    global c2
    global button2
    
    # Получаем текст текущей кнопки (🔊 или 🔈)
    button_text = button2.cget("text")
    
    if button_text == "🔊":  # Если текущая кнопка "включить звук"
        button2.destroy()  # Удаляем текущую кнопку
        
        # Создаем новую кнопку "выключить звук" и размещаем ее на экране
        button2 = ctk.CTkButton(root, text="🔈", command=sound, width=26, height=25,
                                 fg_color="dark grey", hover_color="grey54")
                                 
        button2.place(x=325, y=101)  # Размещаем кнопку на экране
        
        slider.set(0)  # Устанавливаем значение слайдера на 0 (выключен звук)
        
        value2 = 0   # Устанавливаем значение громкости в 0 (выключен звук)
        
        w(value2)   # Вызываем функцию w() для применения громкости

    if button_text == "🔈":  # Если текущая кнопка "выключить звук"
        button2.destroy()  # Удаляем текущую кнопку
        
         # Создаем новую кнопку "включить звук" и размещаем ее на экране
         button2 = ctk.CTkButton(root, text="🔊", command=sound, width=20,
                                  height=25, fg_color="dark grey", hover_color="grey54")
                                  
         button2.place(x=325, y=101)   # Размещаем кнопку на экране
        
         slider.set(50)   # Устанавливаем значение слайдера на 50 (включен звук)
         
         value2 = 50   # Устанавливаем значение громкости в 50 (умеренный уровень звука)
         
         w(value2)   # Вызываем функцию w() для применения громкости

# Инициализация значения громкости по умолчанию в Pygame (0 - выключен звук)
value2 = 0   
pygame.mixer.music.set_volume(value2)   # Устанавливаем громкость музыки в Pygame
def w(value1):
    # Объявляем глобальные переменные для управления кнопкой и значением громкости
    global button2
    global value2
    
    # Преобразуем значение громкости в целое число и сохраняем его
    value2 = int(value1)
    
    # Преобразуем значение громкости в диапазон от 0 до 1 для Pygame
    value1 = value1 / 100
    
    # Устанавливаем громкость музыки в Pygame
    pygame.mixer.music.set_volume(value1)
    
    # Если значение громкости больше 0, создаем кнопку "включить звук"
    if value2 > 0:
        button2.destroy()  # Удаляем текущую кнопку
        
        # Создаем новую кнопку "включить звук" и размещаем ее на экране
        button2 = ctk.CTkButton(root, text="🔊", command=sound, width=20, height=25,
                                 fg_color="dark grey", hover_color="grey54")
        button2.place(x=325, y=101)  # Размещаем кнопку на экране
        
    else:  # Если значение громкости равно 0, создаем кнопку "выключить звук"
        button2.destroy()  # Удаляем текущую кнопку
        
        # Создаем новую кнопку "выключить звук" и размещаем ее на экране
        button2 = ctk.CTkButton(root, text="🔈", command=sound, width=26, height=25,
                                 fg_color="dark grey", hover_color="grey54")
        button2.place(x=325, y=101)  # Размещаем кнопку на экране
        
    print(value2)  # Выводим текущее значение громкости в консоль

def documentation():
    # URL для открытия документации
    url = "https://docs.google.com/presentation/d/17UeY4yW-GUTbcuSApVlCDRqIaByRzo4j/edit?usp=sharing&ouid=109776666387041742162&rtpof=true&sd=true"

    # Открыть URL в новой вкладке браузера
    webbrowser.open_new_tab(url)

# Создаем главное окно приложения (предполагается, что это происходит где-то выше в коде)
# Устанавливаем политику для Windows для работы с асинхронным циклом событий
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

canvas1 = None  # Инициализируем переменную canvas1 как None (предполагается, что она будет использоваться позже)

class Text2ImageAPI:
    def __init__(self, url, api_key, secret_key):
        # Инициализация объекта API с URL и ключами аутентификации
        self.URL = url  # Сохраняем базовый URL API
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',  # Заголовок с API ключом
            'X-Secret': f'Secret {secret_key}',  # Заголовок с секретным ключом
        }
        
    def get_model(self):
        # Получение списка доступных моделей из API
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()  # Преобразуем ответ в JSON формат
        return data[0]['id']  # Возвращаем ID первой модели в списке
    
    def generate(self, prompt, model, images=1, width=1024, height=1024):
        # Генерация изображения на основе текстового запроса (prompt)
        
        # Параметры для генерации изображения
        params = {
            "type": "GENERATE",  # Тип операции
            "numImages": images,  # Количество изображений для генерации
            "width": width,  # Ширина изображения
            "height": height,  # Высота изображения
            "generateParams": {
                "query": f"{prompt}"  # Текстовый запрос для генерации изображения
            }
        }
        
        # Формируем данные для POST-запроса
        data = {
            'model_id': (None, model),  # ID модели для генерации
            'params': (None, json.dumps(params), 'application/json')  # Параметры в формате JSON
        }
        
        # Отправляем POST-запрос на генерацию изображения
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        
        data = response.json()  # Преобразуем ответ в JSON формат
        return data['uuid']  # Возвращаем уникальный идентификатор запроса на генерацию
    
    def check_generation(self, request_id, attempts=10, delay=10):
        # Проверка статуса генерации изображения по уникальному идентификатору запроса
        
        while attempts > 0:  # Пока есть попытки проверки статуса
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()  # Преобразуем ответ в JSON формат
            
            if data['status'] == 'DONE':  # Если статус завершен
                return data['images']  # Возвращаем сгенерированные изображения
            
            attempts -= 1  # Уменьшаем количество оставшихся попыток
            time.sleep(delay)  # Ждем перед следующей проверкой статуса



def gbt(text1):
    # Создаем функцию, которая будет воспроизводить ответ с помощью библиотеки g4f.client
    global jk  # Объявляем переменную jk как глобальную

    jk = True  # Устанавливаем флаг, указывающий на то, что процесс активен
    # Создаем метку для отображения статуса вызова помощника
    label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 o \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 O \n", text_color="black")
    label2.place(x=605, y=200)  # Размещаем метку на экране

    client = Client()  # Создаем экземпляр клиента для работы с библиотекой g4f
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Указываем модель для генерации ответа
        messages=[{"role": "user", "content": text1 + ", ответь на русском языке"}],  # Формируем сообщение от пользователя, добавляя указание отвечать на русском языке
    )

    # Обновляем метку статуса после получения ответа
    label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 O \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 o \n", text_color="black")
    label2.place(x=605, y=200)

    text2 = response.choices[0].message.content  # Получаем текст ответа от модели

    # Получаем ввод пользователя из текстового виджета
    text_widget.delete("1.0", tk.END)  # Очищаем текстовый виджет
    text_widget.insert(tk.END, text2)  # Вставляем ответ от модели в текстовый виджет

    text3 = text_widget.get("1.0", tk.END)  # Получаем весь текст из виджета
    jk = False  # Сбрасываем флаг активности

    if len(text3) > 3:  # Проверяем длину текста (должна быть больше 3 символов)
        # Запускаем функцию say в отдельном потоке для воспроизведения текста
        root.after(100, lambda: threading.Thread(target=say, args=(True, text2, value2), daemon=True).start())

# Список синонимов для команды генерации изображений
synonyms = [
    "сгенерировать",
    "нарисуй",
    "нарисовать",
    "картинку",
    "изображение",
    "картину",
    "Нарисуй",
    "Нарисовать",
    "Картинку",
    "Изображение",
    "Картину",
    "Сгенерировать картинку",
    "Сгенерируй картинку"
]


def micro():
    # Объявляем глобальные переменные, которые будут использоваться в функции
    global synonyms
    global audio_path1
    global a3
    global button34
    global b3

    try:
        # Если музыка уже играет, останавливаем её
        if pygame.mixer.music.get_busy(): 
            pygame.mixer.music.stop()
        
        # Загружаем и воспроизводим аудиофайл
        pygame.mixer.music.load("12345.wav")
        pygame.mixer.music.play()

        # Удаляем старую кнопку и создаем новую для воспроизведения аудио
        button34.destroy()
        button34 = ctk.CTkButton(root, text="▶", command=not_say, width=25, height=25, fg_color="dark grey", hover_color="grey54")
        button34.place(x=a3, y=b3)
        button34.configure(state='disabled')  # Делаем кнопку неактивной

    except Exception as e:
        pass  # Игнорируем любые ошибки при воспроизведении аудио

    # Создаем метку для отображения состояния работы помощника
    label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 o \n \n Анализ речи \n \n                 O \n \n Нейросеть \n \n                 o \n", text_color="black")
    label2.place(x=605, y=200)

    text4 = ""  # Инициализируем переменную для хранения распознанного текста
    recognizer = sr.Recognizer()  # Создаем экземпляр распознавателя речи

    try:
        with sr.Microphone() as source:  # Используем микрофон в качестве источника звука
            print("Скажите что-нибудь:")
            audio_data = recognizer.listen(source)  # Слушаем звук с микрофона
            
            # Распознаем речь с помощью Google Speech Recognition
            text4 = recognizer.recognize_google(audio_data, language="ru-RU")  
            print("Вы сказали: " + text4)

    except sr.UnknownValueError:  # Обработка ошибки, если не удалось распознать речь
        label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 O \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 o \n", text_color="black")
        label2.place(x=605, y=200)
        print("Извините, не могу распознать речь")

    except sr.RequestError as e:  # Обработка ошибки запроса к сервису распознавания речи
        print("Ошибка при выполнении запроса к сервису Google Speech Recognition: {0}".format(e))

    except Exception as e:  # Обработка любых других возможных ошибок
        print("Произошла ошибка: {0}".format(e))

    text_list = text4.split()  # Разбиваем распознанный текст на слова

    a = False  # Флаг для проверки наличия синонимов в распознанном тексте

    for i in range(len(synonyms)):
        if synonyms[i] in text_list:  # Проверяем наличие синонимов в списке слов
            label2 = ctk.CTkLabel(root, text="Вызов помошника \n \n                 o \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 O \n", text_color="black")
            label2.place(x=605, y=200)
            a = True  # Устанавливаем флаг в True, если найден синоним
            
            # Запускаем функцию picture в отдельном потоке с распознанным текстом
            gbt_thread = threading.Thread(target=picture, args=(text4,), daemon=True).start()
            
            return ""  # Завершаем выполнение функции после нахождения синонима

    if a == False:
        gbt2(text4)  # Если синонимы не найдены, вызываем функцию gbt2 с распознанным текстом
        
       

def micro2():
    # Создаем экземпляр распознавателя речи
    recognizer = sr.Recognizer()  
    
    try:
        # Используем микрофон в качестве источника звука
        with sr.Microphone() as source:  
            print("Скажите Джарвис:")  # Подсказка для пользователя
            
            # Слушаем звук с микрофона и сохраняем его в audio_data
            audio_data = recognizer.listen(source)  
            
            # Распознаем речь с помощью Google Speech Recognition
            text5 = recognizer.recognize_google(audio_data, language="ru-RU")  
            
    except sr.UnknownValueError:  # Обработка ошибки, если не удалось распознать речь
        text5 = " "  # Устанавливаем текст в пустую строку, если распознавание не удалось
        print("Извините, не могу распознать речь")  # Сообщаем об ошибке пользователю

    except sr.RequestError as e:  # Обработка ошибки запроса к сервису распознавания речи
        print("Ошибка при выполнении запроса к сервису Google Speech Recognition: {0}".format(e))

    except Exception as e:  # Обработка любых других возможных ошибок
        print("Произошла ошибка: {0}".format(e))

    return text5  # Возвращаем распознанный текст (или пустую строку в случае ошибки)

def jarvis():
    text9 = " "  # Создаем пустую переменную для хранения текста
    
    # Запускаем бесконечный цикл, пока не будет произнесено слово "Джарвис"
    while "Джарвис" not in text9 and "джар" not in text9:  
        text9 = micro2()  # Вызываем функцию micro2(), которая распознает речь и возвращает текст
        print(text9)  # Выводим распознанный текст в консоль

    # Если в распознанном тексте содержится "Джарвис" или "джар"
    if "Джарвис" in text9 or "джар" in text9:
        text8 = micro()  # Вызываем функцию micro(), чтобы продолжить выполнение действий ассистента
        return text8  # Возвращаем результат, полученный из функции micro()

def gbt2(text6):
    # Запускаем функцию gbt в отдельном потоке с переданным текстом
    gbt_thread = threading.Thread(target=gbt, args=(text6,), daemon=True).start()
def get_input_text():
    global synonyms  # Объявляем переменную synonyms как глобальную для использования в других частях программы
    
    # Получаем текст, введенный пользователем, из виджета entry
    text7 = entry.get()  
    print(text7)  # Выводим введенный текст в консоль
    
    text_widget.delete("1.0", tk.END)  # Очищаем содержимое виджета Text
    
    # Разбиваем введенный текст на слова и сохраняем в список
    text_list = text7.split()  
    
    a = False  # Флаг для отслеживания наличия синонимов в тексте
    
    # Проверяем наличие синонимов в введенном тексте
    for i in range(len(synonyms)):
        if synonyms[i] in text_list:  # Если найден синоним
            a = True  # Устанавливаем флаг в True
            
            # Создаем и размещаем метку с информацией о вызове помощника
            label2 = ctk.CTkLabel(root, text="Вызов помощника \n \n                 o \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 O \n", text_color="black")
            label2.place(x=605, y=200)  # Размещаем метку на экране
            
            # Запускаем функцию picture в отдельном потоке с переданным текстом
            gbt_thread = threading.Thread(target=picture, args=(text7,), daemon=True).start()
            break  # Выходим из цикла, если найден хотя бы один синоним

    if not a:  # Если ни один из синонимов не найден
        # Запускаем gbt() в отдельном потоке с переданным текстом
        gbt2(text7)  # Запускаем поток для обработки текста без синонимов
        

        
    
def picture(text8):
    # Генерируем случайное число для создания уникального имени файла
    number = random.randint(1000, 99999)  
    
    if __name__ == '__main__':  # Проверяем, что код выполняется как основная программа
        # Инициализируем API для генерации изображений
        api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '6E1F29727EE466DDD18BB8122CF04C53', 'E3B2F326F6B9FF7FCDC26B1150277CAF')
        
        # Получаем идентификатор модели для генерации изображений
        model_id = api.get_model()  
        
        # Генерируем изображение на основе текста
        uuid = api.generate(text8, model_id)  
        
        # Проверяем статус генерации изображения
        images = api.check_generation(uuid)  
    
        # Здесь image_base64 - это строка с данными изображения в формате base64
        image_base64 = images[0]  # Получаем первую картинку из списка
        
        # Декодируем строку base64 в бинарные данные
        image_data = base64.b64decode(image_base64)  
        
        string2 = ".jpg"  # Определяем расширение файла
        number = str(number)  # Преобразуем число в строку
        
        # Формируем уникальное имя файла для сохранения изображения
        combined_string = f"{number}{string2}"  
        
        # Создаем и размещаем метку с информацией о вызове помощника
        label2 = ctk.CTkLabel(root, text="Вызов помощника \n \n                 O \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 o \n", text_color="black")
        label2.place(x=605, y=200)  
    
        # Открываем файл для записи бинарных данных изображения
        with open(combined_string, "wb") as file:
            file.write(image_data)  # Записываем данные изображения в файл
    
        # Открываем и показываем сгенерированное изображение с помощью PIL
        img = Image.open(combined_string)  # Используем PIL для открытия изображения
        img.show()  # Показываем изображение на экране
    
    
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



