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
