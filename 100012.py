#Устанавливаем все нужные библиотеки
import asyncio
from asyncio import WindowsSelectorEventLoopPolicy
import speech_recognition as sr
import pyaudio
import tkinter as tk
from tkinter import *
from tkinter import ttk
import threading
from g4f.client import Client
import json
import time
import base64
import requests
import random
from PIL import Image
import setuptools
# Устанавливаем политику для Windows
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
def motion(angle):
    start_angle = angle % 360
    canvas.itemconfig(ball, start=start_angle, extent=120)
    angle += 1
    root.after(30, motion, angle)

def motion1(angle1):
    start_angle1 = angle1 % 360
    canvas.itemconfig(ball1, start=start_angle1, extent=90)
    angle1 += 1
    root.after(10, motion1, angle1)

def motion2(angle2, index):
    start_angle2 = angle2 + (index * 60) % 360  # Spread out the arcs evenly
    canvas.itemconfig(ball2[index], start=start_angle2, extent=20)
    angle2 += 1
    root.after(15, lambda: motion2(angle2, index))  # Continue animating each arc


# Глобальная переменная для холста
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


def gbt(text):#Создаём функцию которая будет воспроизводить ответ с помощью библиотеки g4f.client 
    client = Client()# Создаем экземпляр клиента для работы с библиотекой g4f
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text + "?"}],# Формируем сообщение от пользователя, добавляя '?' в конец текста для уточнения
    )
    return response.choices[0].message.content # Возвращаем текст ответа, полученного от модели
    
# Флаг для звука
sou = True


def micro():# 
    # Создаем метку для отображения состояния работы помощника
    label2 = ttk.Label(tab1, text="Вызов помошника \n \n                 o \n \n Анализ речи \n \n                 O \n \n Нейросеть \n \n                 o \n")
    label2.place(x=605, y=200)
    
    text = ""# Инициализируем переменную для хранения распознанного текста
    recognizer = sr.Recognizer()# Создаем экземпляр распознавателя речи
    try:
        with sr.Microphone() as source:# Используем микрофон в качестве источника звука
            print("Скажите что-нибудь:")
            audio_data = recognizer.listen(source)# Слушаем звук с микрофона
            text = recognizer.recognize_google(audio_data, language="ru-RU")# Распознаем речь с помощью Google Speech Recognition
            print("Вы сказали: " + text)
    except sr.UnknownValueError:# Обработка ошибки, если не удалось распознать речь
        label2 = ttk.Label(tab1, text="Вызов помошника \n \n                 O \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 o \n")
        label2.place(x=605, y=200)
        print("Извините, не могу распознать речь")
    except sr.RequestError as e:# Обработка ошибки запроса, если возникла проблема со связью с сервисом
        print("Ошибка при выполнении запроса к сервису Google Speech Recognition: {0}".format(e))
    except Exception as e: # Обработка любых других возможных ошибок
        print("Произошла ошибка: {0}".format(e))

    
    if text:# Если текст успешно распознан
        # Обновляем метку для отображения статуса
        label2 = ttk.Label(tab1, text="Вызов помошника \n \n                 o \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 O \n")
        label2.place(x=605, y=200)
        
        global text1# Объявляем переменную text1 как глобальную для использования вне функции
        text1 = gbt(text)# Вызываем функцию gbt() для обработки распознанного текста
        
        text_widget.delete("1.0", tk.END)#Удаляем текст из виджета
        #Возвращаем метку на исходное состояние
        label2 = ttk.Label(tab1, text="Вызов помошника \n \n                 O \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 o \n")
        label2.place(x=605, y=200)
        
        return text1# Возвращаем текст, полученный от функции gbt()
    else:
        return ""# Если текст не распознан, возвращаем пустую строку

def micro2():
    recognizer = sr.Recognizer()# Создаем экземпляр распознавателя речи
    try:
        with sr.Microphone() as source:# Используем микрофон в качестве источника звука
            print("Скажите Джарвис:")
            audio_data = recognizer.listen(source)# Слушаем звук с микрофона
            text2 = recognizer.recognize_google(audio_data, language="ru-RU")# Распознаем речь с помощью Google Speech Recognition
    except sr.UnknownValueError:# Обработка ошибки, если не удалось распознать речь
        text2 = " "
        print("Извините, не могу распознать речь")
    except sr.RequestError as e:# Обработка ошибки запроса, если возникла проблема со связью с сервисом
        print("Ошибка при выполнении запроса к сервису Google Speech Recognition: {0}".format(e))
    except Exception as e:# Обработка любых других возможных ошибок
        print("Произошла ошибка: {0}".format(e))
    return text2#Возвращаем распознанный текст

