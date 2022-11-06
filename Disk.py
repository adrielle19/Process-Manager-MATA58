import numpy as np

class Disk:
    def __init__(self, PageNum):
        self.PageSize = 4 # tamanho da pagina
        self.Space = PageNum*4 # tamanho total da memoria
        self.PageList = np. # Array com cada pagina

    def clone(self):
        Dis = Memory()
        Dis.PageSize = self.PageSize
        Dis.Space = self.Space
        Dis.PageList = self.PageList
        return Dis
