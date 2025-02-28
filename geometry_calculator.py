import math

class GeometryCalculator:
    """A simple geometry calculator for circles and rectangles."""

    def calculate_circle_area(self, radius):
        """Calculate the area of a circle given its radius."""
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        """Calculate the area of a rectangle given its length and width."""
        return length * width

if __name__ == "__main__":
    calculator = GeometryCalculator()

    # Circle Area Calculation
    radius = 5
    print(f"The area of the circle with radius {radius} = {calculator.calculate_circle_area(radius):.2f}")

    # Rectangle Area Calculation
    length = 10
    width = 6
    print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width):.2f}")
