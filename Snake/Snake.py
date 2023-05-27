import random

#A pálya mérete
width = 60
height = 30

# A kígyó kezdőhelye és iránya
snake_x = random.randint(2, width - 3)
snake_y = random.randint(2, height - 3)

dx = 1
dy = 0

# A pálya feldolgozása
field = [[' '] * width for _ in range(height)]
snake_parts = [(snake_x, snake_y)]

# Az alma kezdőpozíciója
alma_x = random.randint(1, width - 2)
alma_y = random.randint(1, height - 2)

# A pálya szélei
for i in range(width):
    field[0][i] = '*'
    field[height - 1][i] = '*'
for i in range(height):
    field[i][0] = '*'
    field[i][width - 1] = '*'


# A kígyó megjelenítése a pályán
def draw_snake():
    for i, (x, y) in enumerate(snake_parts):
        field[y][x] = '@'



# Az alma megjelenítése a pályán
def draw_apple():
    field[alma_y][alma_x] = 'O'


# Pálya és péntszám megjelenítése
def draw_field():
    for row in field:
        print(''.join(row))
    print("Pontszám: ", len(snake_parts) - 1)



# Játék működése
while True:
    field = [[' '] * width for _ in range(height)]
    draw_snake()
    draw_apple()

    # Pálya széleinek kirajzolása
    for i in range(width):
        field[0][i] = '*'
        field[height - 1][i] = '*'
    for i in range(height):
        field[i][0] = '*'
        field[i][width - 1] = '*'

    draw_field()

    if snake_parts[-1][0] + dx == -1 or snake_parts[-1][0] + dx == width or \
            snake_parts[-1][1] + dy == -1 or snake_parts[-1][1] + dy == height:
        print("Megérintetted a kerítést!")
        print("Most ennyi volt, szép napot!")
        break

    for i in range(len(snake_parts) - 1):
        snake_parts[i] = snake_parts[i + 1]

    snake_x += dx
    snake_y += dy
    snake_parts[-1] = (snake_x, snake_y)

    # Ellenőrizze, hogy az alma fel van-e véve
    if snake_x == alma_x and snake_y == alma_y:
        new_part_x = snake_parts[-1][0] + dx
        new_part_y = snake_parts[-1][1] + dy

        #A kígyó méretének bővítése
        snake_parts.append((new_part_x, new_part_y))

        #Új alma generálása
        alma_x = random.randint(1, width - 2)
        alma_y = random.randint(1, height - 2)
        draw_snake()

    print("Hova?")

    #Irányítás
    command = input()

    if command == 'balra':
        dx = -1
        dy = 0
    elif command == 'jobbra':
        dx = 1
        dy = 0
    elif command == 'fel':
        dx = 0
        dy = -1
    elif command == 'le':
        dx = 0
        dy = 1
    elif command == 'meguntam':
        print("Most ennyi volt, szép napot!")
        break
