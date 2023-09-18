import random
from disjoint_set import DisjointSet
import pygame

WIDTH = 100
HEIGHT = 100


def generate_maze(width, height):
    """Generates a maze of the given width and height."""
    cells = [[False] * width for _ in range(height)]
    disjoint_set = DisjointSet(width * height)

    for i in range(width):
        for j in range(height):
            if i > 0 and not cells[i - 1][j]:
                disjoint_set.union(i * width + j, (i - 1) * width + j)
            if j > 0 and not cells[i][j - 1]:
                disjoint_set.union(i * width + j, i * width + j - 1)

    for _ in range(width * height // 2):
        i = random.randint(0, width - 1)
        j = random.randint(0, height - 1)
        other_cell = disjoint_set.find(i * width + j)
        i2 = other_cell // width
        j2 = other_cell % width
        cells[i][j] = True
        cells[i2][j2] = True
        disjoint_set.union(i * width + j, i2 * width + j2)

    return cells


def main():
    """The main function."""
    cells = generate_maze(WIDTH, HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill((0, 0, 0))
        for i in range(5):
            for j in range(5):
                if cells[i][j]:
                    pygame.draw.rect(screen, (255, 255, 255), (i * 10, j * 10, 10, 10))
        pygame.display.update()


if __name__ == "__main__":
    main()