def jarvis():
    text2 = " "#Создаём пустую переменную для хранения текста
    while "Джарвис" not in text2:# Запускаем бесконечный цикл, пока не будет произнесено слово "Джарвис"
        text2 = micro2() # Вызываем функцию micro2(), которая распознает речь и возвращает текст
        print(text2)
    if "Джарвис" in text2:
        text1 = micro()# Вызываем функцию micro(), чтобы продолжить выполнение действий ассистента
        return text1# Возвращаем результат, полученный из функции micro()


def get_input_text():
    global user_input #Объявляем переменную user_input как глобальную для использования в других частях программы
    text3 = entry_var.get()# Получаем текст, введенный пользователем, из переменной entry_var
    text_widget.delete("1.0", tk.END)# Очищаем содержимое виджета Text
    user_input = gbt(text3)# Вызываем функцию gbt() с введенным текстом и сохраняем результат в user_input
    text_widget.insert(tk.END, user_input)# Вставляем ответ (user_input) в конец виджета Text для отображения
def picture(text):
    number = random.randint(1000, 99999)
    if __name__ == '__main__':
        api = Text2ImageAPI('https://api-key.fusionbrain.ai/', 'api_key', 'secret_key')
        model_id = api.get_model()
        uuid = api.generate(text, model_id)
        images = api.check_generation(uuid)
    
        # Здесь image_base64 - это строка с данными изображения в формате base64
        image_base64 = images[0]  # Получаем первую картинку
        # Декодируем строку base64 в бинарные данные
        image_data = base64.b64decode(image_base64)
        string2 = ".jpg"
        number = str(number)
        combined_string = f"{number}{string2}"  # Убираем пробел для имени файла
    
    # Открываем файл для записи бинарных данных изображения
        with open(combined_string, "wb") as file:
            file.write(image_data)
    
    # Открываем и показываем сгенерированное изображение
        img = Image.open(combined_string)  # Используем PIL для открытия изображения
        img.show()  # Показываем изображение
    
def get_input_text2():
    
    text = entry_var2.get()# Получаем текст, введенный пользователем, из переменной entry_var
    
    picture(text)
    
    
def run_jarvis():
    while True:# Запускаем бесконечный цикл, чтобы программа продолжала работать
        global text1# Объявляем переменную text1 как глобальную для использования в других частях программы
        text1 = jarvis()# Вызываем функцию jarvis() и сохраняем полученный текст в text1
        text_widget.delete("1.0", tk.END)  # очищаем содержимое виджета Text
        text_widget.insert(tk.END, text1)# Вставляем полученный текст в конец виджета Text для отображения
        text1 = ""# Сбрасываем значение text1 для следующего цикла, чтобы избежать конфликтов с предыдущими данными
        user_input = ""# Сбрасываем значение user_input для следующего цикла (если это необходимо)


def songs():
    count = 0#Создаём count для того чтобы переменная "t"спользовалась 1 раз
    if count == 0:
        ts = ""
    a = [""]# Инициализируем список "a" с пустой строкой. Он будет использоваться для хранения данных.
    # Определяем текст запроса для функции gbt
    text = "топ 6 песни для днд с сылками отвечай без лишних слов опираясь на такой ответ 1. название песни  by  исполнитель ссылка на ютуб 2. название песни  by  исполнитель ссылка на ютуб 3. название песни  by  исполнитель ссылка на песню"
    while len(a) != 6 :# Запускаем цикл до тех пор, пока список "a" не будет содержать 3 элемента
        ts1 = ts#Прошлый ответ сохраняем в переменную "ts1"
        ts = gbt(text)# Вызываем функцию gbt(text) для получения списка песен и сохраняем результат в "ts"
        if ts1 != ts:#Сравнимаем что-бы ответ не повторялся
            a = ts.split("\n")# Разбиваем результат на строки, чтобы получить отдельные песни
        else:# В отрицательном случае повторяем цикл
            continue
    
    text_widget1.delete("1.0", tk.END)
        
    text_widget1.insert(tk.END, a[0])
    text_widget2.delete("1.0", tk.END)
        
    text_widget2.insert(tk.END, a[1])
    text_widget3.delete("1.0", tk.END)
        
    text_widget3.insert(tk.END, a[2])

    text_widget4.delete("1.0", tk.END)
        
    text_widget4.insert(tk.END, a[3])
    text_widget5.delete("1.0", tk.END)
        
    text_widget5.insert(tk.END, a[4])
    text_widget6.delete("1.0", tk.END)
        
    text_widget6.insert(tk.END, a[5])
    count += 1
