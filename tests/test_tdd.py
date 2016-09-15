import pytest
import tdd

#You write all of the tests first, then write the function to pass the test
def test_n_neg():
    assert tdd.n_neg('E') == 1
    assert tdd.n_neg('D') == 1
    assert tdd.n_neg('') == 0
    assert tdd.n_neg('ACKCKADE') == 2
    assert tdd.n_neg('DED') == 3
    assert tdd.n_neg('ackckade') == 2

    return None
