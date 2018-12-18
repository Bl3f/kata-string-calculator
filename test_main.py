import pytest
import unittest
from main import StringCalculator


def test_add_empty_string():
    str_calc = StringCalculator()
    assert str_calc.add('') == 0


def test_single_number():
    str_calc = StringCalculator()
    for i in range(0, 1000):
        assert str_calc.add(str(i)) == i
