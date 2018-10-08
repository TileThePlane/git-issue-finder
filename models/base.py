from datetime import datetime


class Base():

    def __init__(self):
        self.created_time = str(datetime.utcnow())

    def to_dict(self):
        return vars(self)

base = Base().to_dict()
print(base)
