"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
# Функция определения деятельности человека по возрасту
def activity_define(age):
    """
    1. Сад:    0...7 лет
    2. Школа   8...17 лет
    3. Вуз     18...24 лет
    4. Работа  25...100 лет 
    """
    # Проверка корректности ввода
    try:
        age = int(age)
    except ValueError:
        return('Необходимо указать целое число')                        
    if age < 0:
        return('Возраст не может быть меньше 0')
    # Определение рода деятельности
    elif 0 <= age <= 7:
        activity = 'ходит в сад'
    elif 8 <= age <= 17:
        activity = 'учится в школе'
    elif 18 <= age <= 24:
        activity = 'учится в ВУЗе'
    elif 25 <= age <= 100:
        activity = 'работает'
    else:
        return('Программа не может определить чем занимается человек старше 100 лет')
    return('Человек ' + activity)    

#Тесты
#print(activity_define('семь'))  # Не число
#print(activity_define(-1))  # Меньше нуля
#print(activity_define(6))  # Ходит в сад
#print(activity_define(14)) # Учится в школе
#print(activity_define(19)) # Учится в ВУЗе
#print(activity_define(27)) # Работает
#print(activity_define(300)) # Слишком стар

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    # Запрос возраста
    years_old = input('Укажите возраст человека:')
    # Вызов функции и присваивание результата работы переменной answ
    answ = activity_define(years_old)
    # Вывод ответа
    print(answ)

if __name__ == "__main__":
    main()
