from position import Position
from map import Map
import math

class Car:
    def __init__(self):
        self.speed: int = 0  # m/s
        Map().prepare_map()
        word_map_array = Map().load_map_from_image('maze.png')
        self.load_map(word_map_array)
        size_x = int(len(word_map_array)/2)
        size_y = int(len(word_map_array[1])/2)
        # jest ryzyko ze trafilismy w sciane
        # 0 to jest sciana
        for _ in range(size_x):
            if(word_map_array[size_x][size_y]==1):
                break
            size_x = size_x+1
        self.position = Position(init_x=size_x, init_y=size_y)

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
        self.word_map = map

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
