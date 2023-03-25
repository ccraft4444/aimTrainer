from countdown import Countdown
from settings import *
import ctypes, pygame, sys
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

# Maintain resolution regardless of Windows scaling settings
#ctypes.windll.user32.SetProcessDPIAware()

class Game:
    def __init__(self):

        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE_STRING)
        self.clock = pygame.time.Clock()
        self.click_count = 0

        #bg image 
        self.bg_image = pygame.image.load(BG_IMAGE_PATH)

        #create countdown
        self.countdown = Countdown(10)

    def run(self):

        self.start_time = pygame.time.get_ticks()

        while True:
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Time variables
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            pygame.display.update()
            self.clock.tick(FPS)

            #game specific updates
            self.countdown.update()

if __name__ == '__main__':
    game = Game()
    game.run()