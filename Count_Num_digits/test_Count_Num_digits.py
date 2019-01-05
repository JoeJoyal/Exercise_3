#count the Num of digits
import Count_Num_digits
def test_canAssertTrue():
    assert True

def test_count_N_digits():
    N=12345
    expected = 5
    #Act
    actual = Count_Num_digits.countdigits(N)
    #assert
    assert actual == expected