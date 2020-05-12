from math_series import __version__
from math_series.series import *

def test_version():
    assert __version__ == '0.1.0'

def test_1():
    expected = 5
    actual = fibonacci(5)
    assert expected == actual

# test result reference http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html
def test_2():
    expected = 6557470319842
    actual = fibonacci(63)
    assert expected == actual

def test_3():
    expected = 11
    actual = lucas(5)
    assert expected == actual

# test result reference from http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/lucas200.html
def test_4():
    expected = 14662949395604
    actual = lucas(63)
    assert expected == actual


def test_5():
    expected = 5
    actual = sum_series(5)
    assert expected == actual

# without optional prams, it uses fibonacci function
# result reference from http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html
def test_6():
    expected = 6557470319842
    actual = sum_series(63)
    assert expected == actual

def test_7():
    expected = 11
    actual = sum_series(5,2,1)
    assert expected == actual

def test_8():
    expected = 14662949395604
    actual = sum_series(63,2,1)
    assert expected == actual


def test_9():
    expected = 110
    actual = sum_series(5,20,10)
    assert expected == actual


def test_10():
    expected = 146629493956040
    actual = sum_series(63,20,10)
    assert expected == actual
