import AmstrongNum_or_Not

def test_canAssertTrue():
    assert True

def test_Amstrong_Num():
    #Arrange
    N = 153
    expected = 153
    #Act
    actual = AmstrongNum_or_Not.Amstrong_Num(N)
    #Assert
    assert actual == expected