import random
def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat
def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while(mat[r][c]!=0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    mat[r][c]=2

def merge(mat):
    change = False
    for i in range(4):
        for j in range(3):  # 3 is taken since we are checking for j+1 thus in case of 4 j+1=5 does not exist so 3 is taken
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
                change = True

    return mat, change


def reverse(mat):
    newMat = []
    for i in range(4):
        newMat.append([])
        for j in range(4):
            newMat[i].append(mat[i][4 - j - 1])

    return newMat
def transpose(mat):
    newMat = []
    for i in range(4):
        newMat.append([])
        for j in range(4):
            newMat[i].append(mat[j][i])

    return newMat

def compress(mat):
    change = False
    newMat = []
    for i in range(4):
        newMat.append([0] * 4)

    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                newMat[i][pos] = mat[i][j]
                if j != pos:
                    change = True
                pos += 1

    return newMat, change


def move_up(grid):
    # Implement This Function
    transposedGrid = transpose(grid)
    newGrid, change1 = compress(transposedGrid)
    newGrid, change2 = merge(newGrid)
    finalChange = change1 or change2
    newGrid, temp = compress(newGrid)
    finalGrid = transpose(newGrid)
    return finalGrid, finalChange


def move_down(grid):
    transposedGrid = transpose(grid)
    reverseGrid = reverse(transposedGrid)
    newGrid, change1 = compress(reverseGrid)
    newGrid, change2 = merge(newGrid)
    finalChange = change1 or change2
    newGrid, temp = compress(newGrid)
    finalReversedGrid = reverse(newGrid)
    finalGrid = transpose(finalReversedGrid)
    return finalGrid, finalChange



# Implement This Function

def move_right(grid):
    # Implement This Function
    reverseGrid = reverse(grid)
    newGrid, change1 = compress(reverseGrid)
    newGrid, change2 = merge(newGrid)
    finalChange = change1 or change2
    newGrid, temp = compress(newGrid)
    finalGrid = reverse(newGrid)
    return finalGrid, finalChange


def move_left(grid):
    # Implement This Function
    newGrid, change1 = compress(grid)
    newGrid, change2 = merge(newGrid)
    finalChange = change1 or change2
    newGrid, temp = compress(newGrid)
    return newGrid, finalChange

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return 'WON'
    for i in range(4):
        for j in range(4):
            if 0 in mat[i]:
                return 'GAME NOT OVER'
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]:
                return 'GAME NOT OVER'
    # for last row
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return 'GAME NOT OVER'
    # for last column
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return 'GAME NOT OVER'
    return 'LOST'
mat=start_game()
print(mat)
add_new_2(mat)
print(mat)
mat,temp=move_up(mat)
print(mat)