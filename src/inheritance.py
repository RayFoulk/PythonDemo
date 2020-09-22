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


class BadParentA(GrandParent, ABC):
    """
    Class derived from grandparent, also itself an ABC for demo purposes.
    Note that this does not even implement some_method() as it should
    """

    def __init__(self) -> None:
        super(BadParentA, self).__init__()


class BadParentB(GrandParent):
    """
    Class derived from grandparent, also itself an ABC for demo purposes.
    Note that this does not even implement some_method() as it should
    """

    def __init__(self) -> None:
        super(BadParentB, self).__init__()


class GoodParent(GrandParent):
    """
    Class derived from grandparent, also itself an ABC for demo purposes
    """

    def __init__(self) -> None:
        super(GoodParent, self).__init__()

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


class ChildA(BadParentA):
    """
    Child class that implements final some_method one way
    """

    def __init__(self) -> None:
        super(ChildA, self).__init__()

    def some_method(self,
                    house: int,
                    mouse: int,
                    *,
                    cheese: str = 'cheddar') -> int:
        """
        A completely different implementation of some_method()

        :param house: A house
        :param mouse: A mouse
        :param cheese: Some cheese
        :return: True
        """
        print(f'House: {house}  Mouse: {mouse}  Cheese: {cheese}')
        return True


class ChildB(BadParentA):
    """
    Child class that implements final some_method another way
    """

    def __init__(self) -> None:
        super(ChildB, self).__init__()

    def some_method(self,
                    man: str,
                    plan: str,
                    canal: str,
                    *,
                    country: str = 'panama') -> str:
        """
        A completely different implementation of some_method()

        :param man: A man
        :param plan: A plan
        :param canal: A canal
        :param country: A country
        :return: A string rather than a bool or an int
        """
        print(f'Man: {man}  Plan: {plan}  Canal: {canal}  Country: {country}')
        return 'some_string'

