class process:
    StartTime = 0
    ExecutingTime = 0
    Deadline = -1
    Priority = False

    def __init__(self, StartTime, ExecutingTime, Deadline, Priority ):
        self.StartTime = StartTime
        self.ExecutingTime = ExecutingTime
        self.Deadline = Deadline
        self.Priority = Priority

