# circle.py

# Define a Circle class that works with a list of radii
class Circle:
    # Private class variable for pi
    __pi = 3.141

    # Constructor accepting a list of radii
    def __init__(self, radius_list):
        self.radius_list = radius_list  # Store the radii list

    # Method to calculate and print area of all circles
    def calculate_area(self):
        print("Area of circles:")
        for radius in self.radius_list:
            area = Circle.__pi * radius ** 2
            print(f"Radius: {radius} => Area: {area:.2f}")

    # Method to calculate and print perimeter of all circles
    def calculate_perimeter(self):
        print("\nPerimeter of circles:")
        for radius in self.radius_list:
            perimeter = 2 * Circle.__pi * radius
            print(f"Radius: {radius} => Perimeter: {perimeter:.2f}")


# Example usage
if __name__ == "__main__":
    radii = [10, 501, 22, 37, 100, 999, 87, 351]
    circle_obj = Circle(radii)
    circle_obj.calculate_area()
    circle_obj.calculate_perimeter()
