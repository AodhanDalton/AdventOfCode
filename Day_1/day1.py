import time
with open('day1') as file:
  nums = [int(i.strip()) for i in file]
mi = min(nums)

num2 = []

# Part A
def a(x,file):
    for i in file:
        j = x - i
        if j >= mi:
            
            if j in file:
                return i * j



# Part B
def b(x,file):
    count = 0
    for i in file:
        for k in file:
            j = x- i - k
            if j in file:
                return i * k * j



start = time.time()
a1 = a(2020,nums)
a2 = b(2020,nums)

print("part a: ", a1, "time:", {time.time() - start})
print("Part b: ", a2, "time:", {time.time() - start})