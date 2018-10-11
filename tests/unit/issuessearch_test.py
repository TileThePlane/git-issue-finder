from models.issuesearch import IssueSearch
from tests.unit.base_test import BaseTest

class IssueSearch(BaseTest):

    def test_help(self):
        issue_search = IssueSearch()
        print(IssueSearch().help())

        self.assertEqual(IssueSearch().help(), {'language': ['Language(s) to be searched for.'],
            'is_archived': 'Flag to include archived issues. Default false; to not return archived issues.',
            'is_open': 'Flag to include open or closed issues. Default True; to return open issues',
            'users': ['Include issues created for projects belonging to some user(s).'],
            'orgs': ['Include issues created for projects belonging to some org(s) or org group.'],
            'labels': ['Include issues with some label(s).'],
            'page': 'Tracks current results page.',
            'type': 'Choose pr or issue or pr and issue. Default to show both pr and issues.',
            'show_languages': 'staticmethod(function) -> method\n\nConvert a function to be a static method.\n\nA static method does not receive an implicit first argument.\nTo declare a static method, use this idiom:\n\n     class C:\n         @staticmethod\n         def f(arg1, arg2, ...):\n             ...\n\nIt can be called either on the class (e.g. C.f()) or on an instance\n(e.g. C().f()).  The instance is ignored except for its class.\n\nStatic methods in Python are similar to those found in Java or C++.\nFor a more advanced concept, see the classmethod builtin.', 'set_language_search_term': '\n        If the language is listed keep the searchable string or else try searching with the user input.\n\n        :param language: User input language.\n        ',
            'set_language_search_term': '\n        If the language is listed keep the searchable string or else try searching with the user input.\n\n        :param language: User input language.\n        ',
            'show_default_labels': 'staticmethod(function) -> method\n\nConvert a function to be a static method.\n\nA static method does not receive an implicit first argument.\nTo declare a static method, use this idiom:\n\n     class C:\n         @staticmethod\n         def f(arg1, arg2, ...):\n             ...\n\nIt can be called either on the class (e.g. C.f()) or on an instance\n(e.g. C().f()).  The instance is ignored except for its class.\n\nStatic methods in Python are similar to those found in Java or C++.\nFor a more advanced concept, see the classmethod builtin.', 'set_language_search_term': '\n        If the language is listed keep the searchable string or else try searching with the user input.\n\n        :param language: User input language.\n        ',
            'set_user_label': '\n        If the label is listed keep the searchable string or else try searching with the user input.\n\n        :param label: User input label.\n        '})

    def test_to_dict(self):
        issue_search = IssueSearch()

        self.assertEqual(issue_search.to_dict(), {'languages': [],
                          'users': [],
                          'orgs': [],
                          'labels': [],
                          'is_archived': False,
                          'is_open': True,
                          'page': 1,
                          'type': 'issueandpr'} )
