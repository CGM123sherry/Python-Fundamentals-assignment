class Car:

    """
    A blueprint to represent a car.

    Attributes:
    make (str): The make.
    model (str): The model.
    year (int): The year the car was made.

    Methods:
    display_info(): Prints the car's information.
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"car:{self.make} {self.model} {self.year}")