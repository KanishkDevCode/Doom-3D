import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
# from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(True)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.mouse_sensitivity = MOUSE_SENSITIVITY
        self.state = 'MENU'
        self.new_game()

    def new_game(self):
        self.map =  Map(self)
        self.player  = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        # self.static_sprite = SpriteObjects(self)
        # self.animated_sprite = AnimatedSprite(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)

    def update(self):
        if self.state == 'PLAYING':
            self.player.update()
            self.raycasting.update()
            # self.static_sprite.update()
            # self.animated_sprite.update()
            self.object_handler.update()
            self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps(): .1f}')

    def draw(self):
        if self.state == 'PLAYING':
            self.object_renderer.draw() # Gives a 3D Environment
            self.weapon.draw()
            self.object_renderer.draw_hud()
        elif self.state == 'MENU':
            self.object_renderer.draw_menu()
        elif self.state == 'SETTINGS':
            self.object_renderer.draw_settings()
        elif self.state == 'GAME_OVER':
            self.object_renderer.draw_game_over()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            
            if self.state == 'PLAYING':
                self.player.single_fire_event(event)
            elif self.state == 'MENU':
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = pg.mouse.get_pos()
                    for i, option in enumerate(['Play', 'Settings', 'Exit']):
                        rect = self.object_renderer.font.render(option, True, 'white').get_rect(center=(HALF_WIDTH, HALF_HEIGHT + i * 80))
                        if rect.collidepoint(mx, my):
                            if option == 'Play':
                                self.state = 'PLAYING'
                                pg.mouse.set_visible(False)
                                self.new_game()
                            elif option == 'Settings':
                                self.state = 'SETTINGS'
                            elif option == 'Exit':
                                pg.quit()
                                sys.exit()
            elif self.state == 'SETTINGS':
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mx, my = pg.mouse.get_pos()
                    sens_text = f"Mouse Sensitivity: {self.mouse_sensitivity:.5f}"
                    rect1 = self.object_renderer.font.render(sens_text, True, 'white').get_rect(center=(HALF_WIDTH, HALF_HEIGHT))
                    rect2 = self.object_renderer.font.render("Back", True, 'white').get_rect(center=(HALF_WIDTH, HALF_HEIGHT + 100))
                    
                    if rect1.collidepoint(mx, my):
                        if self.mouse_sensitivity == 0.0002:
                            self.mouse_sensitivity = 0.0004
                        elif self.mouse_sensitivity == 0.0004:
                            self.mouse_sensitivity = 0.0001
                        else:
                            self.mouse_sensitivity = 0.0002
                    elif rect2.collidepoint(mx, my):
                        self.state = 'MENU'
            elif self.state == 'GAME_OVER':
                if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                    self.state = 'MENU'
                    pg.mouse.set_visible(True)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()