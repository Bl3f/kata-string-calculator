import pytest
import unittest
from main import StringCalculator


def test_add_empty_string():
    str_calc = StringCalculator()
    assert str_calc.add('') == 0
