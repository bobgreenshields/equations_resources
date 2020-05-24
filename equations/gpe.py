def hello():
    """Prints hello"""
    print("Hello Luca")

class GPE:
    """The GPE equation"""
    def __init__(self):
        """initialise"""
        self.description = "Gravitational potential energy"

    def call(self):
        """asks for variables and calculates value"""
        h = input("Enter height: ")
        print(h)
        



if __name__ == "__main__":
    hello()
    gpe = GPE()
    print(gpe.description)
    gpe.call()
