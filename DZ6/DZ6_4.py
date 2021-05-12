"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def show_speed(self):
        print(f"текущая скорость автомобиля: {self.speed}")

    def go(self):
        if self.speed > 0:
            print("машина едет")

    def stop(self):
        if self.speed == 0:
            print("машина стоит")

    def turn(self, side):
        if side == "left":
            print("налево")
        elif side == "right":
            print("направо")
        else:
            print("прямо")

    def Name(self):
        print(self.name, self.color)


class TownCar(Car):
    def show_speed(self):
        print(f"текущая скорость автомобиля: {self.speed}")
        if self.speed > 60:
            print(f"автомобиль превышает скорость на {self.speed - 60}")


class WorkCar(TownCar):
    pass


class SportCar(Car):
    pass


class PoliceCar(Car):
    def police(self):
        if self.is_police:
            print("мигалка включена")


lada = TownCar(70, "баклажан", "Лада седан", False)
lada.Name()
lada.show_speed()
lada.go()
lada.stop()
lada.turn("едем")
print()
Bentley = WorkCar(130, "чёрный", "Bentley Continental Flying Spur", False)
Bentley.Name()
Bentley.show_speed()
Bentley.go()
Bentley.stop()
Bentley.turn("right")
print()
Volga = PoliceCar(130, "жёлтый", "ГАЗ-21", True)
Volga.Name()
Volga.show_speed()
Volga.go()
Volga.stop()
Volga.turn("left")
Volga.police()
print()
Mercedes = SportCar(0, "Серебристый", "AMG GT", False)
Mercedes.Name()
Mercedes.show_speed()
Mercedes.go()
Mercedes.stop()
Mercedes.turn("123")
