# 
from settings import *
from countdown import Countdown
import ctypes, sys, pygame
from title import TitleScreen

# import os
# os.environ['SDL_AUDIODRIVER'] = 'dsp'
# os.environ["SDL_VIDEODRIVER"] = "dummy"

# Maintain resolution regardless of Windows scaling settings
ctypes.windll.user32.SetProcessDPIAware()

class Game:
    def __init__(self):

        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE_STRING)
        self.clock = pygame.time.Clock()
        self.click_count = 0
        self.game_state = "waiting"

        #bg image 
        self.bg_image = pygame.image.load(BG_IMAGE_PATH)

        #create countdown
        
        self.title = TitleScreen()


    def run(self):
        while True:
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and self.game_state == "waiting":
                    if event.key == pygame.K_SPACE:
                        self.countdown = Countdown(10)
                        self.game_state = "playing"    

            pygame.display.update()
            self.screen.blit(self.bg_image, (0,0))
            self.clock.tick(FPS)

            #game specific updates
            if self.game_state == "waiting":
                self.title.update()
            elif self.game_state == "playing":
                self.countdown.update()

if __name__ == '__main__':
    game = Game()
    game.run()