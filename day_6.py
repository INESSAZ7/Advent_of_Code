directions = {
    '<': (0, -1),
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
}
turn_right = {"^": ">", ">": "v", "v": "<", "<": "^"}

def _is_in(nx, ny, rows, cols):
    return 0 <= nx < rows and 0 <= ny < cols 
    
def _is_obstacle(array, nx, ny):
    return array[nx][ny] == "#"

def _find_start_position(array, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if array[i][j] in directions:
                direction = array[i][j]
                return (i,j,direction)

def guard_mapped_area(array):
    array = [list(row) for row in array]
    rows, cols = len(array), len(array[0])
    set_area = set() #add visited position on map

    x, y, direction = _find_start_position(array, rows, cols)
    rows, cols = len(array), len(array[0])

    set_area.add((x,y))    
    
    while True:
        dx, dy = directions[direction]
        nx, ny = x+dx, y+dy
        if not _is_in(nx, ny, rows, cols):
            break
        if _is_obstacle(array, nx, ny):
            direction = turn_right[direction]
        else:
            x, y = nx, ny
            array[x][y] = "X"
            set_area.add((x,y))                
    return len(set_area)


def _simulator(array, rows, cols, x, y, direction)->bool:
    set_visited = set() #add visited position on map
    set_visited.add((x, y, direction)) 
    
    while True:
        dx, dy = directions[direction]
        nx, ny = x+dx, y+dy
        if not _is_in(nx, ny,  rows, cols):
            return False
        if _is_obstacle(array, nx, ny):
            direction = turn_right[direction]
        else:
            x, y = nx, ny
            if (x, y, direction) in set_visited:
                return True
            else:
                set_visited.add((x,y,direction))
    
                
def find_obstacle_position(array):
    array = [list(row) for row in array]
    rows, cols = len(array), len(array[0])
    
    start_x, start_y, direction = _find_start_position(array, rows, cols)
        
    obstacle_cnt = 0
    for i in range(rows):
        for j in range(cols):
            if array[i][j] == ".":  
                array[i][j] = "#" # Add obstacle
                if _simulator(array, rows, cols, start_x, start_y, direction):
                    obstacle_cnt += 1
                array[i][j] = "."  # Remove obstacle

    return obstacle_cnt

if __name__=="__main__":
    
    with open("data/day_6.txt", "r") as file:
        array = []
        for line in file:
            row_list= line.strip().split('\n')
            for row in row_list:
                array.append(row)
    print("Answer 1:", guard_mapped_area(array))
    print("Answer 2:", find_obstacle_position(array))