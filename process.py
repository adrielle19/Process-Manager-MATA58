class process:
    def __init__(self, StartTime, ExecutingTime, Deadline, Priority, MemoryPages ):
        self.StartTime = StartTime
        self.ExecutingTime = ExecutingTime
        self.Deadline = Deadline
        self.Priority = Priority
        self.MemoryPages = MemoryPages
        self.MemorySize = 4 # mudar para 4098 ?

