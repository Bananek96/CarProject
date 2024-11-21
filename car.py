from position import Position
from map import Map
import math
from PIL import Image, ImageDraw

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
        self.draw_position(size_x,size_y)

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
        angle_radians = math.radians(angle) *(-1)

        # Calculation of displacement in the X and Y axes based on angle, velocity and delta_t
        delta_y = math.cos(angle_radians) * self.speed * delta_t * (-1)
        delta_x = math.sin(angle_radians) * self.speed * delta_t * (-1)

        # Position update
        self.position.x += delta_x
        self.position.y += delta_y

    def draw_position(self, size_x, size_y):
        
        image_path = 'maze.png' 
        img = Image.open(image_path)
        # Współrzędne x i y dla czerwonej kropki
        x, y = size_x, size_y 
        # Stworzenie obiektu do rysowania na obrazie
        draw = ImageDraw.Draw(img)
        # Narysowanie czerwonej kropki (można zmienić rozmiar, jeśli chcesz większą)
        draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill="red")
        # Zapisanie zmodyfikowanego obrazu
        img.save('maze_position.png')
