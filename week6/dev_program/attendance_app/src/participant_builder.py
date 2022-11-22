from src.helpers import obtain_keys, dict_builder, get_time, STR_TO_DATE, DATE_TO_STR, TIME_TO_STR
from datetime import datetime, timedelta
from src.duration import Duration
from src.participant import Participant
import copy

KEYS = ['Full Name', 'Join time', 'Leave time', 
    'In-meeting Duration', 'Email', 'Role', 
    'Participant ID (UPN)']

def get_first_last_duration(raw_participants):
    first = datetime(9999, 1, 1)
    last = datetime(1, 1, 1)
    duration = timedelta(seconds=0)
    for participant in raw_participants:
        keys = participant.keys()
        join_key, leave_key, duration_key = obtain_keys(['join time', 'leave time', 'duration'], keys, 'join time')
        new_join = datetime.strptime(participant[join_key], STR_TO_DATE)
        new_last = datetime.strptime(participant[leave_key], STR_TO_DATE)
        if new_last > last:
            last = new_last 
        if new_join < first:
            first = new_join
        new_duration = get_time(participant[duration_key])
        duration += timedelta(seconds=new_duration['Hours']*3600+new_duration['Minutes']*60+new_duration['Seconds'])
    duration = (datetime.min + duration).time()
    return first, last, duration


def normalize_participant(raw: dict):
    if list(raw.keys()) ==  KEYS:
        return copy.deepcopy(raw)
    keys = raw.keys()
    key_words = ["name", 'join time', 'leave time', 'duration', 'email', 'role', 'id']
    data_keys = obtain_keys(key_words, keys, 'email')
    key_words = [('Full Name', 'str'), ('Join time', 'str'), ('Leave time', 'str'), 
    ('In-meeting Duration', 'str'), ('Email', 'str'), ('Role', 'str'), 
    ('Participant ID (UPN)', 'str')]
    norm_participant = dict_builder(key_words, raw, data_keys)
    norm_participant['In-meeting Duration'] = get_time(norm_participant['In-meeting Duration'])
    return norm_participant

def resolve_participant_join_last_time(raw_participants: dict):
    first, last, duration = get_first_last_duration(raw_participants)
    str_duration = ''
    if duration.hour != 0:
        str_duration += f'{str(duration.hour)}h '
    if duration.minute != 0:
        str_duration += f'{str(duration.minute)}m '
    if duration.second != 0:
        str_duration += f'{str(duration.second)}s'
    if str_duration.endswith(' '):
        str_duration = str_duration[:-1]
    resolved_participant = normalize_participant(raw_participants[0])
    resolved_participant['Join time'] = datetime.strftime(first, DATE_TO_STR)
    resolved_participant['Leave time'] = datetime.strftime(last, DATE_TO_STR)
    resolved_participant['In-meeting Duration'] = str_duration
    key_words = [('Name', 'str'), ('First Join time', 'str'), ('Last Leave time', 'str'), 
    ('In-meeting Duration', 'str'), ('Email', 'str'), ('Role', 'str'), 
    ('Participant ID (UPN)', 'str')]
    return dict_builder(key_words, resolved_participant, resolved_participant.keys())
    

def build_participant_object(raw: dict):
    norm_participant = normalize_participant(raw)
    if (norm_participant['Full Name'] is None or norm_participant['Join time'] is None
     or norm_participant['Leave time'] is None):
        raise ValueError('Full Name, Join time, Leave time cannot be None')
    else:
        duration = norm_participant['In-meeting Duration'] 
        norm_participant['In-meeting Duration'] = Duration(duration['Hours'], duration['Minutes'], duration['Seconds'])
        return Participant(*norm_participant.values())