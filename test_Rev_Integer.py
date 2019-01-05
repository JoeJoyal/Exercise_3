import Rev_Integer

def test_canAssertTest():
    assert True

def test_RevInteger():
    #Arrange
    N=12345
    expected = 54321
    #Act
    actual = Rev_Integer.RevInteger(N)
    #Assert
    assert actual == expected