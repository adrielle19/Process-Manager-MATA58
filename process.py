class process:
    StartTime = 0
    ExecutingTime = 0
    Deadline = -1
    Priority = False

    def __init__(self, StartTime, ExecutingTime, Deadline, Priority ):
        self.StartTime = StartTime
        self.ExecutingTime = ExecutingTime
        self.ExecutedTime = 0
        self.WaitTime = 0
        self.Deadline = Deadline
        self.Priority = Priority

    def clone(self):
        proc = process()
        proc.StartTime = self.StartTime
        proc.ExecutingTime = self.ExecutingTime
        proc.ExecutedTime = self.ExecutedTime
        proc.WaitTime = self.WaitTime
        proc.Deadline = self.Deadline
        proc.Priority = self.Priority
        proc.MemoryPages = self.MemoryPages
        proc.MemorySize = self.MemorySize
        return proc
