# Snake

El programa permite cargar un mapa desde un archivo de texto(donde 0
representa que no hay nada en la celda y 3 representa un obstaculo), ademas se
pueden agregar obstaculos en celda deseada haciendo click con el mouse.
Mediante la pulsacion de la tecla SPACE o p se puede pausar el juego, ademas se
puede tomar una captura de pantalla con la tecla s, y si se presiona la
tecla e la configuracion del tablero se guarda en un archivo de texto.


usage:

      snake.py [-h] [--filename FILENAME] [-o NAME] [-w WIDTH]
                      [--height HEIGHT] [-mw MARGIN_WIDTH] [-mh MARGIN_HEIGHT]
                      [-cw CELL_WIDTH] [-ch CELL_HEIGHT] [-sbc SBC] [-f FOOD]
                      [-bc COLOR] [-cf COLOR] [-cs COLOR] [-cc COLOR] [-v VELOCITY]
                      [-a ACCELERATION]

optional arguments:

      -h, --help            show this help message and exit
      --filename FILENAME   Archivo con la configuracion inicial del tablero
      -o NAME, --output NAME
                            nombre con el que se guarda la captura de pantalla(si
                            se hace)
      -w WIDTH, --width WIDTH
                            numero de celdas horizontales
      --height HEIGHT       numero de celdas verticales
      -mw MARGIN_WIDTH, --margin-width MARGIN_WIDTH
                            largo de la margen horizontal
      -mh MARGIN_HEIGHT, --margin-height MARGIN_HEIGHT
                            largo de la margen vertical
      -cw CELL_WIDTH, --cell-width CELL_WIDTH
                            ancho horizontal de las celdas
      -ch CELL_HEIGHT, --cell-height CELL_HEIGHT
                            ancho vertical de las celdas
      -sbc SBC, --separation-between-cells SBC
                            separacion entre las celdas
      -f FOOD, --food FOOD  cantidad de comida en el tablero
      -bc COLOR, --background-color COLOR
                            color de fondo, es el mismo que el de la margen y la
                            separacion entre celdas
      -cf COLOR, --color-food COLOR
                            color de la comida
      -cs COLOR, --color-snake COLOR
                            color de la culebrita
      -cc COLOR, --color-cell COLOR
                            color de las celdas vacias
      -v VELOCITY, --velocity VELOCITY
                            velocidad de la culebrita
      -a ACCELERATION, --acceleration ACCELERATION
                            aceleracion de la culebrita


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
      - GOLDEN


## Ejemplos
python snake.py --color-food GOLDEN --cell-width 20 --cell-height 20 --width 20 --height 20 -mw 30 -mh 30


![](https://github.com/Luispapiernik/Divertimentos/blob/master/Snake/Snake0.png)



python snake.py --color-food GOLDEN --cell-width 20 --cell-height 20 --width 20 --height 20 -mw 30 -mh 30 --filename map.txt


![prueba](https://github.com/Luispapiernik/Divertimentos/blob/master/Snake/Snake1.png)
