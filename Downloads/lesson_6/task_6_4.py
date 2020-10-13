
class Car:
    speed = 0
    color = 0
    name = 0
    is_police = True

    def go(self):
        print('Поехали')

    def stop(self):
        print('Stop')

    def turn(self, direction):
        print('Поворачиваем', direction)

    def show_speed(self):
        speed = 80
        print(speed)

class TownCar(Car):
    def show_speed(self):
        speed = 0
        print(speed)
        if speed > 60:
            print('Превышение скорости выше 60км/ч')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        speed = 0
        print(speed)
        if speed > 40:
            print('Превышение скорости выше 40км/ч')

class PoliceCar(Car):
    pass

my_car = Car()
my_car.turn('right')
my_car.show_speed()