class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimetr(self):
        return self.width * 2 + self.length * 2

    def get_area(self):
        return self.width * self.length

    perimeter = property(get_perimetr)
    area = property(get_area)

rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)