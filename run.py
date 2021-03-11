import sys
import pygame


WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 980

def load_image(image):
    final_image = pygame.image.load(image)
    final_image = pygame.transform.scale(final_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    return final_image

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    background = load_image('resources/spot_the_diff.png')

    screen.blit(background, (0, 0))
    pygame.display.update()

    while True:
        evt = pygame.event.get()
        for event in evt:
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()