def vidio():
    count = 0#Создаём count для того чтобы переменная "tv"спользовалась 1 раз
    if count == 0:
        tv = ""
    a = [""]# Инициализируем список "a" с пустой строкой. Он будет использоваться для хранения данных.
    text = "топ 6 фоновых видио для днд с сылками отвечай без лишних слов опираясь на такой ответ 1. название видио ссылка на ютуб 2. название видио ссылка на ютуб 3. название видио ссылка на видио "
    # Определяем текст запроса для функции gbt
    while len(a) != 6 :# Запускаем цикл до тех пор, пока список "a" не будет содержать 3 элемента
        tv1 = tv#Прошлый ответ сохраняем в переменную "tv1"
        tv = gbt(text)# Вызываем функцию gbt(text) для получения списка видио и сохраняем результат в "tv"
        if tv1 != tv:#Сравнимаем что-бы ответ не повторялся
            a = tv.split("\n")# Разбиваем результат на строки, чтобы получить отдельные видио
        else:# В отрицательном случае повторяем цикл
            continue
    text_widget7.delete("1.0", tk.END)
        
    text_widget7.insert(tk.END, a[0])
    text_widget8.delete("1.0", tk.END)
        
    text_widget8.insert(tk.END, a[1])
    text_widget9.delete("1.0", tk.END)
        
    text_widget9.insert(tk.END, a[2])

    text_widget10.delete("1.0", tk.END)
        
    text_widget10.insert(tk.END, a[3])
    text_widget11.delete("1.0", tk.END)
        
    text_widget11.insert(tk.END, a[4])
    text_widget12.delete("1.0", tk.END)
        
    text_widget12.insert(tk.END, a[5])
    count += 1        
def kvest():
    count = 0#Создаём count для того чтобы переменная "tk"спользовалась 1 раз
    if count == 0:
        th = " "
    a = [""]#Инициализируем список "a" с пустой строкой. Он будет использоваться для хранения данных.
    # Определяем текст запроса для функции gbt
    text = "топ 3 сюжета из днд историй с кратким содержанием отвечай без лишних слов опираясь на такой ответ 1. название сюжета на английском  краткое содержание  2. название сюжета на английском  краткое содержание  3.название сюжета на английском  краткое содержание  "
    while len(a) != 3 :# Запускаем цикл до тех пор, пока список "a" не будет содержать 3 элемента
        th1 = th#Прошлый ответ сохраняем в переменную "th1"
        th = gbt(text)# Вызываем функцию gbt(text) для получения списка историй и сохраняем результат в "th"
        if th1 != th:#Сравнимаем что-бы ответ не повторялся
            a = th.split("\n")# Разбиваем результат на строки, чтобы получить отдельные истории
        else:# В отрицательном случае повторяем цикл
            continue
    text_widget13.delete("1.0", tk.END)
        
    text_widget13.insert(tk.END, a[0])
    text_widget14.delete("1.0", tk.END)
        
    text_widget14.insert(tk.END, a[1])
    text_widget15.delete("1.0", tk.END)
        
    text_widget15.insert(tk.END, a[2])

    
    count += 1        
def round1():#Функция которая запускает: songs, vidio, kvest в отдельных потоках 
    threading.Thread(target=songs, daemon=True).start()
def round2():
    threading.Thread(target=vidio, daemon=True).start()
def round3():
    threading.Thread(target=kvest, daemon=True).start()   
# Создание основного окна
root = tk.Tk()
root.title("Джарвис")  # устанавливаем заголовок окна
root.geometry("750x600")  # Размер окна

# Создание вкладок
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Вкладка 1 - Вкладка с интерфейсом
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Поисковик')

# Вкладка 2 - Рекомендации
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Музыка')
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='Фоновые видио')
tab4 = ttk.Frame(notebook)
notebook.add(tab4, text='Истории')
tab5 = ttk.Frame(notebook)
notebook.add(tab5, text='Генерация картинок')
# текстовые виджеты для рекомендаций
text_widget1 = tk.Text(tab2, font=("Arial", 14), relief="ridge", wrap="word")
text_widget1.place(x=130, y=30, width=150, height=200)
text_widget2 = tk.Text(tab2, font=("Arial", 14), relief="ridge", wrap="word")
text_widget2.place(x=300, y=30, width=150, height=200)
text_widget3 = tk.Text(tab2, font=("Arial", 14), relief="ridge", wrap="word")
text_widget3.place(x=470, y=30, width=150, height=200)
text_widget4 = tk.Text(tab2, font=("Arial", 14), relief="ridge", wrap="word")
text_widget4.place(x=130, y=300, width=150, height=200)
text_widget5 = tk.Text(tab2, font=("Arial", 14), relief="ridge", wrap="word")
text_widget5.place(x=300, y=300, width=150, height=200)
text_widget6 = tk.Text(tab2, font=("Arial", 14), relief="ridge", wrap="word")
text_widget6.place(x=470, y=300, width=150, height=200)

