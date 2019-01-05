import Divisible_of_N

def test_canAssertTure():
    assert True

def test_Divisible_of_all_N():
    #Arrange
    N=32
    expected ="Num can be divided by all integer"
    #Act
    actual = Divisible_of_N.divisible_N(N)
    assert actual == expected

def test_Divisible_of_all_N_1():
    #Arrange
    N=1234
    expected ="Num can't be divided"
    #Act
    actual = Divisible_of_N.divisible_N(N)
    assert actual == expected