import random


###
# Constants
###

DEAD = 0
ALIVE = 1


###
# Class
###

class GameOfLife():

    ###
    # Special Methods
    ###

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__garden = self.__generate_garden()    


    ###
    # Private (Util) Methods
    ###

    # Create new, random 2d garden array
    def __generate_garden(self):
        return [[random.randint(0,1) for i in range(self.__width)] for j in range(self.__height)]

    # 0 -> '.'
    # 1 -> '*'
    def __int_to_ascii(self, i):
        return '*' if (i == 1) else '.'

    # Range of neighbor indices (row or column)
    def __neighbor_range(self, cur, size):
        return range(max(cur-1, 0), min(cur+2, size))

    # Count how many living neighbors for a position garden[cur_i, cur_j]
    def __count_living_neighbors(self, cur_i, cur_j):
        living_count = 0

        for i in self.__neighbor_range(cur_i, self.__height):
            for j in self.__neighbor_range(cur_j, self.__width):
                # garden[cur_i, cur_j] is not a neighbor of itself
                if (i == cur_i and j == cur_j):
                    continue

                if (self.__garden[i][j] is ALIVE):
                    living_count += 1

        return living_count

    # Figure out if a single cell should be Alive or Dead in next generation
    def __next_gen_cell(self, i, j):
        cur = self.__garden[i][j]
        num_living_neighbors = self.__count_living_neighbors(i, j)

        # STAY ALIVE -if- Alive and 2/3 alive neighbors
        if (cur is ALIVE and num_living_neighbors in (2,3)):
            return ALIVE

        # REPRODUCE -if- Dead and 3 alive neighbors
        elif (cur is DEAD and num_living_neighbors == 3):
            return ALIVE

        # -else- DIE/STAY DEAD
        return DEAD


    ###
    # Public (API) Methods
    ###

    # Replace active garden with new garden of next gen cells
    def pass_time(self):
        self.__garden = [[self.__next_gen_cell(i,j) for j in range(self.__width)] for i in range(self.__height)]

    # Get ascii text representation of active garden
    def get_garden_as_text(self):
        garden_text = ""
        for row in self.__garden:
            garden_text += " ".join(self.__int_to_ascii(item) for item in row) + "\n"
        return garden_text

    # Replace garden with new random generated garden
    def reset_garden(self):
        self.__garden = self.__generate_garden()
