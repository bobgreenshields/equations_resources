def hello():
    """Prints hello"""
    print("Hello Luca")

class GPE:
    """The GPE equation"""
    def __init__(self):
        """initialise"""
        self.name = "Gravitational potential energy"

    def calculate(self):
        """asks for variables and calculates value"""
        m = int(input("Enter mass: "))
        h = int(input("Enter height: "))
        return m * 9.8 * h



if __name__ == "__main__":
    hello()
    gpe = GPE()
    print(gpe.name)
    print(gpe.calculate())
