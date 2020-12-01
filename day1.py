with open('day1') as file:
  nums = [int(i.strip()) for i in file]
for i in nums:  
    for j in nums:
        if (i + j==2020):
            num1 = i
            num2 = j
            break
        else:
            continue
print("Numbers that add to 2020: ",num1, num2)
print(num1*num2)