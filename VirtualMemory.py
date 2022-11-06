import numpy as np
class VirtualMemory:
    def __init__(self, ProcessList):
        self.PageSize = 4 # tamanho da pagina

        # Cria as paginas na memoria virtual com o id do processo
        Pages= []  
        for Process in ProcessList:
            print(Process.ProcessId)
            for i in range(Process.MemoryPages):
                Pages.append(Process.ProcessId)
        print(Pages)

        self.Space = len(Pages)*4 # tamanho total da memoria
        self.PageList = np.array(Pages, dtype=int) # Array com cada pagina
        


    def clone(self):
        Mem = VirtualMemory(None)
        Mem.PageSize = self.PageSize
        Mem.Space = self.Space
        Mem.PageList = self.PageList
        return Mem
