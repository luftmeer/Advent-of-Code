import utils

# Part 1
def part1(data: list) -> int:
    horizontal, depth = 0, 0
    stripped = map(lambda x: x.split(' '), data)
    for movement, value in stripped:
        value = int(value)
        if movement == 'forward':
            horizontal += value
        
        if movement == 'up':
            depth -= value
        elif movement == 'down':
            depth += value

    
    return depth * horizontal

# Part 2
def part2(data: list) -> int:
    horizontal, depth, aim = 0, 0, 0
    stripped = map(lambda x: x.split(' '), data)
    for movement, value in stripped:
        value = int(value)

        if movement == 'down':
            aim += value
        elif movement == 'up':
            aim -= value
        elif movement == 'forward':
            horizontal += value
            depth += aim * value

    
    return depth * horizontal



# Read in
data = utils.readFile('input.txt')

print(f'Result for part 1: {part1(data)}')
print(f'Result for part 2: {part2(data)}')