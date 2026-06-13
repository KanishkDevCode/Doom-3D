import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/textures/sky.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.blood_screen = self.get_texture('resources/textures/blood_screen.png', RES)
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'resources/textures/digits/{i}.png', [self.digit_size] * 2)
                              for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_image = self.get_texture('resources/textures/game_over.png', RES)
        self.win_image = self.get_texture('resources/textures/win.png', RES)
        self.font = pg.font.SysFont('Arial', 50, bold=True)
        self.title_font = pg.font.SysFont('Arial', 100, bold=True)

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def win(self):
        self.screen.blit(self.win_image, (0, 0))

    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def draw_hud(self):
        self.draw_player_health()
        self.draw_player_ammo()

    def draw_player_ammo(self):
        ammo_text = self.font.render(f'AMMO: {self.game.player.ammo}', True, 'yellow')
        self.screen.blit(ammo_text, (WIDTH - ammo_text.get_width() - 20, 20))

    def draw_menu(self):
        self.screen.fill('black')
        title = self.title_font.render('DOOM 3D', True, 'darkred')
        self.screen.blit(title, (HALF_WIDTH - title.get_width() // 2, HALF_HEIGHT - 200))
        
        mx, my = pg.mouse.get_pos()
        options = ['Play', 'Settings', 'Exit']
        for i, option in enumerate(options):
            text = self.font.render(option, True, 'white')
            rect = text.get_rect(center=(HALF_WIDTH, HALF_HEIGHT + i * 80))
            if rect.collidepoint(mx, my):
                text = self.font.render(option, True, 'yellow')
            self.screen.blit(text, rect)

    def draw_settings(self):
        self.screen.fill('black')
        title = self.title_font.render('SETTINGS', True, 'darkred')
        self.screen.blit(title, (HALF_WIDTH - title.get_width() // 2, HALF_HEIGHT - 200))
        
        mx, my = pg.mouse.get_pos()
        sens_text = f"Mouse Sensitivity: {self.game.mouse_sensitivity:.5f}"
        
        text1 = self.font.render(sens_text, True, 'white')
        rect1 = text1.get_rect(center=(HALF_WIDTH, HALF_HEIGHT))
        if rect1.collidepoint(mx, my):
            text1 = self.font.render(sens_text, True, 'yellow')
            
        text2 = self.font.render("Back", True, 'white')
        rect2 = text2.get_rect(center=(HALF_WIDTH, HALF_HEIGHT + 100))
        if rect2.collidepoint(mx, my):
            text2 = self.font.render("Back", True, 'yellow')
            
        self.screen.blit(text1, rect1)
        self.screen.blit(text2, rect2)

    def draw_game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))
        prompt = self.font.render('Press ENTER for Menu', True, 'white')
        self.screen.blit(prompt, (HALF_WIDTH - prompt.get_width() // 2, HEIGHT - 100))

    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size, 0))
        self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size, 0))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        #Floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse = True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return{
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.png'),
            5: self.get_texture('resources/textures/5.png'),
        }