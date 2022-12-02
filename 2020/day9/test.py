def getLines():
    infile = open("input", "r")
    lines = []
    for line in infile:
        lines.append(int(line))
    return lines

def checkList(lines, sumList, x, y):
    for i in range(x, y):
        for j in range(x+1, y):
            sumList.append(lines[i]+lines[j])
    if(lines[y] not in sumList):
        return lines[y]
    else:
        x+=1
        y+=1
        sumList.clear()
        return checkList(lines, sumList, x, y)

def main():
    lines = getLines()
    sumList = []
    x = 0
    y = 25
    final = checkList(lines, sumList, x, y)
    print(final)     
main()