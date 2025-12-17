# Работа с прямоугольниками

## Описание
Проект предоставляет функции для работы с прямоугольниками на плоскости. Основные возможности:  
- Проверка корректности прямоугольника  
- Проверка пересечения двух прямоугольников  
- Вычисление площади пересечения двух прямоугольников  
- Вычисление площади пересечения нескольких прямоугольников  

## Определения
- Прямоугольник задается двумя точками: левой нижней и правой верхней, например: `[(x_min, y_min), (x_max, y_max)]`  
- Корректный прямоугольник: `x_min < x_max` и `y_min < y_max`  

## Требования
- Python 3.11 или выше  

## Функции

### `isCorrectRect(points)`
Проверяет корректность прямоугольника.  
**Вход:** список или кортеж двух точек `[(x1, y1), (x2, y2)]`  
**Выход:** `True` или `False`  

### `isCollisionRect(rect1, rect2)`
Проверяет пересечение двух прямоугольников.  
**Вход:** два корректных прямоугольника  
**Выход:** `True`, если есть пересечение, иначе `False`  
**Исключения:** `RectCorrectError` при некорректных прямоугольниках  

### `intersectionAreaRect(rect1, rect2)`
Вычисляет площадь пересечения двух прямоугольников.  
**Вход:** два корректных прямоугольника  
**Выход:** площадь пересечения (число, 0 если нет пересечения)  

### `intersectionAreaMultiRect(rectangles)`
Вычисляет площадь пересечения нескольких прямоугольников.  
**Вход:** список корректных прямоугольников  
**Выход:** площадь пересечения всех прямоугольников, 0 если пересечения нет  
**Исключения:** `RectCorrectError` при некорректных прямоугольниках  

## Примеры использования
```python
from collision import (
    isCorrectRect,
    RectCorrectError,
    isCollisionRect,
    intersectionAreaRect,
    intersectionAreaMultiRect
)

rect1 = [(0, 0), (3, 4)]
rect2 = [(1, 1), (2, 3)]
rect_invalid = [(2, 2), (1, 1)]

print(isCorrectRect(rect1))        # True
print(isCorrectRect(rect_invalid)) # False

try:
    collision = isCollisionRect(rect1, rect2)
    print(f"Прямоугольники пересекаются: {collision}")  # True
except RectCorrectError as e:
    print(e)

area = intersectionAreaRect(rect1, rect2)
print(f"Площадь пересечения: {area}")  # 2

rect3 = [(1, 0), (4, 3)]
rectangles = [rect1, rect2, rect3]
try:
    multi_area = intersectionAreaMultiRect(rectangles)
    print(f"Площадь пересечения всех прямоугольников: {multi_area}")  # 1
except RectCorrectError as e:
    print(e)
