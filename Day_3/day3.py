import time

slope  = tuple(line.rstrip('\n') for line in open("day3").readlines())

def calc(slope, right, down):
    width = len(slope[0])
    height = len(slope)
    count = 0
    y = right
    for x in range(down, height, down):
        if slope[x][y] == "#":
            count += 1
        y = (y + right) % width
    return count

start = time.time()

a = calc(slope, 3, 1)
b = calc(slope, 1, 1) * a * calc(slope, 5, 1) * calc(slope, 7, 1) * calc(slope, 1, 2)

# part 1
print("Part A:",a , "Time:", {time.time()-start})

# part 2
print ("Part B:",b ,"Time:", {time.time()-start})