class Atendance:
    '''Attendance is a Meeting ocurrence, it has a summary and a list of participants.'''

    def __init__(self, start_datetime, summary=None, participants=list()):
        self.start_datetime = start_datetime
        self.summary = summary
        self.participants = participants

    def add_participants(self, participants):
        self.participants += participants
