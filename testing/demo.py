"""
__author__ = 'hogwarts_xixi'
"""
import pytest

# try:
#     a = 1 / 0
# except ZeroDivisionError as e :
#     print("除数为0")

with pytest.raises(ZeroDivisionError) as e:
    a = 1 / 0
