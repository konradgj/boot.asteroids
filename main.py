import pygame

from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gClock = pygame.time.Clock()
    dt = 0

    while True:
        screen.fill(pygame.Color(0, 0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = gClock.tick(60) / 1000


if __name__ == "__main__":
    main()
