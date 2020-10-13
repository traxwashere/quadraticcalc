numbers = [2,3,4,5,6,-100,55]
minimum = numbers[0]
for x in numbers:
    if x < minimum:
        minimum = x
print(minimum)
maximum = numbers[0]
for y in numbers:
    if y>maximum:
        maximum=y
print(maximum)