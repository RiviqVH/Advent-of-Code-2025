### Setup: ###
### Read input: ###
with open('input.txt') as f:
    input = f.read()
    
input_by_line = input.strip().split('\n')

test_input = [
'..@@.@@@@.',
'@@@.@.@.@@',
'@@@@@.@.@@',
'@.@@@@..@.',
'@@.@@@@.@@',
'.@@@@@@@.@',
'.@.@.@.@@@',
'@.@@@.@@@@',
'.@@@@@@@@.',
'@.@.@@@.@.']

# print(input)

# input = test_input
input = input_by_line

input_grid = [list(x) for x in input]
one_away = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def valid_coords(grid, coords):
    y, x = coords
    # print(y, x)
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        # print('invalid')
        return False
    # print('valid')
    return True

def count_adjacent(grid, coords, char = '@'):
    count = 0
    # print(f'Coordinate: {coords}')
    for m in one_away:
        test_coord = tuple(map(lambda i,j: i-j, coords, m))
        if valid_coords(grid, test_coord):
            y, x = test_coord
            # print(f'Considering neighbor: {test_coord}. Value: {grid[y][x]}')
            if grid[y][x] == char: count += 1
    # print(f'Rolls found: {count}')
    return(count)

### Part 1: ###
total = 0
for idxy, y in enumerate(input_grid):
    for idxx, x in enumerate(y):
        if x == '@':
            coords = (idxy, idxx)
            if count_adjacent(input_grid, coords) < 4: total += 1

print(total)

### Part 2: ###

def remove_rolls(grid, count = 0):
    remember = []
    for idxy, y in enumerate(grid):
        for idxx, x in enumerate(y):
            if x == '@':
                coords = (idxy, idxx)
                if count_adjacent(grid, coords) < 4: 
                    remember += [coords]

    for c in remember:
        grid[c[0]][c[1]] = '.'
        
    # print(len(remember), count)
    if len(remember) == 0:
        print('Done!')
        print(count)
    else:
        count += len(remember)
        remove_rolls(grid, count)

remove_rolls(input_grid)