from models.base import Base

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

    def build_url(self):
        pass


print(IssueSearch().help())