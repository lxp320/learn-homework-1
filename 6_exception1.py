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
    # Бесконечный цикл
    while True:
        # Попытка принять пользовательский ввод
        try:
            input('Как дела?\n')
        # Перехват KeyboardInterrupt (Ctrl + C)
        except KeyboardInterrupt:
            # Вывод прощания
            print("Пока!")
            # Выход из бесконечного цикла
            break

    
if __name__ == "__main__":
    hello_user()
