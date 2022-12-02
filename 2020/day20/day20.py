import sys
import re
import math
import numpy as np


def get_lines_from_file():
    with open(sys.argv[1]) as inf:
        return inf.readlines()

lines = [line.rstrip() for line in get_lines_from_file()]

parsing_tile_id = 0
temp_all_tiles = {}
for line in lines:
    if "Tile" in line:
        print(line)
        tile_id = int(re.match(r'Tile (\d+)', line)[1])
        print(tile_id)
        parsing_tile_id = tile_id
        temp_all_tiles[parsing_tile_id] = []
    elif line == "":
        print("Empty")
    else:
        print(line)
        temp_all_tiles[parsing_tile_id].append(line)
print(100*"-")
print(temp_all_tiles[2311])


class Tile:
    def __init__(self, top, right, bot, left):
        self.top_connector = top
        self.right_connector = right
        self.bot_connector = bot
        self.left_connector = left

        self.all_connectors = [top[0], top[1], right[0], right[1], bot[0], bot[1], left[0], left[1]]

        self.possible_connecting_tiles = []


right = -1
left = 0

def side_to_int(side):
    side = side.replace('.', '0')
    side = side.replace('#', '1')
    connector = int(side, 2)
    print(side)

    side = side[::-1]
    revese_connector = int(side, 2)
    print(connector, revese_connector)
    return (connector, revese_connector)

def get_side(tile, side):
    right = ''
    for row in tile:
        right += row[side]
    if side == left:
        return right[::-1]
    return right


all_tiles = {}
bild = [[]]

for tile_id in temp_all_tiles:
    print(tile_id)
    current_tile = temp_all_tiles[tile_id]
    top_side = current_tile[0]
    print(top_side)

    left_side = get_side(current_tile, left)
    right_side = get_side(current_tile, right)
    print(left_side)
    bot_side = current_tile[-1][::-1]
    print(right_side)

    

    top_con = side_to_int(top_side)
    right_con = side_to_int(right_side)
    
    left_con = side_to_int(left_side)
    bot_con = side_to_int(bot_side)

    tile = Tile(top_con, right_con, bot_con, left_con)
    all_tiles[tile_id] = tile
    
    

print(90*"#")
for tile_id in all_tiles:
    print(tile_id)
    tile = all_tiles[tile_id]
    current_tile_set = set(tile.all_connectors)
    for comp_tile_id in all_tiles:
        if comp_tile_id == tile_id:
            continue
        comp_tile = all_tiles[comp_tile_id]
        comp_tile_set = set(comp_tile.all_connectors)
        num_intersections = len(current_tile_set.intersection(comp_tile_set))
        if num_intersections:
            tile.possible_connecting_tiles.append(comp_tile_id)
            
    #print(all_tiles[tile_id].all_connectors)
print(90*"#")

corner_tiles = []
ans = 1
for tile_id in all_tiles:
    tile = all_tiles[tile_id]
    if len(tile.possible_connecting_tiles) == 2:
        corner_tiles.append(tile_id)
        ans *= tile_id


print(ans)


dim = int(math.sqrt(len(all_tiles)))
print(dim)

placed_tiles = {}

top_left_corner = corner_tiles[0]

def get_tile_to_place(tile_id):
    print("Place tile", tile_id)
    tile = all_tiles[tile_id]
    print(all_tiles[tile_id].possible_connecting_tiles)

    min_con = 99
    min_con_id = -1

    for con_tile_id in tile.possible_connecting_tiles:
        num_con = len(all_tiles[con_tile_id].possible_connecting_tiles)
        if num_con < min_con:
            min_con_id = con_tile_id
            min_con = num_con
    print("Tile to place")
    print(min_con_id, min_con)


global_row = 0
global_col = 0
num_placed_tiles = 0
current_pos = (0, 0)

def place_tile(tile_id):
    global num_placed_tiles

    num_placed_tiles += 1
    placed_tiles[(global_row, global_col)] = tile_id

    for neigh_tile_id in all_tiles:
        psbl_conn = all_tiles[neigh_tile_id].possible_connecting_tiles
        if tile_id in psbl_conn:
            psbl_conn.remove(tile_id)

    # Remove it as possible neighbor form all other tiles


place_tile(corner_tiles[0])
get_tile_to_place(top_left_corner)


print(50*"#")
for tile_id in all_tiles:
    tile = all_tiles[tile_id]
    print(tile_id)
    print(tile.possible_connecting_tiles)

print(placed_tiles)

def get_flipped(image):
    flipped_img = []
    
    for line in image:
        flipped_img.append(line[::-1])
    return flipped_img

def print_image(image):
    for line in image:
        print(line)

print("Image 1951")
print_image(temp_all_tiles[1951])

flipped = get_flipped(temp_all_tiles[1951])
print("Flipped")
#print_image(flipped)

fl = np.asarray(flipped)

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

rot90 = rotated(temp_all_tiles[1951])
print_image(rot90)

print("180")
rot180 = rotated(rot90)
print_image(rot180)