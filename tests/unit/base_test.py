from datetime import datetime

from models.base import Base
from tests.unit.unit_base_test import UnitBaseTest
from helpers import convert_date_str_to_epoch

class BaseTest(UnitBaseTest):

    def test_to_dict(self):

        base = Base()

        self.assertAlmostEqual(convert_date_str_to_epoch(base.created_time),
                               convert_date_str_to_epoch(str(datetime.utcnow()).split('.')[0]))

    def test_help(self):

        base = Base()
        self.assertEqual(base.help(), {'created_time': 'The utctime that the object was created.',
                                       'to_dict': '\n        Generate a dictionary of class attributes\n        ',
                                       'help': '\n        Generate helpful information for class features\n        ' })

    def test_to_dict(self):

        base = Base()
        print(base.to_dict().keys())
        self.assertEqual(list(base.to_dict().keys()), ['created_time'])



