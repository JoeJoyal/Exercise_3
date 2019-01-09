import perfect_square_lessthan_N

def test_canAssertTrue():
    assert True

def test_perfect_square():
    #Arrange
    N = 5
    expected = True
    #Act
    actual = perfect_square_lessthan_N.perfectSquare(N)
    #Assert
    assert actual == expected