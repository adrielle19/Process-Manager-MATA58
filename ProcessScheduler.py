import Process
import numpy as np

class ProcessScheduler:
    
    ExecutingProcess = None

    def __init__(self, Quantum, Overload):
        self.Quantum = Quantum
        self.Overload = Overload

    def TurnAround(self, ProcessList):
        Turnaround = 0
        for process in ProcessList:
            Turnaround += process.WaitTime + process.ExecutionTime
        return Turnaround/ProcessList.size

    # Escalonamento
    def FIFO(self, ProcessArray):
            WorkingArray = np.array([]) 

            for process in ProcessArray: # copia pq python é so por referencia
                WorkingArray = np.append(WorkingArray, process.clone() )

            ReadyList = np.array(WorkingArray)
            TotalTime = 0
            ProcessCount = WorkingArray.size
            ExecutingProcess = None

            #execuçao dos processos
            while ProcessCount != 0:

                #Escolhe o proximo
                if ExecutingProcess == None: # so escolhe o proximo se nenhum estiver sendo executado
                    for process in ReadyList:
                        if process.StartTime <= TotalTime: # escolhe o primeiro caso alguem ja tenho chegado
                            ExecutingProcess = process
                            break

                TotalTime += 1
                print("Tempo atual:" + str(TotalTime))

                try:
                    ExecutingProcess.ExecutedTime += 1

                    if ExecutingProcess.ExecutedTime == ExecutingProcess.ExecutionTime: # Remove o processo caso tenha terminado
                            ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                            ExecutingProcess = None
                            ProcessCount -= 1
                except:
                    pass

                #Tempo de espera para calculo de turnaround
                for process in ReadyList:
                    if (process == ExecutingProcess) or (process.StartTime >= TotalTime):#não conta se é o que ta execuntado ou ainda "não chegou"
                        continue
                    process.WaitTime += 1


                for process in WorkingArray:
                    print("Chegada: " +str(process.StartTime)+ " Job: " +str(process.ExecutionTime) + " Tempo executado : "+ str(process.ExecutedTime) + " Tempo de Espera : " + str(process.WaitTime) + " ProcessCount: " + str(ProcessCount))        
                print("----------------------------")
            
            print("TotalTime : ")
            print(TotalTime)
            print("----------------------------------")
            

            print("Turnaround : ")
            print(self.TurnAround(WorkingArray))
            print("----------------------------------")
            return


    def Sjf(self, ProcessArray):
        WorkingArray = np.array([]) 

        for process in ProcessArray: # copia pq python é so por referencia
            WorkingArray = np.append(WorkingArray, process.clone() )

        ReadyList = np.array(WorkingArray)
        TotalTime = 0
        ProcessCount = WorkingArray.size
        ExecutingProcess = None

        #execuçao dos processos
        while ProcessCount != 0:
            #Escolhe o proximo
            if ExecutingProcess == None: # so escolhe o proximo se nenhum estiver sendo executado
                for process in ReadyList:
                    if process.StartTime <= TotalTime : # so escolhe o proximo caso alguem ja tenho chegado
                        if ExecutingProcess == None: # escolhe o 1 para comparação
                            ExecutingProcess = process
                        else: # encontra o com menor job dos que ja chegaram
                            if process.ExecutionTime - process.ExecutedTime  < ExecutingProcess.ExecutionTime - ExecutingProcess.ExecutedTime:
                                ExecutingProcess = process

            TotalTime += 1
            print("Tempo atual:" + str(TotalTime))

            try:
                ExecutingProcess.ExecutedTime += 1

                if ExecutingProcess.ExecutedTime == ExecutingProcess.ExecutionTime: # Remove o processo caso tenha terminado
                        ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                        ExecutingProcess = None
                        ProcessCount -= 1
            except:
                pass
            #Tempo de espera para calculo de turnaround
            for process in ReadyList:
                if (process == ExecutingProcess) or (process.StartTime >= TotalTime):#não conta se é o que ta execuntado ou ainda "não chegou"
                    continue
                process.WaitTime += 1


            for process in WorkingArray:
                print("Chegada: " +str(process.StartTime)+ " Job: " +str(process.ExecutionTime) + " Tempo executado : "+ str(process.ExecutedTime) + " Tempo de Espera : " + str(process.WaitTime) + " ProcessCount: " + str(ProcessCount))        
            print("----------------------------")
        
        print("TotalTime : ")
        print(TotalTime)
        print("----------------------------------")
        print("Turnaround : ")
        print(self.TurnAround(WorkingArray))
        print("----------------------------------")
        return


    def RoundRobin(self, ProcessArray):
        
        WorkingArray = np.array([]) 

        for process in ProcessArray: # copia pq python é so por referencia
            WorkingArray = np.append(WorkingArray, process.clone() )

        CopyArray = np.array(WorkingArray)

        ReadyList = np.array([])
        TotalTime = 0
        ProcessCount = WorkingArray.size
        ExecutingProcess = None

        Overloading = False
        OverloadTime = self.Overload

        #execuçao dos processos
        while ProcessCount != 0:

            for process in WorkingArray:
                if process.StartTime <= TotalTime:
                    ReadyList = np.append(ReadyList, process)
                    WorkingArray = np.delete(WorkingArray, np.where(WorkingArray == process))
            



            if ExecutingProcess == None: # so escolhe o proximo se nenhum estiver sendo executado
                for process in ReadyList:
                    ExecutingProcess = process
                    break

            TotalTime += 1
            print("Tempo atual:" + str(TotalTime))

            if not Overloading:
                try:
                    ExecutingProcess.ExecutedTime += 1
                    ExecutingProcess.ExecutionTimePerQuantum += 1

                    if ExecutingProcess.ExecutedTime == ExecutingProcess.ExecutionTime: # Remove o processo caso tenha terminado
                            ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                            ExecutingProcess = None
                            ProcessCount -= 1        

                    elif ExecutingProcess.ExecutionTimePerQuantum == self.Quantum:
                        ExecutingProcess.ExecutionTimePerQuantum = 0
                        print("Overloading")
                        Overloading = True        

                except:
                    pass

                #Tempo de espera para calculo de turnaround
                for process in ReadyList:
                    if (process == ExecutingProcess) or (process.StartTime >= TotalTime):#não conta se é o que ta execuntado ou ainda "não chegou"
                        continue
                    process.WaitTime += 1
            else:
                ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                ReadyList = np.append(ReadyList, ExecutingProcess)
                for process in ReadyList:
                    if process.StartTime > TotalTime:#não conta se é o que ta execuntado ou ainda "não chegou"
                        continue
                    process.WaitTime += 1
                OverloadTime -= 1
                if OverloadTime == 0:
                    OverloadTime = self.Overload
                    ExecutingProcess = None
                    Overloading = False
              
            for process in CopyArray:
                print("Chegada: " +str(process.StartTime)+ " Job: " +str(process.ExecutionTime) + " Tempo executado : "+ str(process.ExecutedTime) + " Tempo de Espera : " + str(process.WaitTime) + " ProcessCount: " + str(ProcessCount))        
            print("----------------------------")

        
        print("TotalTime : ")
        print(TotalTime)
        print("----------------------------------")
        

        print("Turnaround : ")
        print(self.TurnAround(CopyArray))
        print("----------------------------------")
        return

    def Edf(self, ProcessArray):
        WorkingArray = np.array([]) 

        for process in ProcessArray: # copia pq python é so por referencia
            WorkingArray = np.append(WorkingArray, process.clone() )

        CopyArray = np.array(WorkingArray)

        ReadyList = np.array([])
        TotalTime = 0
        ProcessCount = WorkingArray.size
        ExecutingProcess = None

        Overloading = False
        OverloadTime = self.Overload

        #execuçao dos processos
        while ProcessCount != 0:

            for process in WorkingArray:
                if process.StartTime <= TotalTime:
                    ReadyList = np.append(ReadyList, process)
                    WorkingArray = np.delete(WorkingArray, np.where(WorkingArray == process))
            



            if ExecutingProcess == None: # so escolhe o proximo se nenhum estiver sendo executado
                for process in ReadyList:
                    if process.StartTime <= TotalTime : # so escolhe o proximo caso alguem ja tenho chegado
                        if ExecutingProcess == None: # escolhe o 1 para comparação
                            ExecutingProcess = process
                        else: # encontra o com menor job dos que ja chegaram
                            if process.Deadline - (TotalTime - process.StartTime)  < ExecutingProcess.Deadline - (TotalTime - ExecutingProcess.StartTime):
                                ExecutingProcess = process

            TotalTime += 1
            print("Tempo atual:" + str(TotalTime))

            if not Overloading:
                try:
                    ExecutingProcess.ExecutedTime += 1
                    ExecutingProcess.ExecutionTimePerQuantum += 1

                    if ExecutingProcess.Deadline - (TotalTime - ExecutingProcess.StartTime) < 0:
                        ExecutingProcess.MetDeadline = False

                    if ExecutingProcess.ExecutedTime == ExecutingProcess.ExecutionTime: # Remove o processo caso tenha terminado
                            ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                            ExecutingProcess = None
                            ProcessCount -= 1        

                    elif ExecutingProcess.ExecutionTimePerQuantum == self.Quantum:
                        ExecutingProcess.ExecutionTimePerQuantum = 0
                        print("Overloading")
                        Overloading = True        

                except:
                    pass

                #Tempo de espera para calculo de turnaround
                for process in ReadyList:
                    if (process == ExecutingProcess) or (process.StartTime >= TotalTime):#não conta se é o que ta execuntado ou ainda "não chegou"
                        continue
                    process.WaitTime += 1
            else:
                ReadyList = np.delete(ReadyList, np.where(ReadyList == ExecutingProcess))
                ReadyList = np.append(ReadyList, ExecutingProcess)
                for process in ReadyList:
                    if process.StartTime > TotalTime:#não conta se é o que ta execuntado ou ainda "não chegou"
                        continue
                    process.WaitTime += 1
                OverloadTime -= 1
                if OverloadTime == 0:
                    OverloadTime = self.Overload
                    ExecutingProcess = None
                    Overloading = False
              
            for process in CopyArray:
                print("Chegada: " +str(process.StartTime)+ " Job: " +str(process.ExecutionTime) + " Tempo executado : "+ str(process.ExecutedTime) + " Tempo de Espera : " + str(process.WaitTime) + " ProcessCount: " + str(ProcessCount) + ("   Estourou" if not process.MetDeadline else "") )        
            print("----------------------------")

        
        print("TotalTime : ")
        print(TotalTime)
        print("----------------------------------")
        

        print("Turnaround : ")
        print(self.TurnAround(CopyArray))
        print("----------------------------------")
        return



if __name__ == "__main__":
    ProcessA = Process.process(0,4,7,0,0)
    ProcessB = Process.process(2,2,3,0,0)
    ProcessC = Process.process(4,1,5,0,0)
    ProcessD = Process.process(6,3,10,0,0)


    ProcessArray = np.array([ProcessA,ProcessB,ProcessC,ProcessD,])

    a = ProcessScheduler(2 , 1)

    #a.FIFO(ProcessArray)

    #a.Sjf(ProcessArray)

    #a.RoundRobin(ProcessArray)

    a.Edf(ProcessArray)