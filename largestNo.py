numbers = [3,6,4,10,99,0,12,1]
max = numbers[0]
for item in numbers:
    if max < item:
        max = item
print(max)
