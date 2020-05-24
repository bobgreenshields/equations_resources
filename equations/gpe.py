def hello():
    """Prints hello"""
    print("Hello Luca")

class GPE:
    """The GPE equation"""
    def __init__(self):
        """initialise"""
        self.name = "Gravitational potential energy"

    def call(self):
        """asks for variables and calculates value"""
        h = int(input("Enter height: "))
        return h*h



if __name__ == "__main__":
    hello()
    gpe = GPE()
    print(gpe.name)
    print(gpe.call())
