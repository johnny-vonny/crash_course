class Restaurant():
	"""Рестораны Минска"""

	def __init__(self, restaurant_name, cuisine_type, open_closed):
		"""Инициализирует атрибуты restaurant_name и cuisine_type."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.open_closed = open_closed
		self.number_served = 0

	def describe_restaurant(self):
		"""Выводит название ресторана и тип кухни"""
		print(f"{self.restaurant_name} has {self.cuisine_type} cuisine type.")

	def open_restaurant(self):
		print(f"{self.restaurant_name} is {self.open_closed} now.")

	def set_number_served(self):
		print(f"The number seved visitors is {self.number_served}.")

	def update_number_served(self, number):
		self.number_served += number


class IceCreamStand(Restaurant):
	"""Представляет собой разновидность рестора-мороженного"""

	def __init__(self, restaurant_name, cuisine_type, open_closed):
		"""Инициализация атрибуты класса-родителя"""
		super().__init__(restaurant_name,cuisine_type, open_closed)

	def print_flavors(self):
		flavors = ["apple", "banan"]
		for elem in flavors:
			print(f"We have {elem} taste.")


example_1 = IceCreamStand('villie vonka', 'ice cream', 'open')
example_1.print_flavors()