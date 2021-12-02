from solution import calculate_position

directions = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

input1 = directions.splitlines()

def test_calculate_position():
    result = calculate_position(input1)
    assert result == (10,15, 150)

directions2 = """forward 5
down 10
forward 8
up 3
down 8
forward 2"""

input2 = directions2.splitlines()

def test_calculate_position2():
    result = calculate_position(input2)
    assert result == (15,15, 225)

