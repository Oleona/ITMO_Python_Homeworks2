import pathlib
import random
import typing as tp
from copy import deepcopy, copy
import numpy
import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
            self,
            size: tp.Tuple[int, int],
            randomize: bool = True,
            max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        # Copy from previous assignment
        self.grid = []
        self.grid = [[0 for x in range(self.cols)] for y in range(self.rows)]
        if randomize:
            self.grid = [[random.randint(0, 1) for x in range(self.cols)] for y in range(self.rows)]

        return self.grid
        pass

    def get_neighbours(self, cell: Cell) -> Cells:
        row = cell[0]
        col = cell[1]
        Cells = []
        for i in range(max(0, row - 1), min(self.rows, row + 2)):
            for j in range(max(0, col - 1), min(self.cols, col + 2)):
                if i == row and j == col:
                    continue
                Cells.append(self.curr_generation[i][j])
        return Cells
        # Copy from previous assignment
        pass

    def get_next_generation(self) -> Grid:
        new_grid = deepcopy(self.grid)
        for y in range(self.rows):
            for x in range(self.cols):
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

        # Copy from previous assignment
        pass

    def step(self) -> None:
        self.prev_generation = deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.generations += 1
        """
        Выполнить один шаг игры.
        """
        pass

    @property
    def is_max_generations_exceeded(self) -> bool:
        return self.generations >= self.max_generations

        pass

    @property
    def is_changing(self) -> bool:
        return self.prev_generation != self.curr_generation

        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        pass

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        input = numpy.loadtxt(filename, delimiter=',' )
        cols = len(input)
        rows = len(input[0])
        game = GameOfLife((cols, rows))

        return game

        """
        Прочитать состояние клеток из указанного файла.
        """
        pass

    def save(self, filename: pathlib.Path) -> None:
        numpy.savetxt(filename, self.curr_generation, delimiter=',', dtype=str)
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass
