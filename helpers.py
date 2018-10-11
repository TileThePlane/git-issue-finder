from inspect import isfunction
from time import mktime, strptime

def repr_wrap(v):
    if isfunction(v):
        return v.__doc__

    return v

def convert_date_str_to_epoch(date_time):
    print(date_time)
    pattern = '%Y-%m-%d %H:%M:%S'
    return int(mktime(strptime(date_time, pattern)))