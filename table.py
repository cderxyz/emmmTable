import random

# pair0<pair1
def getCombinationsIndex(pair0, pair1, scale):
    index=0
    for i in range(pair0):
        index=index+(scale-1-i)
    index=index+(pair1-pair0)-1
    return index

scale=10

combinationsNum=scale*(scale-1)//2

mappingTable=[i for i in range(scale)]

random.shuffle(mappingTable)

combinations=[]
count=0
for i in range(scale):
    for j in range(i+1, scale, 1):
        combinations.append(count)
        count=count+1
print(len(combinations))
print(combinations)

mappingCombinations=[0 for i in range(combinationsNum)]
for i in range(scale):
    for j in range(i+1, scale, 1):
        if mappingTable[i]>mappingTable[j]:
            mappingPair0=mappingTable[j]
            mappingPair1=mappingTable[i]
        else:
            mappingPair0=mappingTable[i]
            mappingPair1=mappingTable[j]
        mappingCombinations[getCombinationsIndex(mappingPair0, mappingPair1, scale)]=combinations[getCombinationsIndex(i, j, scale)]

print(len(mappingCombinations))
print(mappingCombinations)
print(sorted(mappingCombinations))

# row first
def get2dTable(width, height, colors):
    table=[]
    for i in range(height):
        row=[]
        for j in range(width):
            row.append(colors.pop(0))
        table.append(row)
    return table

def getRowsColorCount(table):
    rowsColorCount=[]
    for row in table:
        rowColorCount={}
        for color in row:
            if color in rowColorCount:
                rowColorCount[color]=rowColorCount[color]+1
            else:
                rowColorCount[color]=1
        rowsColorCount.append(rowColorCount)
    return rowsColorCount

def getColumnsColorCount(table):
    columnsColorCount=[]
    height=len(table)
    width=len(table[0])
    for column in range(width):
        columnColorCount={}
        for row in range(height):
            color=table[row][column]
            if color in columnColorCount:
                columnColorCount[color]=columnColorCount[color]+1
            else:
                columnColorCount[color]=1
        columnsColorCount.append(columnColorCount)
    return columnsColorCount

def getColumnsColorDistribution(table):
    pass

w=6
h=3

colorsSize=[3,5,5,5]
colors=[]
for i in range(len(colorsSize)):
    colors=colors+[i]*colorsSize[i]
print(colors)

table=get2dTable(w, h, colors)
for row in table:
    print(row)

rowsColorCount=getRowsColorCount(table)
print(rowsColorCount)

columnsColorCount=getColumnsColorCount(table)
print(columnsColorCount)
