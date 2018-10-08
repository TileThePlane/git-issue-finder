from datetime import datetime

from helpers import repr_wrap

class Base(object):

    create_time = 'The utctime that the object was created.'

    def __init__(self):
        self.created_time = str(datetime.utcnow())

    def to_dict(self):
        '''
        Generate a dictionary of class attributes
        '''
        return vars(self)

    def help(self):
        '''
        Generate helpful information for class features
        '''
        return { k : repr_wrap(v) for k, v in self.__class__.__dict__.items() if '__' not in k }
