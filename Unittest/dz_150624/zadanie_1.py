# Задание 1: Площадь и периметр прямоугольника
# Описание задачи
# Напишите программу, которая запрашивает у пользователя длину и ширину прямоугольника и выводит его площадь и периметр.

# Функции для реализации:
# calculate_area(length, width) - возвращает площадь прямоугольника.
# calculate_perimeter(length, width) - возвращает периметр прямоугольника.


#   --Unit Tests--
#   Тесты для функции calculate_area:
# Проверьте правильность расчёта площади для стандартных значений длины и ширины.
# Убедитесь, что функция корректно обрабатывает крайние случаи, например, когда длина или ширина равны нулю.

#   Тесты для функции calculate_perimeter:
# Проверьте правильность расчёта периметра для стандартных значений.
# Проверьте случаи, когда один из параметров равен нулю, чтобы убедиться в правильности расчёта.

#############################################################################################################

import os

def clear_terminal():
    # Проверяем, какая операционная система используется
    if os.name == 'nt':  # Для Windows
        os.system('cls')
    else:  # Для Unix-подобных систем
        os.system('clear')

def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Длина и ширина должны быть положительными числами")
    return length * width

def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Длина и ширина должны быть положительными числами")
    return 2 * (length + width)

def main():
    try:
        length = float(input("Введите длину: "))
        width = float(input("Введите ширину: "))
        
        clear_terminal()
        
        area = calculate_area(length, width)
        perimeter = calculate_perimeter(length, width)
        
        print(f"Площадь прямоугольника со сторонами {length} и {width} равна: {area}")
        print(f"Периметр прямоугольника со сторонами {length} и {width} равен: {perimeter}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()




