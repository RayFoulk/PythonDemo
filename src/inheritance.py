import logging
from hexdump import (
    hexdump
)
from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any
)
logging.basicConfig(filename='')


class GrandParent(ABC):
    """
    Abstract Base Class grandparent
    """

    def __init__(self) -> None:
        self._private_value = 1

    @abstractmethod
    def base_method(self,
                    data: bytes,
                    **kwargs: Any) -> bool:
        """
        Signature low-level method

        :param data: Some data to transmit
        :return: True for success, False for failure
        """
        return False

    @abstractmethod
    def higher_method(self, data: bytes) -> bool:
        """
        Signature higher level

        :param data: Some data to transmit
        :return: True for success, False for failure
        """


class Parent(GrandParent, ABC):
    """
    Class derived from grandparent
    """

    def __init__(self) -> None:
        super(Parent, self).__init__()

    def higher_method(self,
                      data: bytes,
                      *,
                      option_a: bool = True,
                      option_b: str = 'something',
                      option_c: int = 0) -> bool:
        """
        Final implementation of higher method used by either ChildA or ChildB

        :param data: Some data to transmit
        :param option_a: Some option that only ChildA
        :param option_b: Some option that only ChildB
        :param option_c: Some option that only ChildB
        :return: True for success, False for failure
        """
        self.base_method(data,
                         option_a=option_a,
                         option_b=option_b,
                         option_c=option_c)

        # dumpstr = hexdump(data, result='return')
        # logging.debug(f'data: \n\n{dumpstr}\n\n')
        return True


class ChildA(Parent):
    """
    Child class that implements final some_method one way
    """

    def __init__(self) -> None:
        super(ChildA, self).__init__()

    def base_method(self,
                    data: bytes,
                    *,
                    option_a: bool = True,
                    **kwargs: Any) -> bool:
        """
        Establish the signature for a method in the base class

        :param data: Some data to transmit
        :param option_a: Some option that only ChildA
        :return: True for success, False for failure
        """
        dumpstr = hexdump(data, result='return')
        logging.debug(f'data: \n\n{dumpstr}\n\n')
        return True


class ChildB(Parent):
    """
    Child class that implements final some_method another way
    """

    def __init__(self) -> None:
        super(ChildB, self).__init__()

    def base_method(self,
                    data: bytes,
                    *,
                    option_b: str = 'something',
                    option_c: int = 0,
                    **kwargs: Any) -> bool:
        """
        Establish the signature for a method in the base class

        :param data: Some data to transmit
        :param option_b: Some option that only ChildB
        :param option_c: Some option that only ChildB
        :return: True for success, False for failure
        """
        dumpstr = hexdump(data, result='return')
        logging.debug(f'data: \n\n{dumpstr}\n\n')
        return True
