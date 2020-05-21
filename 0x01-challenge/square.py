#!/usr/bin/python3
"""
File to manage of a square
"""


class square:
    """Class of a square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Method to inicialize a square with all attributes """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Modify the form to print the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Some comment """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
