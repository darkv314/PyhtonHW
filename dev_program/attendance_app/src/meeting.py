from src.summary import Summary
from src.participant import Participant

class Meeting:
    '''Encapsulates a Meeting definition.'''

    # def __init__(self, summary: Summary):
    #     self.attendance = list()
    #     self.id = summary.id
    #     self.title = summary.title
    #     self.summary = summary

    # def add_attendance(self, attendance):
    #     self.attendance += attendance

    def __init__(self, summary, participants: list[Participant]):
        self.id = summary.id
        self.title = summary.title
        self.summary = summary
        self.participants = participants

    def add_participant(self, participant):
        self.participants.append(participant)