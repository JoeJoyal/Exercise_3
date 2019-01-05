
import Panlindrom_num_even_len_and_odd_len

#def test_canassertTrue():
    #assert True

def panlindrom_or_not():
    N = 1234
    #expected = 2,2
    expected =count_even(),count_odd()
    
    actual = Panlindrom_num_even_len_and_odd_len.panlindrom(N)
    assert actual == expected
  