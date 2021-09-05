class CAR:

    def __init__(self, color, brand, speed):
        self.wheel = 4
        self.stearing = 1
        self.color=color
        self.brand=brand
        self.speed=speed

    def print_car(self):
        print(f'wheel: {self.wheel}')
        print(f'stearing: {self.stearing}')
        print(f'color: {self.color}')
        print(f'brand: {self.brand}')
        print(f'speed: {self.speed}')