from src.helpers import STR_TO_DATE, obtain_keys, dict_builder
from src.summary import Summary
from src.duration import Duration
from datetime import datetime

def normalize_summary_keys(raw_data):
    if raw_data:
        keys = raw_data.keys()
        key_words = ['title', 'id', 'participants', 'start time', 'end time']
        data_keys = obtain_keys(key_words, keys, 'title')
        key_words = [('Title', 'str'), ('Id', 'str'), ('Attended participants', 'int'), 
        ('Start Time', 'str'), ('End Time', 'str')]
        # participants_key = obtain_key('participants', keys)
        # start_key = obtain_key('start time', keys)
        # end_key = obtain_key('end time', keys)
        # title_key = obtain_key('title', keys)
        # id_key = obtain_key('id', keys)
        norm_summaray = dict_builder(key_words, raw_data, data_keys)
        # norm_summaray['Title'] = raw_data[data_keys[0]]
        # norm_summaray['Id'] = raw_data[data_keys[1] or data_keys[0]]
        # norm_summaray['Attended participants'] = int(raw_data[data_keys[2]])
        # norm_summaray['Start Time'] = raw_data[data_keys[3]]
        # norm_summaray['End Time'] = raw_data[data_keys[4]]
        start_date = datetime.strptime(norm_summaray['Start Time'], STR_TO_DATE)
        end_date = datetime.strptime(norm_summaray['End Time'], STR_TO_DATE)
        res_time = end_date - start_date
        norm_summaray['Duration'] = {}
        norm_summaray['Duration']['hours'] = res_time.seconds//3600
        norm_summaray['Duration']['minutes'] = (res_time.seconds//60)%60
        norm_summaray['Duration']['seconds'] = res_time.seconds%60
        return norm_summaray
        

def build_summary_object(raw_data):
    norm_data = normalize_summary_keys(raw_data)
    duration = norm_data['Duration']
    norm_data['Duration'] = Duration(duration['hours'], duration['minutes'], duration['seconds'])
    return Summary(*norm_data.values())
