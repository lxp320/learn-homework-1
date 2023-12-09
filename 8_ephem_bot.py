"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
# Импорт модулей
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
# Модуль для работы с датой
from datetime import date
# Модуль для астрономических вычислений
import ephem
# Логгирование
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

# Функция для обработки команды старт
def greet_user(update, context):
    # переменная с текстом для пользователя
    text = f"Привет!\n"\
            "Я умею определять в каком созвездии находится планета\n"\
            "Введи /planet 'Имя планеты по английски'\n"\
            "Например: /planet Mars"
    print(text)
    # Отправка текста пользователю
    update.message.reply_text(text)

# Функция для определения созвездия планеты    
def constellation_identifier(space_body):
    # Попытка выполнить код
    try:
        # Пользовательский ввод приводится к нужному регистру для подстановки в атрибут 
        space_body = space_body.capitalize()
        # Подстановка названия планеты в атрибут функции ephem
        planet = getattr(ephem, space_body)(date.today())
        # Определение созвездия
        constellation = ephem.constellation(planet)
        return constellation
    # Если пользователь ввел название планеты не правильно перехватим ошибку
    except AttributeError:
        return(f'Указана неизвестная планета: {space_body} !!!\n'
                'Я постараюсь разузнать что-нибудь о ней, а Вы пока что попробуйте указать другую.')
# Функция для обработки поступающего текста
def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    # Деление пользовательского ввода на слова
    command = user_text.split()
    # Если была команда /planet
    if command[0] == '/planet':
        print('Обнаружено: /planet')
        # Запрос ответа о созвездии у функции определения созвездия
        constellation = constellation_identifier(command[1])
        # Отправление ответа пользователю
        update.message.reply_text(constellation)
    # Если команды /planet не было, то возвращаем сообщение пользователю
    else:
        update.message.reply_text(user_text)


# Функция с основным кодом бота
def main():
    # Создание бота и передача ему ключа для авторизации
    mybot = Updater(settings.API_KEY, use_context=True)

    # Присвоение переменной dp диспетчера бота для сокращения и удобства
    dp = mybot.dispatcher
    # Добавление обработчика команды старт диспетчеру
    dp.add_handler(CommandHandler("start", greet_user))
    # Добавление обработчика команды старт диспетчеру
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    # Запуск запросов к Telegram о наличии новых сообщений 
    mybot.start_polling()
    # Запуск бота. Остановка только принудительно
    mybot.idle()


if __name__ == "__main__":
    main()
