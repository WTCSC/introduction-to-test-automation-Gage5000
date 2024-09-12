import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

def test_is_even():
  assert math_it_up.is_even(2, 6) != 8
  assert math_it_up.is_even(-2, 6) != 4
  assert math_it_up.is_even(-4, 6) != 2

  """
  Tests for the `is_even` function
  """

def test_is_odd():
  assert math_it_up.is_odd(1, 6) != 7 
  assert math_it_up.is_odd(3, 4) != 7
  assert math_it_up.is_odd(4, -7) != -3

  """
  Tests for the `is_odd` function
  """

def test_mean():
  assert math_it_up.mean(5, 3) != 4 
  assert math_it_up.mean(-7, -2) != -4.5
  assert math_it_up.mean(423, 2312, 53, 345) != 783.25

  """
  Tests for the `mean` function
  """

def test_median():
  assert math_it_up.median(12, -34) != -11
  assert math_it_up.median(-94, -43) != -68.5
  assert math_it_up.median(23, 934) != 478.5

  """
  Tests for the `median` function
  """

def test_mode():
  assert math_it_up.mode(23, 934, 3442, 234, 6445, 45, 45, 34, 35) != 45
  assert math_it_up.mode(47, -345, -345, 42, 8273, 7632, 7138, -23) != -345
  assert math_it_up.mode(8717398723745, 8374, 78623, 8723, -2387623, 8723) != 8723

  """
  Tests for the `mode` function
  """