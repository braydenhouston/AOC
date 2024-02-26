def find_floor(instructions, find_basement=False):
    floor = basement = 0
    for i, char in enumerate(instructions, 1):
        floor += 1 if char == '(' else -1
        if find_basement and floor == -1 and not basement:
            basement = i
    return basement if find_basement else floor

# Test cases
print(find_floor('(())'))  # Expected output: 0
print(find_floor('()()'))  # Expected output: 0
print(find_floor('((('))  # Expected output: 3
print(find_floor('(()(()('))  # Expected output: 3
print(find_floor('))((((('))  # Expected output: 3
print(find_floor('())'))  # Expected output: -1
print(find_floor('))('))  # Expected output: -1
print(find_floor(')))'))  # Expected output: -3
print(find_floor(')())())'))  # Expected output: -3

# Read the file
with open('/home/brayden/Projects/AOC/2015/input.txt', 'r') as file:
    data = file.read().replace('\n', '')

# Call the function with the file content
print(find_floor(data))

print(find_floor(')', True))  # Output: 1
print(find_floor('()())', True))  # Output: 5

print(find_floor(data, True))  # Output: 5
