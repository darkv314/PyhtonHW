from os import listdir
from os.path import isfile, join
from datetime import datetime
import csv
import copy


STR_TO_DATE = '%m/%d/%y, %I:%M:%S %p'
DATE_TO_STR = '%m/%d/%y, %#I:%M:%S %p'
TIME_TO_STR = '%#Ih %Mm %Ss'


def discover_data_files(path='../data', pattern='csv'):
    return [join(path, f) for f in listdir(path) if isfile(join(path, f)) and f.endswith('csv')]


def read_file(files):
    readers = []
    for  f in files:
        csv_file = open(f, encoding='UTF-16')
        readers.append((f, csv.reader(csv_file, delimiter='\t')))
    return readers

def obtain_key(key_word, keys):
    key_result = [key for key in keys if key_word in key.lower()]
    if key_result:
        return key_result[0]
    if not key_result:
        return None

def obtain_keys(key_words, keys, optional):
    data_keys = []
    optional_value = obtain_key(optional, keys)
    for key in key_words:
        data_keys.append(obtain_key(key, keys) or optional_value)
    if data_keys:
        return data_keys

def get_new_value(value, type):
    if type == 'int':
        return int(value)
    elif type == 'date':
        return datetime.strptime(value, STR_TO_DATE)
    else: 
        return value

def get_time(time):
    if type(time) is dict:
        return copy.deepcopy(time)
    time = time.split()
    duration = {
        'Hours': 0,
        'Minutes': 0,
        'Seconds': 0
    }
    for value in time:
        if value.endswith('h'):
            duration['Hours']=int(value[:-1])
        elif value.endswith('m'):
            duration['Minutes']=int(value[:-1])
        else:
            duration['Seconds']=int(value[:-1])
    return duration

def dict_builder(key_words, data, data_keys):
    if len(key_words) == len(data_keys):
        new_dict = {}
        for index, value in enumerate(data_keys):
            new_value = get_new_value(data[value], key_words[index][1])
            new_dict[key_words[index][0]] = new_value
        return new_dict
