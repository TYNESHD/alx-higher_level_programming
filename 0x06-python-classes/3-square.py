#!/usr/bin/python3
"""Square class to represent a square"""


class Square:
    """
    Defines a Square and its basic properties

    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """

    def __init__(self, size=0) -> None:
        """
        Innitialize size of the square. the size can be specified.
        else, the size defaults to 0

        :param size: int size of square ( > 0)
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self) -> int:
        """
        returns the area of the square
        """

        return self.__size ** 2
