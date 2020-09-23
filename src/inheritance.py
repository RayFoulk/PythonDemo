from abc import (
    ABC,
    abstractmethod,
)


class GrandParent(ABC):
    """
    Abstract Base Class grandparent
    """

    def __init__(self) -> None:
        self._private_value = 1

    @abstractmethod
    def some_method(self,
                    name: str,
                    rank: str,
                    serial: int) -> bool:
        """
        Establish the signature for a method in the base class

        :param name: Name
        :param rank: Rank
        :param serial: Serial Number
        :return: True for success, False for failure
        """
        return False


# PyCharm IDE does not pick up that this class does not implement all abstract
# methods.  The multiple inheritance from ABC is directly related to this.
# Warning in PyCharm goes away when either: InvalidParent(GrandParent, ABC)
# OR: InvalidParent(ABC, GrandParent)
class InvalidParent(GrandParent):
    """
    Class derived from grandparent
    Note that this does not even implement some_method() as it should
    """

    def __init__(self) -> None:
        super(InvalidParent, self).__init__()


class ChildA(InvalidParent):
    """
    Child class that implements final some_method one way
    """

    def __init__(self) -> None:
        super(ChildA, self).__init__()

    def some_method(self,
                    name: str,
                    rank: str,
                    serial: int,
                    *,
                    option_a: str = 'Nothing') -> bool:
        """
        Establish the signature for a method in the base class

        :param name: Name
        :param rank: Rank
        :param serial: Serial Number
        :param option_a: Some option that only ChildA uses
        :return: True for success, False for failure
        """
        return True


class ChildB(InvalidParent):
    """
    Child class that implements final some_method another way
    """

    def __init__(self) -> None:
        super(ChildB, self).__init__()

    def some_method(self,
                    name: str,
                    rank: str,
                    serial: int,
                    *,
                    option_b: int = -1) -> bool:
        """
        Establish the signature for a method in the base class

        :param name: Name
        :param rank: Rank
        :param serial: Serial Number
        :param option_b: Some option that only ChildB uses
        :return: True for success, False for failure
        """
        return True
