import os
import pytest
from src.inheritance import (
    GrandParent,
    Parent,
    ChildA,
    ChildB,
)


def test_inheritance_quirks():

    # This should not be possible anyway, as pure virtual
    with pytest.raises(TypeError):
        GrandParent()

    # Neither this, because it does not implement some_method
    with pytest.raises(TypeError):
        Parent()

    childa = ChildA()
    childa.higher_method(os.urandom(64), option_a=False)

    childb = ChildB()
    childb.higher_method(os.urandom(64), option_b='something_else', option_c=7)
