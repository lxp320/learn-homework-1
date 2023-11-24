"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""
# Функция для расчета скидки
def discounted(price, discount, max_discount=20):
    """
    Замените pass на ваш код
    """
    # Попытка выполнить код
    try:
        # Приведение цены к положительному вещественному числу
        price = abs(float(price))
        # Приведение скидки к положительному вещественному числу
        discount = abs(float(discount))
        # Приведение цены к положительному целому числу
        max_discount = abs(int(max_discount))
        # Вызов исключения для ограничения максимального размера скидки
        if max_discount >= 100:
            raise ValueError
        # Ограничение размера скидки
        if discount >= max_discount:
            return(price)
        # Расчет цены со скидкой при условии, что проверки ранее не сработали
        else:
            return price - (price * discount / 100)
    # Обработка исключений
    except ValueError:
        return('Укажите корректные данные')
    except TypeError:
        return('Ошибка типов')
    except KeyboardInterrupt:
        # Вывод прощания
        return("Пока!")

if __name__ == "__main__":
    # Тесты
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
