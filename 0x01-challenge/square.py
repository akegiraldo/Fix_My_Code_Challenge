#!/usr/bin/python3
""" File to manage of a square """


class Square():
    """ Class of a square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Method to inicialize a square with all attributes """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimeter of the square """
        return (self.width + self.height) * 2

    def __str__(self):
        """ Modify the form to print the square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Some comment """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
