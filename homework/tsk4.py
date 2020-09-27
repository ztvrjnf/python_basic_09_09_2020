"""
Реализуйте базовый класс Car. У данного класса должны быть
следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны
сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar. Добавьте в базовый класс метод show_speed, который
должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    # attributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} has started'

    def stop(self):
        return f'{self.name} has stopped'

    def turn_right(self):
        return f'{self.name} has turned right'

    def turn_left(self):
        return f'{self.name} has turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allowed for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allowed for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


model_s = SportCar(130, 'Dark blue', 'Model S', False)
lancer = TownCar(60, 'Navy', 'Lancer', False)
duster = WorkCar(70, 'Black', 'Duster', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(duster.turn_left())
print(f'When {lancer.turn_right()}, {model_s.stop()}')
print(f'{lancer.go()} with speed {lancer.show_speed()}')
print(f'{duster.go()} with speed {duster.show_speed()}')
print(f'{duster.name} is {lancer.color}')
print(f'Is {duster.name}  a police car? {duster.is_police}')
print(model_s.show_speed())
print(lancer.show_speed())
print(ford.show_speed())
