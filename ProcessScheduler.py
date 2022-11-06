import process
import numpy as np

class ProcessScheduler:
    
    ExecutingProcess = None

    def __init__(self, Quantum, Overload):
        self.Quantum = Quantum
        self.Overload = Overload


    # Escalonamento
    def FIFO(ProcessArray):

        WorkingArray = np.array([]) 

        for process in ProcessArray: # copia pq python é so por referencia
            WorkingArray = np.append(WorkingArray, process.clone() )


        print("ProcessList por startime : ")

        for process in WorkingArray:
            print(process.StartTime)
        print("----------------------------------")

        SortedList = np.array([])

        # ordena valors por ordem de chegada. É n^2 ,podia ser quicksort para objetos em array mas fiquei com pregruiça 
        # talvez nao necessario,
        while WorkingArray.size != 0:
            smallest = WorkingArray[0]
            
            for process in WorkingArray:
                if process.StartTime < smallest.StartTime:
                    smallest = process

            WorkingArray = np.delete(WorkingArray, np.where(WorkingArray == smallest))
            SortedList = np.append(SortedList,smallest) 

        print("SortedList por startime : ")
        for process in SortedList:
            print(process.StartTime)
        print("----------------------------------")

        TotalTime = 0
        ReadyList = np.array([])

        ProcessCount = SortedList.size

        #execuçao dos processos
        while ProcessCount != 0:
            
            #adiciona a lista de prontos caso o tempo de chegada seja menor que o de execuçao
            for process in SortedList:
                if process.StartTime <= TotalTime:
                    ReadyList = np.append(ReadyList,process) 
                    SortedList = np.delete(SortedList, 0)

            #passagem de tempo para o 1° processo ja que é o fifo
            TotalTime += 1
            try:
                ExectuingProcess = ReadyList[0]
                ExectuingProcess.ExecutedTime += 1

                #remove caso tenha terminado de ser executado
                if ExectuingProcess.ExecutedTime == ExectuingProcess.ExecutingTime:
                    ReadyList = np.delete(ReadyList, np.where(ReadyList == ExectuingProcess))
                    ProcessCount -= 1

                #Tempo de espera para calculo de turnaround
                for process in ReadyList:
                    if process == ExectuingProcess:
                        continue
                    process.WaitTime += 1
            except:
                ExectuingProcess = None

            
        print("TotalTime : ")
        print(TotalTime)
        print("----------------------------------")
        return


    def Sjf(ProcessArray):
        WorkingArray = np.array([]) 

        for process in ProcessArray: # copia pq python é so por referencia
            WorkingArray = np.append(WorkingArray, process.clone() )

        ReadyList = np.array(WorkingArray)
        TotalTime = 0
        ProcessCount = WorkingArray.size
        ExectuingProcess = None

        #execuçao dos processos
        while ProcessCount != 0:
            #Escolhe o proximo
            for process in ReadyList:
                if process.StartTime <= TotalTime and (not process.Done): # so escolhe o proximo caso alguem ja tenho chegado
                    if ExectuingProcess == None:
                        ExectuingProcess = process
                    else:
                        if process.ExecutingTime - process.ExecutedTime  < ExectuingProcess.ExecutingTime - ExectuingProcess.ExecutedTime:
                            ExectuingProcess = process

            TotalTime += 1
            try:
                ExectuingProcess.ExecutedTime += 1

                if ExectuingProcess.ExecutedTime == ExectuingProcess.ExecutingTime:
                        ExectuingProcess.Done = True
                        ReadyList = np.delete(ReadyList, np.where(ReadyList == ExectuingProcess))
                        ExectuingProcess = None
                        ProcessCount -= 1
            except:
                pass
            #Tempo de espera para calculo de turnaround
            for process in ReadyList:
                if (process == ExectuingProcess) or (process.StartTime >= TotalTime):
                    continue
                process.WaitTime += 1


            for process in WorkingArray:
                print("Chegada: " +str(process.StartTime)+ " Job: " +str(process.ExecutingTime) + " Tempo executado : "+ str(process.ExecutedTime) + " Tempo de Espera : " + str(process.WaitTime) + " ProcessCount: " + str(ProcessCount))        
            print("----------------------------")
        
        print("TotalTime : ")
        print(TotalTime)
        print("----------------------------------")
        Turnaround = 0
        for process in WorkingArray:
            Turnaround += process.WaitTime + process.ExecutingTime

        print("Turnaround : ")
        print(Turnaround/WorkingArray.size)
        print("----------------------------------")
        return


    def RoundRobin():
        return

    def Edf():
        return