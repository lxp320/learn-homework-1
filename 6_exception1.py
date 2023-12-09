"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
# Функция вопрос)
def hello_user():
    """
    Замените pass на ваш код
    """
    # Попытка выполнить код
    try:
        # Бесконечный цикл
        while True:
            answer = input('\nКак дела?\n -')
            if answer == 'Стоп':
                # Выход из бесконечного цикла
                break
    # Перехват KeyboardInterrupt (Ctrl + C)
    except KeyboardInterrupt:
        # Вывод прощания
        print("Пока!")
        

    
if __name__ == "__main__":
    hello_user()
