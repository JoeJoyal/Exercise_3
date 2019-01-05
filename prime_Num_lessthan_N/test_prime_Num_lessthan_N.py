import prime_Num_lessthan_N

def test_canAssertTrue():
    assert True

def test_Prime_Num():
    #Arrange
    N = 15
    expected = 7
    #Act
    actual = prime_Num_lessthan_N.primeNumber_N(N)
    #Assert
    assert actual == expected