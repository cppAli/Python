#   --Unit Tests--
#   Тесты для функции calculate_area:
# Проверьте правильность расчёта площади для стандартных значений длины и ширины.
# Убедитесь, что функция корректно обрабатывает крайние случаи, например, когда длина или ширина равны нулю.

#   Тесты для функции calculate_perimeter:
# Проверьте правильность расчёта периметра для стандартных значений.
# Проверьте случаи, когда один из параметров равен нулю, чтобы убедиться в правильности расчёта.

import unittest
from zadanie_1 import calculate_area, calculate_perimeter

#правильность для стандартных значений
class TestCalculateArea(unittest.TestCase):
    #OK
    def test_calculate_area(self):
        self.assertEqual(calculate_area(5, 6), 30)
        self.assertEqual(calculate_area(10, 10), 100)
        
    #OK 0
    def test_zero_values(self):
        with self.assertRaises(ValueError):
            calculate_area(0, 4)
        with self.assertRaises(ValueError):
            calculate_area(5, 0)
        with self.assertRaises(ValueError):
            calculate_area(0, 0)
    
    #OK
    def calculate_perimeter(self):
        self.assertEqual(calculate_perimeter(5, 6), 22)
        self.assertEqual(calculate_perimeter(10, 10), 40)
    
    #OK 0
    def calculate_perimetr_zero(self):
        with self.assertRaises(ValueError):
            calculate_perimeter(0, 4)
        with self.assertRaises(ValueError):
            calculate_perimeter(4, 0)
        
        
if __name__ == "__main__":
    unittest.main()