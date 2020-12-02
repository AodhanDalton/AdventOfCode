import time

with open('day2', 'r') as f:
    nums = [i.rstrip().split() for i in f.readlines()]

#part a
def a(row):
    _min, _max = row[0].split('-')
    letter = row[1][0]
    password = row[2]

    return int(_max) >= len([i for i in password if i == letter]) >= int(_min)

def b(row):
    password = row[2]
    l1, l2 = password[int(row[0].split('-')[0]) - 1], password[int(row[0].split('-')[1]) - 1]
    letter = row[1][0]

    return l1 != l2 and letter in (l1, l2)

print(len([1 for i in nums if a(i) is True]))
print(len([1 for i in nums if b(i) is True]))
