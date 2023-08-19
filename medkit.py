import pyttsx3
import speech_recognition as sr
import requests

# Инициализация движка для воспроизведения звука
engine = pyttsx3.init()

# Функция для воспроизведения ответа
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Функция для распознавания речи
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите что-нибудь...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="ru-RU")
            print("Вы сказали:", text)
            return text
        except sr.UnknownValueError as e:
            print(e)
            pass

# Функция для перевода текста
def translate_text(text, target_lang):
    api_key = "ВАШ_КЛЮЧ_API_YANDEX_TRANSLATE"
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    params = {
        "key": api_key,
        "text": text,
        "lang": target_lang
    }
    response = requests.post(url, params=params)
    translation = response.json()["text"][0]
    return translation

# Функция для интеграции Yandex GPT
def integrate_GPT():
    text = listen()
    if text:
        translated_text = translate_text(text, "en")
        speak(translated_text)

# Основной цикл программы
while True:
    command = listen().lower()
    if command:
        if "привет" in command:
            speak("Привет! Что Вас беспокоит?")
        elif "как дела" in command:
            speak("У меня все отлично, спасибо!")
        elif "пока" in command:
            speak("До свидания!")
            break
        else:
            integrate_GPT()
    else:
        speak("Извините, я не расслышал команду.")