'''
init_state() - mandatory call; init the states of each cell
init_mapgrid() - mandatory call; init the mapping 2D cell to linear using dictionary
class Grid - mandatory object call; it init the display coordinates of grid
'''

import time
import pygame
# import only class grid
import Grid

pygame.init()
# window size
width = 600
height = 600
G = Grid._Grid(width, height)  # constructor init and set height and width

# make window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")  # caption
# draw grids
for x in G.grid:
    pygame.draw.line(window, (255, 255, 255), x[0], x[1])

# Init game sign
# Player 1: X; sign = 1
# Player 2: O; sign = 0
sign = 1

# Init all vital components
Grid.init_state()
Grid.init_mapgrid()
Grid.init_cellno2centre(width, height)
Grid.init_cellno2leftcorner(width, height)

naught = pygame.image.load('ttt_naught.png')
naught = pygame.transform.scale(naught, (160, 160))
def draw_naught(coor):
    x, y = coor[0], coor[1]
    '''pygame.draw.circle(window, (255, 0, 0), Grid.get_cell_centre(Cell_pos[0]), 80)
    pygame.draw.circle(window, (0, 0, 0), Grid.get_cell_centre(Cell_pos[0]), 70)'''
    window.blit(naught, (x,y))

cross = pygame.image.load('ttt_cross.png')
cross = pygame.transform.scale(cross, (160,160))
def draw_cross(coor):
    x, y = coor[0], coor[1]
    window.blit(cross,(x, y))

def draw_strike(list_coor):
    start_point = list_coor[0]
    end_point = list_coor[1]
    pygame.draw.line(window, (100,100,100), start_point, end_point, 20)

def display_result(sign = -1):
    font = pygame.font.Font('freesansbold.ttf', 50)

    if sign == -1:
        text = font.render("DRAW", True, (0,150,0))
        window.blit(text,(30*width//100, 30*height//100))
    elif sign == 0:                  # when sign 1 (Player 1) wins, in next step sign becomes 0
        text = font.render("PLAYER1 WON", True, (0, 200, 0))
        window.blit(text, (30 * width // 100, 30 * height // 100))
    else:                            # when sign 0 (Player 2) wins, in next step sign becomes 1
        text = font.render("PLAYER2 WON", True, (0, 200, 0))
        window.blit(text, (30 * width // 100, 30 * height // 100))

# Game Loop
win = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pressed()  # which mouse button is pressed
            if click[0] == 1:  # (1,0,0) for left click
                Click_pos = pygame.mouse.get_pos()  # get pixel coordinates
                Cell_pos = [(Click_pos[0]//(width//3), Click_pos[1]//(height//3))]  # get cell coordinates
                print(Cell_pos[0])
                result = Grid.update_grid(Cell_pos[0], sign)  # if True: then update really took place
                if result == True:                            # changes Player
                    if sign == 1:
                        draw_cross(Grid.get_cell_left_corner(Cell_pos[0]))
                    else:
                        draw_naught(Grid.get_cell_left_corner(Cell_pos[0]))
                    sign = (sign+1) % 2

                # to check for DRAW MATCH ie not match but all cells exhausted
                if Grid.check_game_over() == True and Grid.check_match() == False:
                    running = False
                # to check for match
                if Grid.check_match() == True:
                    strike_list = Grid.get_strike()
                    draw_strike(strike_list)
                    running = False
                    win = True
    pygame.display.update()

pygame.time.wait(500)
pygame.quit()

pygame.init()
window = pygame.display.set_mode((width, height))

if win == True:
    display_result(sign)
else:
    display_result()
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()