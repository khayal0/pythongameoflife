import random

height = 50 #100 
width = 50 #100

def randomize(grid, width, height):   # grid - 
    for i in range(0, height):
        for j in range(0, width):
            grid[i][j] = random.randint(0,1)      # randint funksyasi 0 ve ya 1 secir
            
grid_model = [0] * height                       #grid model 100 0 dan ibaret listdi
next_grid_model = [0] * height                  #next_grid_model de 100 0dan ibaret listdi
for i in range(height):                          #yuz defe tekrarla (0 - 99) , 
    grid_model[i] = [0] * width                  # creates a list of lists
    next_grid_model[i] = [0] * width



def next_gen():
    global grid_model, next_grid_model
    
    for i in range(0, height):
        for j in range(0, width):
            cell = 0                            # olu baslayir 0 olu demekdi
            #print('checking cell', i, j)

            count = count_neighbors(grid_model, i, j)
            
            if grid_model[i][j] == 0:
                if count == 3:
                    cell = 1
            elif grid_model[i][j] ==1:
                if count == 2 or count == 3:
                    cell = 1
            next_grid_model[i][j] = cell
            #print("Next grid value is", next_grid_model[i][j])
            
    temp = grid_model
    grid_model = next_grid_model
    next_grid_model = temp

glider_pattern = [[0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]]

glider_gun_pattern =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                     [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def count_neighbors(grid, row, col):               #h elpet function
    count = 0
    if row-1 >= 0:
        count = count + grid[row-1][col]
    if (row-1 >= 0) and (col-1 >= 0):
        count = count + grid[row-1][col-1]
    if (row-1 >= 0) and (col+1 < width):
        count = count + grid[row-1][col+1]
    if col-1 >= 0:
        count = count + grid[row][col-1]
    if col + 1 < width:
        count = count + grid[row][col+1]
    if row + 1 < height:
        count = count + grid[row+1][col]
    if (row + 1 < height) and (col-1 >= 0):
        count = count + grid[row+1][col-1]
    if (row + 1 < height) and (col+1 < width):
        count = count + grid[row+1][col+1]
    return count

def load_pattern(pattern, x_offset=0, y_offset=0):
    global grid_model
    
    for i in range(0, height):
        for j in range(0, width):
            grid_model[i][j] = 0

    j = y_offset
    for row in pattern:
        i = x_offset
        for value in row:
            grid_model[i][j] = value
            i = i + 1
        j = j + 1

if __name__ == '__main__':
    next_gen()
    

