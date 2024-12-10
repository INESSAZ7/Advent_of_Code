def transform_map_to_blocks(disk_map):
    file_blocks = []
    for i, num in enumerate(disk_map):
        if i%2 == 0:
            for j in range(int(num)):
                file_blocks.append(i//2)
        else:
            for j in range(int(num)):
                file_blocks.append(".")
    return file_blocks

def fragment_move(file_blocks):
    file_blocks = file_blocks.copy()
    ptr_left = 0
    ptr_right = len(file_blocks)-1
    while ptr_left<ptr_right:
        while file_blocks[ptr_left] != '.':
            ptr_left+=1
        while file_blocks[ptr_right] == '.':
            ptr_right-=1
        file_blocks[ptr_left] = file_blocks[ptr_right]
        file_blocks[ptr_right] = "."
        ptr_left+=1
        ptr_right-=1
    return file_blocks

def full_move(file_blocks):
    file_blocks = file_blocks.copy()
    
    # Identify files and free spaces
    files = []  # List of (file_id, start_idx, size)
    free_spaces = []  # List of (start_idx, size)
    
    n = len(file_blocks)
    i = 0
    while i < n:
        if file_blocks[i] != '.':
            file_id = file_blocks[i]
            start = i
            while i < n and file_blocks[i] == file_id:
                i += 1
            files.append((file_id, start, i - start)) 
        else:
            start = i
            while i < n and file_blocks[i] == '.':
                i += 1
            free_spaces.append((start, i - start))
            
    # Move files to the leftmost free space
    for file_id, start, size in files:
        for free_start, free_size in free_spaces:
            if free_size >= size and free_start < start:
                # Move the file
                for i in range(size):
                    file_blocks[free_start + i] = file_id
                # Mark old location as free
                for i in range(start, start + size):
                    file_blocks[i] = '.'
                # Update the free spaces
                free_spaces = [
                    (idx, sz) if idx != free_start else (free_start + size, free_size - size)
                    for idx, sz in free_spaces
                ]
                break  # Only move once per file
    
    return file_blocks
    
def count_sum(file_blocks):
    return sum(i*num for i , num in enumerate(file_blocks) if num!= '.' )

if __name__ == "__main__":
    with open('data/test.txt', 'r') as file:
        disk_map = file.readline()
    blocks = transform_map_to_blocks(disk_map)
    ans1 = count_sum(fragment_move(blocks))
    ans2 = count_sum(full_move(blocks))
    print('Part 1:', ans1)
    print('Part 2:', ans2)