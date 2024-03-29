#!/usr/bin/python3
'''
Module for Rectangle class.
'''
class Rectangle:
    """This class defines a simple Rectangle."""
    number_of_instances = 0
    """int: The number of active instances."""
    print_symbol = '#'
    """type: print symbol, can be any type."""
    def __init__(self, width=0, height=0):
        """Constructor
        Args:
            width: The width of rectangle.
            height: The height of rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1
    @property
    def width(self):
        """Property for the width of the rectangle.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """Property for the height of the rectangle.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height
    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
    def __str__(self):
        """returns printable string representation of the rectangle"""
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_symbol) * self.width  + "\n") *
                self.height)[:-1]
    def __repr__(self):
        """returns a strings representation of the rectangles"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye Rectangle...")
        Rectangle.number_of_instances -= 1
