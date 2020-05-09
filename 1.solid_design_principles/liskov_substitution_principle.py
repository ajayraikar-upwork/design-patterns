# Liscov Substituion Principle
'''
* You should be able to substitute a base type for a subtype
'''

class Rectagle:
    def __init__(self, width, height):
        self._height = height
        self._width = width


    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value



class Square(Rectagle):
    def __init__(self, size):
        Rectagle.__init__(self, size, size)

    @Rectagle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectagle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {rc.area}')

rc = Rectagle(2, 3)
use_it(rc)

s = Square(5)
use_it(s)