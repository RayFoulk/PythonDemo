import pytest
from src.inheritance import (
    GrandParent,
    BadParentA,
    BadParentB,
    GoodParent,
)


def test_inheritance_quirks():

    # This should not be possible anyway, as pure virtual
    with pytest.raises(TypeError):
        GrandParent()

    # Neither this, because it does not implement some_method
    with pytest.raises(TypeError):
        BadParentA()

    # Slightly different due to no multiple inheritance from ABC
    with pytest.raises(TypeError):
        BadParentB()

    parent = GoodParent()
    parent.some_method('John Doe', 'Private', 12345)


