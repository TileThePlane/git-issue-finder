from models.base import Base
from constants import LANGUAGES, DEFAULT_LABELS
from pprint import pprint

'''
Issue defined: https://github.com/TileThePlane/git-issue-finder/issues/1

Example issues search: https://github.com/search?
    q=archived%3Afalse+user%3Anasa+user%3Adefense-cyber-crime-center+user%3Agsa+is%3Aopen+label%3A%22good+first+issue%22
    &type=Issues
    &l=python
'''

BASE_URL = 'https://github.com/search?'

class IssueSearch(Base):

    language = ['Language(s) to be searched for.']
    is_archived = 'Flag to include archived issues. Default false; to not return archived issues.'
    is_open = 'Flag to include open or closed issues. Default True; to return open issues'
    users = ['Include issues created for projects belonging to some user(s).']
    orgs = ['Include issues created for projects belonging to some org(s) or org group.']
    labels = ['Include issues with some label(s).']
    page = 'Tracks current results page.'
    type = 'Choose pr or issue or pr and issue. Default to show both pr and issues.'

    def __init__(self, languages=[], users=[], orgs=[],labels=[], is_open=True, is_archived=False, page=1, type='issueandpr'):
        self.languages = languages
        self.users = users
        self.orgs = orgs
        self.labels = labels
        self.is_archived = is_archived
        self.is_open = is_open
        self.page = page
        self.type = type
        super(Base, self).__init__()

    @staticmethod
    def show_languages():
        '''
        Print list of searchable languages
        '''

        print('You may try searching for a language from the list.')

        for language in LANGUAGES.keys():
            print(language)

    def set_language_search_term(self, language):
        '''
        If the language is listed keep the searchable string or else try searching with the user input.

        :param language: User input language.
        '''

        try:
            self.languages.append(LANGUAGES[language])
        except KeyError:
            return self.languages.append(language)

    @staticmethod
    def show_default_labels():
        '''
        Print list of commonly used labels
        '''

        print('For reference here is a list of the most common labels used for github issues.')

        for k,v in DEFAULT_LABELS.items():
            print('{} : {}'.format(k,v))

    def set_user_label(self, label):
        '''
        If the label is listed keep the searchable string or else try searching with the user input.

        :param label: User input label.
        '''

        try:
            self.labels.append(LANGUAGES[label])

        except KeyError:
            return self.labels.append(label)

print(IssueSearch().to_dict())
