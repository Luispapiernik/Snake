from collections import deque
from random import randint
from copy import deepcopy

from snake.cellgraph import System


DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]


class Snake(System):
    """1: snake, 2: food, 3: wall"""

    def __init__(self, width, height, colors, food=1, filename=None, add=True):
        if filename:
            matrix = self.getMatrixFromFile(filename)
        else:
            matrix = [[0] * width for i in range(height)]

        self.baseMatrix = matrix

        super(Snake, self).__init__(matrix, colors=colors, name='Snake',
                                    clear=False, export=True, add=add)

        self.event['keyDown'].append(self.__keyDown)
        self.gameover = False
        self.pause = False

        self.size = self.height, self.width
        self.dir = (0, 0)
        self.pos = deque([(randint(0, self.height - 1),
                           randint(0, self.width - 1))])
        self.food = deque([])

        for i in range(food):
            self.getFood()

    def getCaption(self):
        if self.gameover:
            return 'Game Over ' + str(len(self.pos))
        return 'Snake ' + str(len(self.pos))

    def getColor(self, i, j):
        key = self.matrix[i][j] or self.baseMatrix[i][j]
        return self.colors.get(key, 'BLACK')

    def add(self, pos, _):
        """agrega celulas al tablero"""
        super(Snake, self).add(pos, _, self.baseMatrix, 3, 6)

    def collide(self, pos=None, wall=False, direction=None):
        direction = direction or self.dir
        posy = (self.pos[0][0] + direction[0]) % self.size[0]
        posx = (self.pos[0][1] + direction[1]) % self.size[1]

        if wall:
            return self.baseMatrix[posy][posx] == 3

        for i, j in pos:
            if i == posy and j == posx:
                return True

        return False

    def __keyDown(self, key):
        if key == 'r':
            self.dir = (0, 0)
            self.pos = deque([(randint(0, self.height - 1),
                               randint(0, self.width - 1))])
        if key == 'p' or key == 'space':
            self.pause = not self.pause
        if not self.pause and not self.gameover:
            if (key == 'up' and not
                    self.collide([self.pos[int(len(self.pos) > 1)]],
                                 direction=DIRECTIONS[1])):
                self.dir = DIRECTIONS[1]
            elif (key == 'down' and not
                    self.collide([self.pos[int(len(self.pos) > 1)]],
                                 direction=DIRECTIONS[0])):
                self.dir = DIRECTIONS[0]
            elif (key == 'right' and not
                    self.collide([self.pos[int(len(self.pos) > 1)]],
                                 direction=DIRECTIONS[3])):
                self.dir = DIRECTIONS[3]
            elif (key == 'left' and not
                    self.collide([self.pos[int(len(self.pos) > 1)]],
                                 direction=DIRECTIONS[2])):
                self.dir = DIRECTIONS[2]
            else:  # solo por simetria
                pass

    def getFood(self):
        posy = randint(0, self.height - 1)
        posx = randint(0, self.width - 1)

        while self.matrix[posy][posx] != 0:
            posy = randint(0, self.height - 1)
            posx = randint(0, self.width - 1)

        self.food.append((posy, posx))

    def move(self, grow=False):
        posy = (self.pos[0][0] + self.dir[0]) % self.size[0]
        posx = (self.pos[0][1] + self.dir[1]) % self.size[1]

        self.pos.appendleft((posy, posx))

        if grow:
            self.food.remove((posy, posx))
            self.getFood()
        else:
            self.pos.pop()

    def update(self):
        self.gameover = self.collide(wall=True) or (
            self.collide(self.pos) and len(self.pos) != 1)

        if not self.pause and not self.gameover:
            self.move(self.collide(self.food))
            self.matrix = deepcopy(self.baseMatrix)

            for i, j in self.food:
                self.matrix[i][j] = 2

            for i, j in self.pos:
                self.matrix[i][j] = 1
