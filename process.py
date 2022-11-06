class process:
    def __init__(self, StartTime = 0, ExecutionTime = 0, Deadline = 0, Priority = 0, MemoryPages = 0 ):
        self.StartTime = StartTime
        self.ExecutionTime = ExecutionTime
        self.ExecutedTime = 0
        self.ExecutionTimePerQuantum = 0
        self.WaitTime = 0
        self.Deadline = Deadline
        self.Priority = Priority
        self.MemoryPages = MemoryPages
        self.MemorySize = 4 # mudar para 4098 ?
        self.MetDeadline = True

    def clone(self):
        proc = process()
        proc.StartTime = self.StartTime
        proc.ExecutionTime = self.ExecutionTime
        proc.ExecutedTime = self.ExecutedTime
        proc.ExecutionTimePerQuantum = self.ExecutionTimePerQuantum
        proc.WaitTime = self.WaitTime
        proc.Deadline = self.Deadline
        proc.Priority = self.Priority
        proc.MemoryPages = self.MemoryPages
        proc.MemorySize = self.MemorySize
        proc.MetDeadline = self.MetDeadline
        return proc
