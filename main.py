from argparse import ArgumentParser, RawDescriptionHelpFormatter

from snake.cellgraph import CellGraph, COLORS
from snake.snake import Snake


def execute(args):
    colors = {0: args.color_cell, 1: args.color_snake, 2: args.color_food}

    snake = Snake(args.width, args.height, colors, food=args.food,
                  filename=args.filename)

    game = CellGraph(snake, margin_width=args.margin_width,
                     margin_height=args.margin_height,
                     cellwidth=args.cell_width, cellheight=args.cell_height,
                     separation_between_cells=args.sbc,
                     background_color=args.background_color,
                     fps=args.velocity)

    game.run(acceleration=args.acceleration)


def main():
    epilog = ''' Clasico juego Snake.

El programa permite cargar un mapa desde un archivo de texto(donde 0
representa que no hay nada en la celda y 3 representa un obstaculo), ademas se
pueden agregar obstaculos en celda deseada haciendo click con el mouse.
Mediante la pulsacion de la tecla SPACE o p se puede pausar el juego, ademas se
puede tomar una captura de pantalla con la tecla s, y si se presiona la
tecla e la configuracion del tablero se guarda en un archivo de texto.


Los colores disponibles son:
    - WHITE
    - BLACK
    - CYAN
    - GREEN
    - BLUE
    - YELLOW
    - ORANGE
    - MAGENTA
    - SILVER
    - PURPLE
    - TEAL
    - GRAY
    - RED
    - BROWN
    - GOLDEN'''

    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                            epilog=epilog)

    parser.add_argument('--filename', default=None,
                        help='''Archivo con la configuracion
                        inicial del tablero''')
    parser.add_argument('-o', '--output', default='gameoflife',
                        dest='name', help='''nombre con el que se guarda la
                        captura de pantalla(si se hace)''')
    parser.add_argument('-w', '--width', type=int, default=30,
                        help='numero de celdas horizontales')
    parser.add_argument('--height', type=int, default=30,
                        help='numero de celdas verticales')
    parser.add_argument('-mw', '--margin-width', type=int, default=0,
                        help='largo de la margen horizontal')
    parser.add_argument('-mh', '--margin-height', type=int, default=0,
                        help='largo de la margen vertical')
    parser.add_argument('-cw', '--cell-width', type=int, default=5,
                        help='ancho horizontal de las celdas')
    parser.add_argument('-ch', '--cell-height', type=int, default=5,
                        help='ancho vertical de las celdas')
    parser.add_argument('-sbc', '--separation-between-cells', type=int,
                        default=1, dest='sbc',
                        help='separacion entre las celdas')
    parser.add_argument('-f', '--food', type=int, default=1,
                        help='cantidad de comida en el tablero')
    parser.add_argument('-bc', '--background-color', type=lambda x: x.upper(),
                        metavar='COLOR', default='BLACK',
                        choices=COLORS.keys(),
                        help='''color de fondo, es el mismo que el de la
                        margen y la separacion entre celdas''')
    parser.add_argument('-cf', '--color-food', type=lambda x: x.upper(),
                        metavar='COLOR', default='GREEN',
                        choices=COLORS.keys(),
                        help='color de la comida')
    parser.add_argument('-cs', '--color-snake', type=lambda x: x.upper(),
                        metavar='COLOR', default='RED',
                        choices=COLORS.keys(),
                        help='color de la culebrita')
    parser.add_argument('-cc', '--color-cell', type=lambda x: x.upper(),
                        metavar='COLOR', default='WHITE',
                        choices=COLORS.keys(),
                        help='color de las celdas vacias')
    parser.add_argument('-v', '--velocity', type=int,
                        default=10, help='''velocidad de la culebrita''')
    parser.add_argument('-a', '--acceleration', type=float,
                        default=0, help='''aceleracion de la culebrita''')

    args = parser.parse_args()
    execute(args)


if __name__ == '__main__':
    main()
