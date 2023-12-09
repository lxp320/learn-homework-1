"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
# Функция сравнения двух строк
def string_comparison(str1, str2):
    # Проверка переданы ли две строки функции
    if isinstance(str1, str) and isinstance(str2, str):
        # Проверка равны ли строки
        if str1 == str2:
            return 1
        # Проверка длиннее ли первая строка
        elif len(str1) > len(str2):
            return 2
        # Проверка равнали вторая строка 'learn'
        elif str2 == 'learn':
            return 3
    # Возвращаем 0, если str1 или str2 не строка
    else:
        return 0

#Тесты
#print(string_comparison(1, '1'))          # Не строки
#print(string_comparison('1', '1'))        # Строки одинаковые
#print(string_comparison('11', '1'))       # Первая длиннее
#print(string_comparison('11', 'learn'))   # вторая строка 'learn'

# Списки с данными для передачи в функцию
list1 = ['строка', 'обычная строка', 'обычная строка', 'учить']
list2 = [123, 'обычная строка', 'я строка', 'learn']

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    # Цикл для вызова функции несколько раз с разными данными
    for i in range(len(list1)):
        print(str(list1[i]) + ' | ' + str(list2[i]))
        print('Результат: ' + str(string_comparison(list1[i],list2[i])))
        print()
    
if __name__ == "__main__":
    main()
