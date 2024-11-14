
class Position:
	"""
		angle = 0, pojazd skierowany na północ
	"""
	def __init__(self, init_x: float, init_y: float):
		self.x: float = init_x
		self.y: float = init_y
		self.angle: float = 0