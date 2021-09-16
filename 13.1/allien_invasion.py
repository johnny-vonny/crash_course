import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from random import randint

class AllienInvasion:
	"""Класс для управления ресурсами и поведением игры"""

	def __init__(self):
		"""Инициализирует игру и создает игровые ресурсы."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		# self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		# self.settings.screen_width = self.screen.get_rect().width
		# self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.random_number = randint(-200, 200)

		self._create_fleet()


	def run_game(self):
		"""Запуск основного цикла игры."""
		while True:
			self._check_events()			
			self.ship.update()
			self._update_bullets()
			self._update_screen()



	def _check_events(self):
		"""Обрабаотывает нажатия клавиш и события мыши."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type ==pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Реагирует на нажатие клавиш."""
		if event.key == pygame.K_RIGHT:
			# Переместить корабль вправо
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Реагирует на нажатие клавиш."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Создание нового снаряда и включение его в группу bullets."""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Обновляет позиции снарядов и уничтожает старые снаряды."""
		# Обновление позиций снарядов.
		self.bullets.update()

		# Удаление снарядов, вышедших за край экрана.
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def _create_fleet(self):
		"""Созданут флот пришельцев."""
		# Создание пришельца и вычисление количества пришельцев в ряду.
		# Интервал между соседними пришельцами равен ширине пришельца.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		avaliable_space_x = self.settings.screen_width - alien_width 
		number_aliens_x = avaliable_space_x // (2 * alien_width)

		"""Определяет количество рядов, помещающихся на экране."""
		ship_height = self.ship.rect.height
		avaliable_space_y = (self.settings.screen_height)
		number_rows = avaliable_space_y // (2 * alien_height)

		# Создание флота вторжения.
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				random_number = randint(-50, 50)
				self._create_alien(alien_number, row_number, random_number)


	def _create_alien(self, alien_number, row_number, random_number):
		"""Создание пришельца и размещение его в ряду."""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = random_number + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = random_number + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _update_screen(self):
		"""Обновляет изображения на экране и отображает новый экран."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		# Отображение последнего прорисованного экрана.
		pygame.display.flip()

if __name__ == '__main__':
	# Создание экземпляра и запуск игры.
	ai = AllienInvasion()
	ai.run_game()