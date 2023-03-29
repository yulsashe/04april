def evaluate(x, y):
    return (x+2)*(y-3)




def is_square(width, length):
    if width<=0 or length<=0:
        return False
    if width==length:
        return True
    return False






def square_area(width, length):
    if width<=0 or length<=0:
        return 'Error'
    return  width* length




def test_is_square():
    assert is_square(3, 5) == False
    assert is_square(5, 3) == False
    assert is_square(3, 3) == True
    assert is_square(3, 0) == False
    assert is_square(0, 30) == False
    assert is_square(-3, 3) == False
    assert is_square(-5, -5) == False

def test_square_area():
    assert square_area(3, 5) == 15
    assert square_area(5, 3) == 15
    assert square_area(0, 10) == "Error"
    assert square_area(0, -4) == "Error"
    assert square_area(-5, -4) == "Error"

def test_evaluation():
    assert evaluate(2, 3) == 0
    assert evaluate(2, 0) == -12
    assert evaluate(-7, -2) == 25

if __name__ == '__main__':
    test_is_square()
    test_square_area()
    test_evaluation()
