import copy
from src.summary_builder import build_summary_object
from src.participant_builder import build_participant_object
from src.meeting import Meeting

def build_meeting_object(raw_meeting: dict):
    raw = copy.deepcopy(raw_meeting)
    participants = raw.pop('Participants', None)
    new_participants = []
    for participant in participants:
        new_participants.append(build_participant_object(participant))
    new_summaray = build_summary_object(raw)
    return Meeting(new_summaray, new_participants)