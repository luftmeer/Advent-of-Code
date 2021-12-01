'''
Collection of helper functions.
'''

def readFile(filename: str) -> list:
    with open(filename, 'r') as file:
        data = file.readlines()
        # Remove linebreaks
        data = list(map(lambda x: x.strip(), data))
    return data