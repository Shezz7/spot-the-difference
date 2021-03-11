import sys
import pygame


WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 980
LEFT_CLICK = (1, 0, 0)

def load_image(image):
    final_image = pygame.image.load(image)
    final_image = pygame.transform.scale(final_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    return final_image


def score_msg(screen, score):
    myfont = pygame.font.SysFont('Arial', 36)
    myfont.set_bold(1)
    scoretext = myfont.render("Score=" + str(score), 1, (200, 200, 200))
    screen.blit(scoretext, (0, 900))
    pygame.display.update()


def get_diff():
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


def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    background = load_image('resources/spot_the_diff.png')

    screen.blit(background, (0, 0))
    pygame.display.update()
    score = 0
    score_msg(screen, score)
    diff_list = get_diff()
    
    while True:
        evt = pygame.event.get()
        for event in evt:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == LEFT_CLICK:
                pos = pygame.mouse.get_pos()
                score = score + 1
                screen.blit(background, (0, 0))
                score_msg(screen, score)


if __name__ == "__main__":
    main()
