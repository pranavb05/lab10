import pygame
import random

rows = 16
columns = 20
SQUARE_SIZE = 32
LINE_WIDTH = 1
HEIGHT = 512
WIDTH = 640
mole_square_x = random.randint(0, rows-1)
mole_square_y = random.randint(0, columns-1)
x = 32 * mole_square_x
y = 32 * mole_square_y
def draw_grid(screen):
    for i in range (columns):
        pygame.draw.line(
            screen,
            'black',
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )
    for i in range (rows):
        pygame.draw.line(
            screen,
            'black',
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )

def new_position():
    global mole_square_x, mole_square_y, x, y
    mole_square_x = random.randint(0, columns-1)
    mole_square_y = random.randint(0, rows-1)
    x = 32 * mole_square_x
    y = 32 * mole_square_y

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                screen.fill("light green")
                draw_grid(screen)
                screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    square_x = event.pos[0]//SQUARE_SIZE
                    square_y = event.pos[1]//SQUARE_SIZE
                    if square_x == mole_square_x and square_y == mole_square_y:
                        new_position()

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()



if __name__ == "__main__":
    main()
