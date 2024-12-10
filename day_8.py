from itertools import combinations

def _parse_map(grid):
    antennas = []
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] not in ".":  
                antennas.append((i, j, grid[i][j]))
    return antennas, rows, cols

def _find_antinodes(antennas, rows, cols):
    antinodes = set()

    # Group antennas by frequency
    freq_groups = {}
    for i, j, freq in antennas:
        freq_groups.setdefault(freq, []).append((i, j))
    # print('freq_groups:', freq_groups )

    for freq, group in freq_groups.items():
        group_comb = list(combinations(group, 2))
        # print('freq', freq,  'group', group, ':', group_comb)
        # print('\n')
        for comb in group_comb:
            r1 = 2*comb[0][0]-comb[1][0]
            c1 = 2*comb[0][1]-comb[1][1]
            r2 = 2*comb[1][0]-comb[0][0]
            c2 = 2*comb[1][1]-comb[0][1]
            antinodes.add((r1, c1))
            antinodes.add((r2, c2))

    valid_antinodes = {(r, c) for r, c in antinodes if 0 <= r < rows and 0 <= c < cols}
    return valid_antinodes

def count_antinodes(grid):
    antennas, rows, cols = _parse_map(grid)
    antinodes = _find_antinodes(antennas, rows, cols)
    return len(antinodes)


if __name__=="__main__":
    with open("data/day_8.txt", "r") as file:
        array = []
        for line in file:
            row_list= line.strip().split('\n')
            for row in row_list:
                array.append(row)
                
    print("Part 1:", count_antinodes(array))