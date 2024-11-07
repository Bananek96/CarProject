import random
import numpy as np
from PIL import Image, ImageDraw

class Map:

	def generate_maze(self, width, height):
		# Ustawiamy wszystkie komórki jako ściany (wartość 0)
		maze = np.zeros((height, width), dtype=int)
		
		# Używamy stosu do implementacji DFS
		stack = [(0, 0)]
		maze[0, 0] = 1  # Początkowa komórka jako przejście
		
		# Definiujemy cztery kierunki ruchu z odstępem 4 jednostek dla większych przejść
		directions = [(0, 4), (0, -4), (4, 0), (-4, 0)]
		
		while stack:
			x, y = stack[-1]
			
			# Tworzymy listę sąsiednich komórek, które są oddzielone ścianą
			neighbors = []
			for dx, dy in directions:
				nx, ny = x + dx, y + dy
				if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0:
					neighbors.append((nx, ny))
			
			if neighbors:
				# Wybieramy losowego sąsiada i usuwamy ścianę między komórkami
				nx, ny = random.choice(neighbors)
				maze[(y + ny) // 2][(x + nx) // 2] = 1  # Usuwamy ścianę między komórkami
				maze[ny][nx] = 1  # Przekształcamy sąsiada w przejście
				stack.append((nx, ny))
			else:
				stack.pop()  # Brak sąsiadów - cofamy się
				
		return maze

	def draw_maze(self, maze, cell_size=5, passage_width=3, output_filename="maze.png"):
		height, width = maze.shape
		img_width = width * cell_size
		img_height = height * cell_size
		image = Image.new("RGB", (img_width, img_height), "black")  # Ustawienie czarnego tła (ściany)
		draw = ImageDraw.Draw(image)
		
		# Rysujemy przejścia w labiryncie na biało
		for y in range(height):
			for x in range(width):
				if maze[y][x] == 1:  # Jeśli komórka jest częścią przejścia
					# Rysujemy większy prostokąt dla przejścia
					top_left = (x * cell_size, y * cell_size)
					bottom_right = (top_left[0] + passage_width * cell_size, top_left[1] + passage_width * cell_size)
					draw.rectangle([top_left, bottom_right], fill="white")  # Wypełnienie białych przejść
		
		# Zapisujemy obraz jako 100x100 pikseli
		image = image.resize((300, 300), Image.NEAREST)
		image.save(output_filename)
		print(f"Maze saved as {output_filename}")

	def prepare_map(self):	

		# Parametry
		maze_width = 41  # liczba komórek w szerokości labiryntu (musi być nieparzysta dla przejść)
		maze_height = 41  # liczba komórek w wysokości labiryntu (musi być nieparzysta)
		cell_size = 5  # rozmiar komórki w pikselach
		passage_width = 3  # szerokość przejścia (w liczbie komórek)

		# Generacja i zapis labiryntu
		maze = self.generate_maze(maze_width, maze_height)
		self.draw_maze(maze, cell_size=cell_size, passage_width=passage_width)

Map().prepare_map()
