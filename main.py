#Импорт всех функций и классов из файла rects.py
from collision import (
    isCorrectRect,
    RectCorrectError,
    isCollisionRect,
    intersectionAreaRect,
    intersectionAreaMultiRect
)


#Пример 1: Проверка корректности прямоугольника
rect1 = [(0, 0), (3, 4)]
rect2 = [(1, 1), (2, 3)]
rect_invalid = [(2, 2), (1, 1)]

print(isCorrectRect(rect1))        # True
print(isCorrectRect(rect_invalid)) # False

#Пример 2: Проверка пересечения двух прямоугольников
try:
    collision = isCollisionRect(rect1, rect2)
    print(f"Прямоугольники пересекаются: {collision}")  # True
except RectCorrectError as e:
    print(e)

#Пример 3: Площадь пересечения двух прямоугольников
area = intersectionAreaRect(rect1, rect2)
print(f"Площадь пересечения: {area}")  # 2

#Пример 4: Площадь пересечения нескольких прямоугольников
rect3 = [(1, 0), (4, 3)]
rectangles = [rect1, rect2, rect3]
try:
    multi_area = intersectionAreaMultiRect(rectangles)
    print(f"Площадь пересечения всех прямоугольников: {multi_area}")  # 1
except RectCorrectError as e:
    print(e)
