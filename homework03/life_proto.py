import random
import typing as tp
from copy import deepcopy

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
            self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        self.grid = []
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток
        # PUT YOUR CODE HERE
        self.grid = self.create_grid(randomize=True)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            # PUT YOUR CODE HERE
            self.draw_grid()

            self.get_next_generation()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:

        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """

        self.grid = []
        col = self.cell_width
        row = self.cell_height
        self.grid = [[0 for x in range(col)] for y in range(row)]

        if randomize:
            self.grid = [[random.randint(0, 1) for x in range(col)] for y in range(row)]
            '''self.grid.append(self.grid[col][row])'''
        return self.grid

    pass

    def draw_grid(self) -> None:
        for y in range(self.cell_height):
            for x in range(self.cell_width):
                if self.grid[y][x]:
                    pygame.draw.rect(self.screen, pygame.Color('green'),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                                     (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    pass

    def get_neighbours(self, cell: Cell) -> Cells:
        row = cell[0]
        col = cell[1]
        Cells = []
        for i in range(max(0, row - 1), min(self.cell_height, row + 2)):
            for j in range(max(0, col - 1), min(self.cell_width, col + 2)):
                if i == row and j == col:
                    continue
                Cells.append(self.grid[i][j])
        return Cells

    """
    Вернуть список соседних клеток для клетки `cell`.

    Соседними считаются клетки по горизонтали, вертикали и диагоналям,
    то есть, во всех направлениях.

    Parameters
    ----------
    cell : Cell
        Клетка, для которой необходимо получить список соседей. Клетка
        представлена кортежем, содержащим ее координаты на игровом поле.

    Returns
    ----------
    out : Cells
        Список соседних клеток.
    """

    pass

    def get_next_generation(self) -> Grid:
        new_grid = deepcopy(self.grid)
        for y in range(self.cell_height):
            for x in range(self.cell_width):
                neighbours = self.get_neighbours((y, x))
                if self.grid[y][x]:
                    if sum(neighbours) == 2 or sum(neighbours) == 3:
                        new_grid[y][x] = 1
                    else:
                        new_grid[y][x] = 0
                else:
                    if sum(neighbours) == 3:
                        new_grid[y][x] = 1
                    else:
                        new_grid[y][x] = 0

        self.grid = new_grid
        return self.grid

    """
    Получить следующее поколение клеток.

    Returns
    ----------
    out : Grid
        Новое поколение клеток.
    """

    pass
if __name__ == '__main__':
    game = GameOfLife()
    game.run()