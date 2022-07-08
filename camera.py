import pygame as pg


class Camera:

	def __init__(self, width, height):

		self.width = width
		self.height = height

		self.scroll = pg.Vector2(0, 0)
		self.dx = 0
		self.dy = 0
		self.speed = 20

	def update(self):

		mouse_pos = pg.mouse.get_pos()
		keys = pg.key.get_pressed()

		if keys[pg.K_w]:
			self.dy = self.speed
		elif keys[pg.K_s]:
			self.dy = -self.speed
		else:
			self.dy = 0

		if keys[pg.K_a]:
			self.dx = self.speed
		elif keys[pg.K_d]:
			self.dx = -self.speed
		else:
			self.dx = 0

		# update camera scroll	
		self.scroll.x += self.dx
		self.scroll.y += self.dy




#mouse controls that really suck
				# x movement
		#if mouse_pos[0] > self.width * 0.97:
			#self.dx = -self.speed
		#elif mouse_pos[0] < self.width * 0.03:
			#self.dx = self.speed
		#else:
			#self.dx = 0

		# y movement
		#if mouse_pos[1] > self.height * 0.97:
			#self.dy = -self.speed
		#elif mouse_pos[1] < self.height * 0.03:
			#self.dy = self.speed
		#else:
			#self.dy = 0