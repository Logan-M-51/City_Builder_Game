import pygame as pg
from game import Game
from menu import StartMenu, GameMenu

def main():

	 running = True

	 pg.init()
	 pg.mixer.init()
	 screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
	 pg.display.set_caption("WANNABE REMASTER")
	 pg_icon = pg.image.load("assets/graphics/icon.png").convert_alpha()
	 pg.display.set_icon(pg_icon)
	 clock = pg.time.Clock()

	 #implement menus
	 start_menu = StartMenu(screen, clock)
	 game_menu = GameMenu(screen, clock)

	 game = Game(screen, clock)

	 while running:

	 	#start menu
	 	playing = start_menu.run()

	 	while playing:
	 		#game loop
	 		game.run()
			#pause loop here
	 		playing = game_menu.run()

if __name__ == "__main__":
	main()
