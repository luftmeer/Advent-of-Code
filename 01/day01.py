import utils

data = utils.readFile('input.txt')

# Part 1
def part1(data: list) -> int:
    base = None
    counter = 0
    for elem in data:
        if isinstance(base, type(None)):
            base = int(elem)
        
        else:
            if base < int(elem):
                counter += 1
            
        base = int(elem)

    return counter

# Part 2
def part2(data: list) -> int:
    base = int(data[0]) + int(data[1]) + int(data[2])
    counter = 0
    for i in range(1, len(data)-2):
        window = int(data[i]) + int(data[i+1]) + int(data[i+2])
        if base < window:
            counter += 1
        
        base = window
    
    return counter

print(f'Result for part 1: {part1(data)}')
print(f'Result for part 2: {part2(data)}')