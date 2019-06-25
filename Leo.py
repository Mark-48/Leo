'''Leo-v1.0
@-Mark7
ваши координаты элементов отличаются от координат в коде
чтобы узнать ваши координаты используете приложение cord.py
'''
from time import sleep
import pyautogui#pip install pyautogui
import random
import speech_recognition as sr #pip install SpeechRecognition

screenWidth,screenHieght=pyautogui.size()
print('Started programm....')
#функция для открытия диолога в вк
def open_br():
    print('opening diolog in vk..')
    sleep(2)
    pyautogui.click(966, 49)
    pyautogui.typewrite('https://vk.com/im?sel=-91050183')
    sleep(1.1)
    pyautogui.keyDown('Enter')
    sleep(5)

#функция для нажатия на кнопку лайк
def like():
    pyautogui.click(972,707)
    sleep(1)
#функция для нажатия на кнопку дизлайк
def ignor():
    pyautogui.click(1181,707)#нажатие на координату
    sleep(1)


#основной цикл
while True :
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:#у вас device_index другой, это микрофон используйте приложение Jarviss.py
        print('Say-')
        audio = r.listen(source)

    query = r.recognize_google(audio, language='ru-RU')
    print('You say: ' + query.lower())

    if query.lower()=='открой диалог':
        print('Ok ;)')
        open_br()
        sleep(8)

    if query.lower() == 'да':
        like()
        sleep(1)

    if query.lower() == 'нет нет' or 'нет':
        ignor()
        sleep(1)


    if query.lower()=='стоп' :
        break

print('programm.....closed....')
sleep(1)
print('By!:)')