import time

def set_shape(world, shape):
    for y in range(5):
        world[y+5][5:20] = shape[y][:]

def print_world(world):
    for row in world:
        print(" ".join(row))
    print()
    time.sleep(.5)

def check_world(world):
    temp = world[:]
    for y in range(15):
        temp[y] = world[y][:]
        for x in range(15):
            n = neighbors(world, x, y)
            if n < 2 or n > 3:
                temp[y][x] = "."
            elif n == 3:
                temp[y][x] = "o"
    return temp
def neighbors(world, x, y):
    n = 0 
    for i in range(y-1, y+2):
        if i < 0 or i >= 15: continue 
        for j in range(x-1, x+2):
            if j < 0 or j >= 15: continue 
            if i == y and j == x: continue
            if world[i][j] == 'o':
                n += 1
    return n