from models.base import Base

'''
Issue defined: https://github.com/TileThePlane/git-issue-finder/issues/1

Example issues search: https://github.com/search?
    q=archived%3Afalse+user%3Anasa+user%3Adefense-cyber-crime-center+user%3Agsa+is%3Aopen+label%3A%22good+first+issue%22
    &type=Issues
    &l=python
'''

BASE_URL = 'https://github.com/search?'

class URL(Base):

    language = ['Language(s) to be searched for.']
    is_archived = 'Flag to included archived issues. Default false; to not return archived issues.'
    is_open = 'Flag to included open or closed issues. Dafault True; to return open issues'
    users = ['Includ issues created for projects belonging to some user(s).']
    labels = ['Include issues with some label(s).']
    page = 'Tracks current results page.'

    def __init__(self, languages=[], users=[], labels=[], is_open=True, is_archived=False, page=1):
        self.languages = languages
        self.users = users
        self.labels = labels
        self.is_archived = is_archived
        self.is_open = is_open
        self.page = page
        super(Base, self).__init__()

    def build_url(self):
        pass

print(URL().help())