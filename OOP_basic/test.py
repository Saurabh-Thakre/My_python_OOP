class Computer:
    def __init__(self, ram, mouse, keyboard):
        self.ram = ram
        self.mouse = mouse
        self.keyboard = keyboard
        self.saurabh = "calling"

    def cal(self):
        if hasattr(self, "ipad"):
            return self.ipad
        else:
            return "no attribute ipad present"
        return self.mouse

    def cala(self, ipad):
        self.ipad = ipad

c1 = Computer("32 GB", "logitech", "cyberstock")
print(c1.cal())
c1.cala("ipad attribute is presernt now")
print(c1.cal())
