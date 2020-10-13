
from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = 'off'

    def running(self):
        __color = 'red'
        print(__color)
        sleep(7)
        __color = 'yellow'
        print(__color)
        sleep(2)
        __color = 'green'
        print(__color)
        sleep(5)

my_trafficlight = TrafficLight
count = 0
while True:
    my_trafficlight.running(my_trafficlight)
    if count > 1:
        break
    count += 1
