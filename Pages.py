class Page:
    def __init__(self, Process, RencentlyUsed = 50):
        self.Process = Process
        self.RencentlyUsed = RencentlyUsed

class VirtualPage:
    def __init__(self, Process):
        self.Process = Process
        self.RamAdress = -1 