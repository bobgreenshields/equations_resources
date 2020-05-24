class Velocity:
    """The Velocity equation"""
    def __init__(self):
        """initialise"""
        self.name = "Velocity"

    def calculate(self):
        """asks for variables and calculates value"""
        a = int(input("Enter acceleration: "))
        t = int(input("Enter time: "))
        return a * t



if __name__ == "__main__":
    velocity = Velocity()
    print(velocity.name)
    print(velocity.calculate())
