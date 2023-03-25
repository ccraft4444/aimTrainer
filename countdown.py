from settings import *
import pygame, random

class Countdown():
    def _init_(self, seconds):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(COUNTDOWN_FONT, 80)
        self.decrement_time = pygame.time.get_ticks()
        self.should_decrement = False
        self.time_left = int(seconds)
        self.initial_countdown_length = self.time_left
        self.target_group = pygame.sprite.Group()
        self.targets_spawned = 0
    
    def cooldowns(self):
        curr_time = pygame.time.get_ticks()

        if not self.should_decrement and self.time_left > 0:
            if curr_time - self.decrement_time > 999:
                self.should_decrement = True

    def draw_timer(self):
        if self.should_decrement:
            self.time_left -= 1
            self.decrement_time = pygame.time.get_ticks()
            self.should_decrement = False
        if self.time_left > 0:
            count_string = str(self.time_left)
        else:
            count_string = ""

        count_surf = self.font.render(count_string, True, TEXT_COLOR, None)
        x , y = WIDTH - 20, HEIGHT - 10
        count_rect = count_surf.get_rect(bottomright = (x, y))
        self.display_surface.blit(count_surf, count_rect)

    def update(self):
        self.cooldowns()
        self.draw_timer()