def isCorrectRect(points):
    if not isinstance(points, (list, tuple)) or len(points) != 2:
        return False

    try:
        (x1, y1), (x2, y2) = points
    except (TypeError, ValueError):
        return False

    #Проверка корректности прямоугольника:
    #Левая нижняя точка должна быть строго левее и ниже правой верхней
    return x1 < x2 and y1 < y2

class RectCorrectError(Exception):
    pass

def isCollisionRect(rect1, rect2):
    #Проверка корректности первого прямоугольника
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")
    #Проверка корректности второго прямоугольника
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")
    (x1_min, y1_min), (x1_max, y1_max) = rect1
    (x2_min, y2_min), (x2_max, y2_max) = rect2
    #Проверка пересечения прямоугольников
    return not (
        x1_max <= x2_min or  # rect1 левее rect2
        x2_max <= x1_min or  # rect2 левее rect1
        y1_max <= y2_min or  # rect1 ниже rect2
        y2_max <= y1_min     # rect2 ниже rect1
    )

