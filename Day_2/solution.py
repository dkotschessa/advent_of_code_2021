input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

#arr = [x.split(' ') for x in input.splitlines()]

def calculate_position(directions):
    arr = [x.split(' ') for x in directions]
    array_converted = [(x,int(y)) for x,y in arr]
    depth = 0
    horizontal = 0
    for d in array_converted:
        if d[0] == 'forward':
            horizontal += d[1]
        if d[0] == 'down':
            depth += d[1]
        if d[0] == 'up':
            depth -= d[1]
    return depth, horizontal, depth*horizontal

    
