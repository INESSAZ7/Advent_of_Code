from collections import Counter

def part_1(column1,column2):
    column1.sort()
    column2.sort()    
    diff = 0
    for i in range(len(column1)):
        diff += abs(column1[i] - column2[i])
    
    return diff
    
def part_2(left, right):
    result = 0
    right_counts = Counter(right)
    for num in left:
        result += right_counts[num] * num
    
    return result

if __name__=="__main__":
    
    with open("data/day_1.txt", "r") as file:
        column1 = []  
        column2 = [] 
        
        for line in file:
            values = line.split()  
            if len(values) >= 2:  
                column1.append(int(values[0]))  
                column2.append(int(values[1]))  

    print("Answer 1:", part_1(column1,column2))
    print("Answer 2:", part_2(column1,column2))