"""
EXAMPLE:
    class MyClass:
    name = "No Name"
    def __init__(self):
        Grid.name = "Sayan"
    def display(self):
        print(Grid.name)
g = Grid()
g.display() """
##########################################################
'''
init_state() - mandatory call; init the states of each cell
init_mapgrid() - mandatory call; init the mapping 2D cell to linear using dictionary
class Grid - mandatory object call; it init the display coordinates of grid
get_key(pos) - it gives the key of search cell_coordinate from mapGrid dictionary
update_grid(cell_pos, sign) - it updates state of grid, more specific cell_coordinates
 
'''
##########################################################
w, h = 600, 600
##########################################################
state = []

def init_state():
    for i in range(9):
        state.append((0, -1))

##########################################################
mapgrid = {}

def init_mapgrid():
    index = 0
    for i in range(3):
        for j in range(3):
            mapgrid[index] = (i, j)
            index += 1
###########################################################

def check_game_over():
    for x in state:
        if x[0] != 1:
            return False
    return True
###########################################################

def check_match():
    global strike
    match = 0
    ver_cell_index = [0,3,6]
    hor_cell_index = [0,1,2]
    diag_cell_index = [0, 2]
    for i in ver_cell_index:
        if state[i] == state[i+1] and state[i+1] == state[i+2] and state[i][1] != -1 and state[i+1][1] != -1 and state[i+2][1] != -1:
            if i == 0:
                x = w//6
            elif i == 3:
                x = 3*w//6
            else:
                x = 5*w//6
            strike = [(x, 5 * h // 100), (x, 95 * h // 100)]
            match = 1
    for i in hor_cell_index:
        if state[i] == state[i+3] and state[i+3] == state[i+6] and state[i][1] != -1 and state[i+3][1] != -1 and state[i+6][1] != -1:
            if i == 0:
                y = h//6
            elif i == 1:
                y = 3*h//6
            else:
                y = 5*h//6
            strike = [(5*w//100,y),(95*w//100,y)]
            match = 1
    for i in diag_cell_index:
        if i == 0:  # direction: cell 0 to cell 8 (top left to bottom right)
            if state[i] == state[i+4] and state[i+4] == state[i+8] and state[i][1] != -1 and state[i+4][1] != -1 and state[i+8][1] != -1:
                x1,y1,x2,y2 = 5*w//100, 5*h//100, 95*w//100, 95*h//100
                strike = [(x1,y1), (x2,y2)]
                match = 1
        else:       # direction: cell 2 to cell 6 (bottom left to top right)
            if state[i] == state[i+2] and state[i+2] == state[i+4] and state[i][1] != -1 and state[i+2][1] != -1 and state[i+4][1] != -1:
                x1, y1, x2, y2 = 5*w //100, 95*h//100, 95*w//100, 5*h//100
                strike = [(x1, y1), (x2, y2)]
                match = 1

    if match == 1:
        return True
    else:
        return False
###########################################################


###########################################################
class _Grid:
    grid = []
    def __init__(self, width, height):
        self.grid = [((0,height//3),(width,height//3)),
                     ((0,2*height//3),(width,2*height//3)),
                     ((width//3,0),(width//3,height)),
                     ((2*width//3,0),(2*width//3,height))]

###################################################################
def get_key(pos):
    for key, value in mapgrid.items():
        if value == pos:
            return key

##################################################################
def update_grid(cell_pos, sign):  # here cell_pos is tuple (,)
    i = get_key(cell_pos)
    if state[i][0] == 1:
        return False
    else:
        state[i] = (1, sign)
        print(state)
        return True

#########################################################################
mapcellno2centre = {}
def init_cellno2centre(width, height):
    cell_width = width // 3
    cell_height = height // 3
    initial_centre = (cell_width//2, cell_height//2)
    h_offset = 0
    for i in range(9):
        if i < 3:
            mapcellno2centre[i] = (initial_centre[0] + 0*cell_width, initial_centre[1] + h_offset*cell_height)
        if i >= 3 and i < 6:
            mapcellno2centre[i] = (initial_centre[0] + 1*cell_width, initial_centre[1] + h_offset*cell_height)
        if i >= 6 and i < 9:
            mapcellno2centre[i] = (initial_centre[0] + 2*cell_width, initial_centre[1] + h_offset*cell_height)
        h_offset = (h_offset+1) % 3
#############################################################################################################

def get_cell_centre(coor):
    i = get_key(coor)
    print(mapcellno2centre[i])
    return mapcellno2centre[i]

#############################################################################################################
mapcellno2leftcorner = {}
def init_cellno2leftcorner(width, height):
    cell_width = width // 3
    cell_height = height // 3
    x_offset = 10
    y_offset = 10
    initial_corner = (x_offset, y_offset)
    h_offset = 0
    for i in range(9):
        if i < 3:
            mapcellno2leftcorner[i] = (initial_corner[0] + 0*cell_width, initial_corner[1] + h_offset*cell_height)
        if i >= 3 and i < 6:
            mapcellno2leftcorner[i] = (initial_corner[0] + 1*cell_width, initial_corner[1] + h_offset*cell_height)
        if i >= 6 and i < 9:
            mapcellno2leftcorner[i] = (initial_corner[0] + 2*cell_width, initial_corner[1] + h_offset*cell_height)
        h_offset = (h_offset+1) % 3
####################################################################################################################

def get_cell_left_corner(coor):
    i = get_key(coor)
    return mapcellno2leftcorner[i]
###############################################################################################################
strike = []
def get_strike():
    return strike