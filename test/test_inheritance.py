import pytest
from src.inheritance import (
    GrandParent,
    InvalidParentMultiple,
    InvalidParentSingle,
    ValidParent,
    IncompatibleChildA,
    IncompatibleChildB,
)


def test_inheritance_quirks():

    # This should not be possible anyway, as pure virtual
    with pytest.raises(TypeError):
        GrandParent()

    # Neither this, because it does not implement some_method
    with pytest.raises(TypeError):
        InvalidParentMultiple()

    # Slightly different due to no multiple inheritance from ABC
    with pytest.raises(TypeError):
        InvalidParentSingle()

    parent = ValidParent()
    parent.some_method('John Doe', 'Private', 12345)

    childa = IncompatibleChildA()
    childa.some_method(1, 2, cheese='Limburger')

    childb = IncompatibleChildB()
    childb.some_method('Palindromes', 'are', 'fun', country='Belgium')
