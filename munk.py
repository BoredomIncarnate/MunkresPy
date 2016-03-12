import random
from random import randint
from datetime import datetime
from pandas import *

def printMats(): 
    print("Cost Matrix")
    print(DataFrame(mat))
    print()
    print("Compare Matrix")
    print(DataFrame(comp))
    print()
    print("Rows Array")
    print(rows)
    print()
    print("Columns Array")
    print(cols)  
    print()
    
def findUncoveredZero():
    print("find uncovered 0")
    done = False
    r = -1 
    c = -1
    while(done != True):
        for i in range(0, n):
            for j in range(0, n):
                if(mat[i][j] == 0):
                    if(cols[j] == 0):
                        if(rows[i] == 0):
                            r = i
                            c = j
                            done = True
        done = True
    return r,c
        
def isStarInRow(row):
    found = False
    for col in range(0, n):
        if(comp[row][col] == 1):
            found = True
    return found
    
def findStarInRow(row):
    c = -1
    for col in range(0,n):
        if(comp[row][col] == 1):
            c = col
    return c
    
def findStarInCol(col):
    r = -1
    for row in range(0,n):
        if(comp[row][col] == 1):
            r = row
    return r
    
def findPrimeInRow(row):
    c = -1
    for col in range(0,n):
        if(comp[row][col] == 2):
            c = col
    return c
def step_1():
    print("Step 1")
    printMats()
    min = None
    for i in range(0,n):
        min = mat[i][0]
        for j in range(0,n):
            if(mat[i][j] < min):
                min = mat[i][j]
        for j in range(0,n):
            mat[i][j] = mat[i][j] - min
    printMats()

def step_2():
    print("Step 2")
    for i in range(0,n):
        for j in range(0,n):
            if(mat[i][j] == 0):
                if(rows[i] == 0):
                    if(cols[j] == 0):
                        comp[i][j] = 1
                        rows[i] = 1
                        cols[j] = 1
    printMats()
    
def step_3():
    print("Step 3")
    count = 0
    for i in range(0,n):
        for j in range(0,n):
            if(comp[i][j] == 1):
                cols[j] = 1
                
    for i in range(0, n):
        if(cols[i] == 1):
            count = count + 1
            
    if(count >= n):
        printMats()
        print("finished")
        return
    else:
        step_4()
        return
         
def step_4():
    print("Step 4")   
    printMats()
    r,c = findUncoveredZero()
    if(r > -1):
        print("r > -1")
        comp[r][c] = 2
        if(isStarInRow(r)):
            print("There is a starred 0 in row {}".format(r))
            rows[r] = 1
            col = findStarInRow(r)
            cols[col] = 0
            step_4()
            return
        else:
            print("No starred 0 in row {}".format(r))
            step_5(r,c)
            return
    else:
        step_6()
        return
        
    print("{},{}".format(r,c))
    return
    
def step_5(row, col):
    print("Step 5")    
    r = -1
    c = -1
    path = []
    path.append([row,col])
    done = False
    while(done == False):
        r = findStarInCol(col)
        print(r)
        if(r > -1):
            if([r,c] not in path):
                print("found starred 0 in col {}".format(col))
                path.append([r,col])
            else:
                done = True
        else:
            done = True
        if(done == False):
            c = findPrimeInRow(r)
            path.append([r,c])
            print(path)
            printMats()
            
            
    for p in range(0, len(path)):
        print("path: {},{}".format(path[p][0], path[p][1]))
        print(comp[path[p][0]][path[p][1]])
        if(comp[path[p][0]][path[p][1]] == 1):
            comp[path[p][0]][path[p][1]] = 0
        else:
            comp[path[p][0]][path[p][1]] = 1
    for i in range(0,n):
        rows[i] = 0
        cols[i] = 0
    for i in range(0,n):
        for j in range(0,n):
            if(comp[i][j] == 2):
                comp[i][j] = 0
    printMats()
    step_3()
    return

def step_6():
    print("Step 6")
    min = 999
    for i in range(0,n):
        for j in range(0,n):
            if(rows[i] == 0):
                if(cols[j] == 0):
                    if(min > mat[i][j]):
                        min = mat[i][j]
    for i in range(0,n):
        for j in range(0,n):
            if(rows[i] == 1):
                mat[i][j] = mat[i][j] + min
            if(cols[j] == 0):
                mat[i][j] = mat[i][j] - min
    printMats()
    step_4()
                        
n = int(input("N: "))

mat = [[0 for x in range(n)] for x in range(n)] #init main matrix with 0s
comp = [[0 for x in range(n)] for x in range(n)] #init comparison matrix with 0s
rows = [0 for x in range(n)] #init rows array with 0s
cols = [0 for x in range(n)] #init columns array with 0s

for i in range(0,n):
    for j in range(0,n):
        # mat[i][j] = randint(0,9) #give a pseudorandom value to element in mat
        mat[i][j] = (i + 1) * (j + 1)
        
step_1()
step_2()
step_3()