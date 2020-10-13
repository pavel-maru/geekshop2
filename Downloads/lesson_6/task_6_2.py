
class Road:
    def __init__(self):
        self._length = 0
        self._width = 0

    def mass(_length, _width, dencity, s):
        return _length * _width * dencity * s

road_1 = Road
print(f'{road_1.mass(_length=5000, _width=20, dencity=25, s=5)} кг')
