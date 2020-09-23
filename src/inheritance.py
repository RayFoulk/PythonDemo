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
# TODO: It is unclear (to me) if this is by design or intentional.
class InvalidParentMultiple(GrandParent, ABC):
    """
    Class derived from grandparent, also itself an ABC for demo purposes.
    Note that this does not even implement some_method() as it should
    """

    def __init__(self) -> None:
        super(InvalidParentMultiple, self).__init__()


# PyCharm IDE properly picks up that this class does not implement all abstract
# methods
class InvalidParentSingle(GrandParent):
    """
    Class derived from grandparent, also itself an ABC for demo purposes.
    Note that this does not even implement some_method() as it should
    """

    def __init__(self) -> None:
        super(InvalidParentSingle, self).__init__()


class ValidParent(GrandParent):
    """
    Class derived from grandparent, also itself an ABC for demo purposes
    """

    def __init__(self) -> None:
        super(ValidParent, self).__init__()

    def some_method(self,
                    name: str,
                    rank: str,
                    serial: int) -> bool:
        """
        Concrete, final implementation of some_method

        :param name: Name
        :param rank: Rank
        :param serial: Serial Number
        :return: True for success, False for failure
        """
        print(f'Name: {name}  Rank: {rank}  Serial: {serial}')
        return True


class IncompatibleChildA(InvalidParentMultiple):
    """
    Child class that implements final some_method one way
    """

    def __init__(self) -> None:
        super(IncompatibleChildA, self).__init__()

    def some_method(self,
                    house: int,
                    mouse: int,
                    *,
                    cheese: str = 'Cheddar') -> int:
        """
        A completely different implementation of some_method()
        Mypy correctly complains about this as expected,
        but it is allowed at runtime.

        :param house: A house
        :param mouse: A mouse
        :param cheese: Some cheese
        :return: True
        """
        print(f'House: {house}  Mouse: {mouse}  Cheese: {cheese}')
        return True


class IncompatibleChildB(InvalidParentMultiple):
    """
    Child class that implements final some_method another way
    """

    def __init__(self) -> None:
        super(IncompatibleChildB, self).__init__()

    def some_method(self,
                    man: str,
                    plan: str,
                    canal: str,
                    *,
                    country: str = 'Panama') -> str:
        """
        A completely different implementation of some_method()
        Mypy correctly complains about this as expected,
        but it is allowed at runtime.

        :param man: A man
        :param plan: A plan
        :param canal: A canal
        :param country: A country
        :return: A string rather than a bool or an int
        """
        print(f'Man: {man}  Plan: {plan}  Canal: {canal}  Country: {country}')
        return 'some_string'
