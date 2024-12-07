from typing import List
from itertools import product

def possible_equation(result: int, int_list: List[int])->bool:
    operator = ['*', '+']
    oper_conseq = list(product(operator, repeat=len(int_list) - 1))
    for oper_conseq_i in oper_conseq:
        res_eq = int_list[0]
        for i in range(0, len(oper_conseq_i)):
            if oper_conseq_i[i]=='*':
                res_eq *= int_list[i+1]
            else:
                res_eq += int_list[i+1]      
        if res_eq==result:
            return True
    
    return False

def fix_by_concat_oper(result: int, int_list: List[int])->bool:
    operator = ['*', '+', '||']
    oper_conseq = list(product(operator, repeat=len(int_list) - 1))
    for oper_conseq_i in oper_conseq:
        res_eq = int_list[0]
        for i in range(0, len(oper_conseq_i)):
            if oper_conseq_i[i]=='*':
                res_eq *= int_list[i+1]
            elif oper_conseq_i[i]=='+':
                res_eq += int_list[i+1] 
            else:
                n = len(str(int_list[i+1]))
                for j in range(n):
                    res_eq*=10
                res_eq += int_list[i+1]
        if res_eq==result:
            return True
    
    return False 

if __name__=="__main__":
    # Open file for read
    with open("data/day_7.txt", "r") as file:
        ans1, ans2 = 0, 0
        for line in file:
            row = line.strip().split(':')
            result, int_list = int(row[0]), list(map(int, row[1].split()))
            if possible_equation(result, int_list):
                ans1+=result
            if fix_by_concat_oper(result, int_list):
                ans2+=result
    print("Answer 1:", ans1)
    print("Answer 2:", ans2)