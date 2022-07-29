import pygame.locals as pl
from os.path import exists
from copy import deepcopy
import pygame as p


_events = None

COLORS = {'WHITE': (255, 255, 255), 'BLACK': (0, 0, 0), 'CYAN': (0, 255, 255),
          'GREEN': (0, 255, 0), 'BLUE': (0, 0, 255), 'YELLOW': (255, 255, 0),
          'ORANGE': (255, 165, 0), 'MAGENTA': (255, 0, 255),
          'SILVER': (192, 192, 192), 'PURPLE': (128, 0, 128),
          'TEAL': (0, 128, 128), 'GRAY': (128, 128, 128), 'RED': (255, 0, 0),
          'BROWN': (165, 42, 42), 'GOLDEN': (255, 215, 0)}


def setEvents():
    global _events

    _events = p.event.get()

    return _events


class System(object):
    """Esta clase representa un sistema en el que..."""

    def __init__(self, matrix, colors={0: 'BLACK'}, name='system', nullCell=0,
                 clear=True, export=True, add=True):
        """matrix: tablero, lo que se muestra en pantalla
           colors: diccionario con los colores para cada numero en matrix
           name: nombre del sistema
           nullCell: numero de celda con la que se limpia el tablero
           clear: si se desea la funcion clear activa
           export: si se desea la funcion export activa
           add: si se desea la funcion add activa"""
        self.width = len(matrix[0])
        self.height = len(matrix)
        self.nullCell = nullCell
        self.colors = colors
        self.matrix = matrix
        self.name = name
        self.event = {'keyDown': [], 'keyUp': [], 'mouseButtonDown': [],
                      'mouseButtonUp': []}
        if clear:
            self.event['keyDown'].append(self.clear)
        if export:
            self.event['keyDown'].append(self.export)
        if add:
            self.event['mouseButtonDown'].append(self.add)

    def getMatrixFromFile(cls, filename):
        matrix = []

        with open(filename, 'r') as fichero:
            for line in fichero:
                matrix.append(list(map(int, line.replace('\n', ''))))

        return matrix

    def getColor(self, i, j):
        return self.colors.get(self.matrix[i][j], 'BLACK')

    def getCaption(self):
        return self.name

    def getName(self, extension='png'):
        number = 0
        while True:
            name = self.name + str(number) + '.' + extension
            if not exists(name):
                return name
            number += 1

    def clear(self, key, matrix=None):
        """limpia el tablero"""
        if key == 'c':
            if not matrix:
                self.matrix = deepcopy(matrix)
            else:
                self.matrix = [[self.nullCell] *
                               self.width for i in range(self.height)]

    def export(self, key, matrix=None):
        """exporta el tablero a un archivo txt"""
        if key == 'e':
            if not matrix:
                matrix = self.matrix

            with open(self.getName('txt'), 'w') as file:
                for line in matrix:
                    file.write(''.join(list(map(str, line))) + '\n')
            print('Text saved')

    # esta funcion debe ser modificada
    def add(self, pos, _, matrix=None, increase=1, base=2):
        """agrega celulas al tablero"""
        if not matrix:
            matrix = self.matrix

        if 0 <= pos[0] < self.width and 0 <= pos[1] < self.height:
            matrix[pos[1]][pos[0]] += increase
            matrix[pos[1]][pos[0]] %= base

    def mouseButtonDown(self, pos, event):
        for function in self.event['mouseButtonDown']:
            function(pos, event)

    def mouseButtonUp(self, pos, event):
        for function in self.event['mouseButtonUp']:
            function(pos, event)

    def keyDown(self, key):
        for function in self.event['keyDown']:
            function(key)

    def keyUp(self, key):
        for function in self.event['keyUp']:
            function(key)

    def update(self):
        """Se debe implementar en las clases que heredan"""
        pass


class CellGraph(object):
    """docstring for CellGraph"""

    def __init__(self, system, margin_width=0, margin_height=0,
                 background_color='BLACK', cellwidth=5, cellheight=5, fps=60,
                 separation_between_cells=1):
        self.separation_between_cells = separation_between_cells
        self.background_color = COLORS[background_color]
        self.margin_height = margin_height
        self.margin_width = margin_width
        self.cellheight = cellheight
        self.cellwidth = cellwidth
        self.system = system
        self.fps = fps

        self.age = 0

        self.width = 2 * margin_width + cellwidth * system.width + \
            separation_between_cells * (system.width - 1)
        self.height = 2 * margin_height + cellheight * system.height + \
            separation_between_cells * (system.height - 1)

    def getPositionInMatrix(self, pos):
        posx = pos[0] - self.margin_height
        posy = pos[1] - self.margin_width
        posx = posx / (self.cellwidth + self.separation_between_cells)
        posy = posy / (self.cellheight + self.separation_between_cells)
        return int(posx), int(posy)

    def draw(self, screen):
        screen.fill(self.background_color)
        for i in range(self.system.height):
            for j in range(self.system.width):
                p.draw.rect(screen, COLORS[self.system.getColor(i, j)],
                            p.Rect(self.margin_width + j * self.cellwidth +
                                   (j * self.separation_between_cells),
                                   self.margin_height + i * self.cellheight +
                                   (i * self.separation_between_cells),
                                   self.cellwidth, self.cellheight))

    def reload(self, screen):
        self.draw(screen)
        p.display.set_caption(self.system.getCaption())
        p.display.update()

    def eventManager(self, screen):
        quit = False
        pause = False

        for event in setEvents():
            if event.type == p.QUIT:
                quit = True
                break
            if event.type == p.KEYDOWN:
                if event.key == pl.K_p or event.key == pl.K_SPACE:
                    pause = True
                if event.key == pl.K_q:
                    quit = True
                    break
                if event.key == pl.K_s:
                    p.image.save(screen, self.system.getName())
                    print('Saved image')
                self.system.keyDown(p.key.name(event.key))
                self.reload(screen)
            if event.type == p.MOUSEBUTTONDOWN:
                self.system.mouseButtonDown(
                    self.getPositionInMatrix(event.pos), event)
                self.reload(screen)
            if event.type == p.KEYUP:
                self.system.keyUp(p.key.name(event.key))
                self.reload(screen)
            if event.type == p.MOUSEBUTTONUP:
                self.system.mouseButtonUp(
                    self.getPositionInMatrix(event.pos), event)
                self.reload(screen)

        return quit, pause

    def run(self, manual=False, acceleration=0):
        p.display.init()

        screen = p.display.set_mode((self.width, self.height))
        p.display.set_caption(self.system.getCaption())

        clock = p.time.Clock()

        quit = False
        pause = False

        self.reload(screen)

        while not quit and not manual:
            clock.tick(self.fps + acceleration * self.age)

            quit, temp = self.eventManager(screen)

            if temp:
                pause = not pause

            if not pause and not quit:
                self.system.update()
                self.reload(screen)

            self.age += 1

        while not quit and manual:
            clock.tick(20)

            quit, pause = self.eventManager(screen)
            pause = not pause

            if p.key.get_pressed()[pl.K_SPACE]:
                pause = False

            if not pause and not quit:
                pause = True
                self.system.update()
                self.reload(screen)

            self.age += 1


def test():
    pass


if __name__ == '__main__':
    test()
