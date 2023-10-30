class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width **2 + self.height**5) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture'

        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, other_shape):
        return (self.width // other_shape.width) * (self.height // other_shape.height)

    def __str__(self):
        return f'Rectangle = width{self.width}, height={self.height}'

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side

    def set_height(self, side):
        self.height = side

    def __str__(self):
        return f'Square(side={self.width}'


rectangle= Rectangle(10, 5)
area = rectangle.get_area()
print(area)
diagonal = rectangle.get_diagonal()
print(diagonal)
picture = rectangle.get_picture()
print(picture)
square = Rectangle(4,4)
print(rectangle.get_amount_inside(square))
square = Square(5)
print(square.get_area())
print(square.get_picture())

