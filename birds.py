class birds:
    def __init__(self):
        print("Bird is ready")

    def head(self):
        print("Head")

    def body(self):
        print("Body")

    def wing(self):
        print("Wing")

    def leg(self):
        print("Leg")

class rajawali(birds):
    def __init__(self):
        super().__init__()
        print("Rajawali is coming")

    def head(self):
        print("Has a beak")

    def body(self):
        print("Strong")

    def wing(self):
        print("Wide")

    def leg(self):
        print("Claw")

Raja = rajawali()
Raja.head()
Raja.body()
Raja.wing()
Raja.leg()