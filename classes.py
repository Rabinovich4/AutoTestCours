class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def display(self):
        print(f'Координата X: {self.x} Координата Y: {self.y}')


coords = Point(1, 2)
coords.display()

coords.move(5, 6)
coords.display()