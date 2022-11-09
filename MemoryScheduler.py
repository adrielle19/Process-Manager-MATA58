import numpy as np
import Process
import Pages
import Memory
import VirtualMemory

class MemoryScheduler:
    def __init__ (self):
        pass

    #Escalonamento
    def FIFO(self,Mem, VMen, Process):
        
        ProcessPages = np.where(VMen == Process)

        if VMen[ProcessPages[0][0]].RamAdress != -1: # processo ja esta na memoria
            return

        if Mem.EmptyPagesNum >= Process.MemoryPages: # a memoria tem espaço vazio
            for i in range(50):
                if Mem.PageList[i].Process == None: # quando encontrar o primeiro espaço vazio
                    j = 0
                    for page in ProcessPages[0]: # liga as paginas na memoria virtual para a real e coloca o processo na real
                        VMen[page].RamAdress = i+j
                        Mem.PageList[i+j].Process = Process
                        Mem.PageList[i+j].RencentlyUsed = 50 - j
                        j += 1    
                return  
            
        # se chegou até aqui a memoria ta cheia e o processo não ta nela
        while nao tem espaço na memoria:
            # criar função que remove processo da memoria e ja compacta ela


        return

    def LRU(self,Mem, VMen, Process):

        return
