import numpy as np
class Memory:
    def __init__(self):
        self.PageSize = 4 # tamanho da pagina
        self.Space = 200 # tamanho total da memoria
        self.PageList = np.zeros(50, dtype=int) # Array com cada pagina       
        for i in range(50):
            self.PageList[i] = -1 # -1 significa que ta vazia
        self.EmptyPagesNum = 50

    def clone(self):
        Mem = Memory()
        Mem.PageSize = self.PageSize
        Mem.Space = self.Space
        Mem.PageList = self.PageList
        return Mem
