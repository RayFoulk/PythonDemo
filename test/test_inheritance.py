import pytest
from src.inheritance import (
    GrandParent,
    InvalidParent,
    ChildA,
    ChildB,
)


def test_inheritance_quirks():

    # This should not be possible anyway, as pure virtual
    with pytest.raises(TypeError):
        GrandParent()

    # Neither this, because it does not implement some_method
    with pytest.raises(TypeError):
        InvalidParent()

    childa = ChildA()
    childa.some_method('one', 'two', 3, option_a='test')

    childb = ChildB()
    childb.some_method('four', 'five', 6, option_b=7)