text_widget7 = tk.Text(tab3, font=("Arial", 14), relief="ridge", wrap="word")
text_widget7.place(x=130, y=30, width=150, height=200)
text_widget8 = tk.Text(tab3, font=("Arial", 14), relief="ridge", wrap="word")
text_widget8.place(x=300, y=30, width=150, height=200)
text_widget9 = tk.Text(tab3, font=("Arial", 14), relief="ridge", wrap="word")
text_widget9.place(x=470, y=30, width=150, height=200)
text_widget10 = tk.Text(tab3, font=("Arial", 14), relief="ridge", wrap="word")
text_widget10.place(x=130, y=300, width=150, height=200)
text_widget11 = tk.Text(tab3, font=("Arial", 14), relief="ridge", wrap="word")
text_widget11.place(x=300, y=300, width=150, height=200)
text_widget12 = tk.Text(tab3, font=("Arial", 14), relief="ridge", wrap="word")
text_widget12.place(x=470, y=300, width=150, height=200)

text_widget13 = tk.Text(tab4, font=("Arial", 14), relief="ridge", wrap="word")
text_widget13.place(x=30, y=100, width=210, height=250)
text_widget14 = tk.Text(tab4, font=("Arial", 14), relief="ridge", wrap="word")
text_widget14.place(x=275, y=100, width=210, height=250)
text_widget15 = tk.Text(tab4, font=("Arial", 14), relief="ridge", wrap="word")
text_widget15.place(x=515, y=100, width=210, height=250)



#кнопка для изменения значения виджетов
buttonround = tk.Button(tab2, text="Обновление", command=round1)
buttonround.place(x=1, y=1)
buttonround = tk.Button(tab3, text="Обновление", command=round2)
buttonround.place(x=1, y=1)
buttonround = tk.Button(tab4, text="Обновление", command=round3)
buttonround.place(x=1, y=1)
#текстовый виджет для вывода ответа функции - gbt()
text_widget = tk.Text(tab1, font=("Arial", 14), relief="ridge", wrap="word")
text_widget.place(x=65, y=150, width=505, height=300)

#label для помощи в интерфейсе
label2 = ttk.Label(tab1, text="Вызов помошника \n \n                 O \n \n Анализ речи \n \n                 o \n \n Нейросеть \n \n                 o \n")
label2.place(x=605, y=200)

#поле для ввода вопросов
entry_var = tk.StringVar()
entry = tk.Entry(tab1, textvariable=entry_var)
entry.place(x=65, y=84, width=460, height=25)

#кнопка для отправки запросов
button = tk.Button(tab1, text="поиск", command=get_input_text)
button.place(x=525, y=85)
#поле для ввода запросов
entry_var2 = tk.StringVar()
entry = tk.Entry(tab5, textvariable=entry_var2)
entry.place(x=85, y=84, width=460, height=25)

#кнопка для отправки запросов для генерации
button10 = tk.Button(tab5, text="сгенерировать", command=get_input_text2)
button10.place(x=545, y=85)

# Настройка стиля для вкладок
style = ttk.Style()
style.configure("TFrame", background="lavender")  # Установить цвет фона для всех фреймов
style.configure("TNotebook", background="lavender")  # Установить цвет фона для вкладок
canvas = Canvas(tab5, bg="lavender", width=350, height=350,highlightthickness=0)
canvas.place(x=275, y=210)

# Create main arcs (ball and ball1)
ball = canvas.create_arc(7, 7, 170, 170, start=200, extent=200, outline="grey29", style="arc", width=4)
motion(0)

ball1 = canvas.create_arc(7, 7, 170, 170, start=0, extent=10, outline="grey57", style="arc", width=4)
motion1(0)

# Create static inner ovals
canvas.create_oval(20, 20, 155, 155, fill="LightSteelBlue2", outline="DarkSlateGray", width=3)
canvas.create_oval(60, 60, 115, 115, fill="DarkSlateGray1", outline="DarkSlateGray", width=4)
canvas.create_oval(70, 70, 105, 105, fill="mint cream", outline="DarkSlateGray1", width=3)

# Create 6 `ball2` arcs evenly spaced
ball2 = []
num_balls = 6

for i in range(num_balls):
    arc = canvas.create_arc(30, 30, 145, 145, start=i * 60, extent=10, outline="grey57", style="arc", width=20)
    ball2.append(arc)  # Store the arc in a list
    motion2(0, i)  # Call motion2 for each arc

# Включаем фон для вкладки 1
tab1.configure(style="TFrame")
tab2.configure(style="TFrame")

# Запускаем выполнения функций в отдельных потоках
threading.Thread(target=run_jarvis, daemon=True).start()
threading.Thread(target=songs, daemon=True).start()
threading.Thread(target=vidio, daemon=True).start()
threading.Thread(target=kvest, daemon=True).start()
# Запуск главного цикла приложения
root.mainloop()

