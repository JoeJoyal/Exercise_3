import prime_Num_lessthan_N

def test_canAssertTrue():
    assert True

def test_Prime_Num():
    #Arrange
    N = 10
    expected = 17
    #Act
    actual = prime_Num_lessthan_N.is_prime(N)
    #Assert
    assert  actual == expected