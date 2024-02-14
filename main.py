class Iphone:
    def __init__(self):
        super().__init__()
        self.memory = 128


class Samsung:
    def __init__(self):
        self.camera = "1023px"


class Xiomi(Iphone, Samsung):
    def print_info3(self):
        print("Operation memory = 12 gb")
        print(f"Memory = {self.memory}")
        print(f"Pixels of camera = {self.camera}")


PH3 = Xiomi()

PH3.print_info3()
