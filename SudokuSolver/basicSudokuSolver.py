from typing import Tuple


def addPlan():
    plan = []
    for i in range(9):
        inner_list = []
        print("Set {}. line, add your numbers:\n(instead of blank space fill 0)".format(i + 1))
        for j in range(9):
            x = int(input("{}. column:".format(j + 1)))
            inner_list.append(x)
        plan.append(inner_list)
    return plan

def drawPlan(plan):
    for i in range(9):
        print(9*"----")
        for j in range(9):
            print("|", end=" ")
            print(plan[i][j], end=" ")
            if j == 8:
                print("|")

def check_line(line):
    line_in_set = set()

    for nums in range(9):
        line_in_set.add(line[nums])
    return len(line_in_set) == 9 and sum(line_in_set) == 45


def check_column(plan, col):
    col_in_set = set()
    for i in range(9):
        col_in_set.add(plan[i][col])
    return len(col_in_set) == 9 and sum(col_in_set) == 45


def check_square(plan, position: Tuple[int, int]):
    x, y = position
    #sets od nums:
    first = {0,3,6}
    second = {1,4,7}
    third = {2,5,8}
    # columns: 0, 3, 6; lines: 0, 3, 6
    if x in first and x in first:
        s = set()
        for i in range(3):
            for j in range(3):
                s.add(plan[i][j])
        return len(s) == 9 and sum(s) == 45

    # columns: 0, 3, 6; lines: 1, 4, 7
    # columns: 0, 3, 6; lines: 2, 5, 8
    # columns: 1, 4, 7; lines: 1, 4, 7
    # columns: 1, 4, 7; lines: 0, 3, 6
    # columns: 1, 4, 7; lines: 2, 5, 8
    # columns: 2, 5, 8; lines: 2, 5, 8
    # columns: 2, 5, 8; lines: 1, 4, 7
    # columns: 2, 5, 8; lines: 0, 3, 6



p1 = [[1,0,3,8,4,0,6,0,7],[2,0,3,8,2,0,6,1,7],[3,0,3,8,4,0,6,0,7],[4,0,3,8,4,0,6,0,7],[5,0,3,8,2,0,6,1,7],[6,0,3,8,4,0,6,0,7],[7,0,3,8,4,0,6,0,7],[8,0,3,8,2,0,6,1,7],[9,0,3,8,4,0,6,0,7]]
drawPlan(p1)
print(check_square(p1, (0,0)))




