numbers = [2,2,3,33,4,5,66,66,7,8,8,9,9]
unique = []

for item in numbers:
    if item not in unique:
        unique.append(item)


print(unique)