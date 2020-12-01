with open('day1') as file:
  nums = [int(i.strip()) for i in file]
for i in nums:  
    for j in nums:
        for x in nums:
            if (i + j + x==2020):
                num1 = i
                num2 = j
                num3 = x
                break
            else:
                continue
print("Numbers that add to 2020: ",num1, num2, num3)
print(num1*num2*num3)