
class Stationery:
    title = 'None'
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')

class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')

my_tool = Stationery()
my_tool.draw()
my_handle = Handle()
my_handle.draw()
my_pencil = Pencil()
my_pencil.draw()
my_pen = Pen()
my_pen.draw()
