import numpy as np
import Pages
class Memory:
    def __init__(self):
        self.PageSize = 4 # tamanho da pagina
        self.Space = 200 # tamanho total da memoria
        Pages= []  
        for Process in range(50):
            Pages.append(Pages.Page(None))
        self.PageList = np.array(Pages) # Array com cada pagina                   
        self.EmptyPagesNum = 50

    def clone(self):
        Mem = Memory()
        Mem.PageSize = self.PageSize
        Mem.Space = self.Space
        Mem.PageList = self.PageList
        return Mem
