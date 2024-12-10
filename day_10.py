from typing import List

with open('data/day_10.txt', 'r') as file:
    tp_map = []
    for line in file:
        row_list= line.strip().split('\n')
        for row in row_list:
            tp_map.append(row)

direction = (
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)    
)

def _is_valid(tp_map, ni, nj):
    return 0 <= ni < len(tp_map) and 0 <= nj < len(tp_map[0])

def _find_road(tp_map, i, j, num, found_peaks):
    if num==10:
        found_peaks.add((i, j))
        #print(found_peaks)
        return 1
    for dx, dy in direction:
        if _is_valid(tp_map, i+dx, j+dy) and tp_map[i+dx][j+dy] == str(num):
            #print(f"Moving to ({i+dx}, {j+dy}) with num: {num}")
            _find_road(tp_map, i+dx, j+dy,num+1, found_peaks)
                
    return len(found_peaks)

def _find_distinct_road(tp_map, i, j, num):
    if num==10:
        return 1
    cnt = 0
    for dx, dy in direction:
        if _is_valid(tp_map, i+dx, j+dy) and tp_map[i+dx][j+dy] == str(num):
            cnt+=_find_distinct_road(tp_map, i+dx, j+dy,num+1)
                
    return cnt

def find_score(tp_map: List[str])->int:
    total_paths = 0
    total_distinct_paths = 0
    rows = len(tp_map)
    cols = len(tp_map[0])
    for i in range(rows):
        for j in range(cols):
            if tp_map[i][j]=='0':
                found_peaks = set()
                #print(i, j)
                total_paths+=_find_road(tp_map, i, j, 1, found_peaks)
                total_distinct_paths+=_find_distinct_road(tp_map, i, j, 1)
                #print(total_paths)
    
    return total_paths, total_distinct_paths

print('ans_1:', find_score(tp_map)[0])
print('ans_2:', find_score(tp_map)[1])