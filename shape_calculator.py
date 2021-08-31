class Rectangle:
    def __init__(self, width, height):
        """
        Constructor for the Rectangle class

        Args:
            width (int):    Represents the width of the shape.
            height (int):   Represents the height of the shape.
        """
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        """
        Setter/mutator for the width of the shape

        Args:
            width (int): Represents the width of the shape.
        """
        self._width = width

    def set_height(self, height):
        """
        Setter/mutator for the height of the shape

        Args:
            height (int): Represents the width of the shape.
        """
        self._height = height

    def get_width(self):
        """
        Getter/accessor for the width of the shape

        Returns:
            int: Returns the width of the shape
        """
        return self._width

    def get_height(self):
        """
        Getter/accessor for the height of the shape

        Returns:
            int: Returns the height of the shape
        """
        return self._height

    def get_area(self):
        """
        Calculates the area of the shape

        Returns:
            int: Returns the area of the shape
        """
        return self.get_width() * self.get_height()

    def get_perimeter(self):
        """
        Calculates the perimeter of the shape

        Returns:
            int: Returns the perimeter of the shape
        """
        return self.get_width() * 2 + self.get_height() * 2

    def get_diagonal(self):
        """
        Calculates the diagonal

        Returns:
            int: Returns the diagonal
        """
        return (self.get_width() ** 2 + self.get_height() ** 2) ** 0.5
    
    def get_picture(self):
        if self.get_width() > 50 or self.get_height() > 50:
            return "Too big for picture."
        
        return ("*"*self.get_width() + "\n")*self.get_height()

    def get_amount_inside(self, shape):
        """
        Returns the amount of shapes that can fit inside another shape

        Args:
            shape (Rectangle | Square): Represents the shape that is being compared

        Returns:
            int: Returns the number of shapes that will fit
        """
        return (self.get_area() // shape.get_area())

    def __str__(self):
        """
        Displays a message when a Rectangle object is printed

        Returns:
            str: Returns the message that should be displayed
        """
        return "Rectangle(width={}, height={})".format(self.get_width(), self.get_height())


class Square(Rectangle):
    def __init__(self, side):
        """
        Constructor for the Square class

        Args:
            side (int): Represents the sides (width and height) of the square
        """
        super().__init__(side, side)
        self.set_side(side)

    def set_width(self, width):
        """
        Sets the width, height, and sides of the square

        Args:
            width (int): Represents the width, height, and sides of the square
        """
        self._width = width
        self._height = width
        self._side = width

    def set_height(self, height):
        """
        Sets the width, height, and sides of the square

        Args:
            height (int): Represents the width, height, and sides of the square
        """
        self._height = height
        self._width = height
        self._side = height

    def set_side(self, side):
        """
        Setter/mutator for the sides of the square and the width and height

        Args:
            side (int): Represents the sides of the square
        """
        self._side = side
        self._width = side
        self._height = side

    def get_side(self):
        """
        Getter/accessor for the sides of the square

        Returns:
            int: Returns the sides of the square
        """
        return self._side

    def __str__(self):
        """
        Displays a message when a Square object is printed

        Returns:
            str: Returns the message that should be displayed
        """
        return "Square(side={})".format(self.get_side())
