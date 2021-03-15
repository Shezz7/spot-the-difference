import sys
from time import sleep
import pygame


WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 980
LEFT_CLICK = (1, 0, 0)


def load_image(image):
    """
    Load and scale an image to the specified width and height
    """
    final_image = pygame.image.load(image)
    final_image = pygame.transform.scale(final_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    return final_image


def score_msg(screen, score):
    """
    Display the score on the screen
    """
    myfont = pygame.font.Font('resources/font/halloween.ttf', 45)
    myfont.set_bold(1)
    score_text = myfont.render("Score:" + str(score), 1, (200, 200, 200))
    screen.blit(score_text, (0, 900))
    pygame.display.update()


def get_diff():
    """
    Define the points where clicking will increment the score
    """
    diff_list = []
    bat_logo = pygame.Rect(367, 447, 50, 25)
    ugly_nose = pygame.Rect(360, 340, 27, 27)
    cat_whisker = pygame.Rect(50, 535, 20, 28)
    white_candle = pygame.Rect(68, 139, 52, 47)
    potion_label = pygame.Rect(679, 763, 64, 51)
    spider_web = pygame.Rect(0, 0, 43, 38)
    spider_hand = pygame.Rect(662, 122, 41, 55)
    diff_list = [bat_logo, ugly_nose, cat_whisker, white_candle, potion_label, spider_web, spider_hand]
    return diff_list


def zombie_popup(screen):
    """
    Jump scare when the game ends
    """
    scream = pygame.mixer.Sound('resources/audio/scream.wav')
    zombie = load_image('resources/images/scary_face.png')
    scream.play()
    screen.blit(zombie, (0, 0))
    pygame.display.update()
    sleep(2)
    scream.stop()


def main():
    """
    Describe the main thread of execution in an infinite loop
    """
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    background = load_image('resources/images/spot_the_diff.png')
    bgmusic = pygame.mixer.Sound('resources/audio/bgmusic.wav')

    screen.blit(background, (0, 0))
    pygame.display.update()

    score = 0
    score_msg(screen, score)
    # Acquire list of hit points
    diff_list = get_diff()
    # List to store which points have been hit to avoid duplicate scores
    hits = []

    while True:
        bgmusic.play()
        evt = pygame.event.get()
        for event in evt:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == LEFT_CLICK:
                pos = pygame.mouse.get_pos()
                for rect in diff_list:
                    if rect.collidepoint(pos) and rect not in hits:
                        score = score + 1
                        screen.blit(background, (0, 0))
                        score_msg(screen, score)
                        hits.append(rect)
            # Jump scare when game is over
            if score == 7:
                bgmusic.stop()
                zombie_popup(screen)
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
