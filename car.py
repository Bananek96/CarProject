from position import Position
from map import Map

class Car:
    def __init__(self):
        self.speed: int = 0  # m/s
        self.position = Position()

    def __str__(self) -> str:
        return (f"x: {self.position.x}, y: {self.position.y}, angle: {self.position.angle}")

    def get_position(self) -> Position:
        return self.position

    def move_forward(self, speed: int) -> None:
        self.speed = speed

    def measure_distance(self) -> int:
        raise NotImplementedError("To Do")

    def turn(self, angle) -> None:
        self.position.angle = angle

    def load(self, map: Map) -> None:
        raise NotImplementedError("To Do")

    def stop(self) -> None:
        self.speed = 0

    def move_backwards(self, speed) -> None:
        self.speed = speed * (-1)

    def run_model(self, delta_t: int):
        angle = self.position.angle
        if angle > 360:
            ile = angle / 360
            angle = angle - ile * 360
        else:
            if angle == 0:
                self.position.y = self.position.y + delta_t * self.speed
            elif angle == 90:
                self.position.x = self.position.x + delta_t * self.speed
            elif angle == 180:
                self.position.y = self.position.y - delta_t * self.speed
            elif angle == 270:
                self.position.x = self.position.x - delta_t * self.speed
