from position import Position
from map import Map
import math

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

    def load_map(self, map: Map) -> None:
        raise NotImplementedError("To Do")

    def stop(self) -> None:
        self.speed = 0

    def move_backwards(self, speed) -> None:
        self.speed = speed * (-1)

    def run_model(self, delta_t: float):
        angle = self.position.angle

        # Convert angle to radians (trigonometric functions in Python use radians)
        angle_radians = math.radians(angle)

        # Calculation of displacement in the X and Y axes based on angle, velocity and delta_t
        delta_y = math.cos(angle_radians) * self.speed * delta_t
        delta_x = math.sin(angle_radians) * self.speed * delta_t

        # Position update
        self.position.x += delta_x
        self.position.y += delta_y
