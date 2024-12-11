from collections import defaultdict

# def _blink_part1(stones):
#     add = []
#     for i, num in enumerate(stones):
#         # print(i)
#         # print(num)
#         ln = len(str(num))
#         if num == 0:
#             stones[i]=1
#         elif ln%2==0:
#             stones[i] = int(str(num)[0:ln//2])
#             add.append(int(str(num)[ln//2:ln]))
#         else:
#             stones[i] = int(num)*2024
#     stones+=add
#     return stones


def _blink(cnt_stones):
    work_stones = cnt_stones.copy()
    for stone, cnt in work_stones.items():
        ln = len(str(stone))
        if stone == 0:
            cnt_stones[1]+=cnt
        elif ln%2==0:
            cnt_stones[int(str(stone)[0:ln//2])]+=cnt
            cnt_stones[int(str(stone)[ln//2:ln])]+=cnt
        else:
            cnt_stones[int(stone)*2024]+=cnt
            
        cnt_stones[stone]-=cnt
        
    return cnt_stones


if __name__=="__main__":
    n = int(input())
    with open('data/day_11.txt', 'r') as f:
        stones = list(map(int, f.readline().split(' ')))

    cnt_stones = defaultdict(int)
    for stone in stones:
        cnt_stones[stone]+=1

    for i in range(n):
        _blink(cnt_stones)
    
    print('Answer:', sum(cnt_stones.values()))