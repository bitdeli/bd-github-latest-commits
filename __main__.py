from bitdeli import profiles, set_theme, Title, Description
from bitdeli.widgets import Timeline, gravatar_hash
from itertools import starmap
import re

REPO = re.compile('https://api.github.com/repos/(.*?/.*?)/git')
NUM_ITEMS = 20

text = {}

set_theme('space')

def commits():
    for profile in profiles():
        for commit in profile['commits']:
            c = commit['commit']
            if 'repo' not in text:
                text['repo'] = REPO.search(c['tree']['url']).group(1)
            yield c['committer']['date'],\
                  c['committer']['name'],\
                  c['committer'].get('email', ''),\
                  c['message']

def entry(datestr, name, email, msg):
    if 'newest' not in text:
        text['newest'] = datestr.replace('T', ' ').replace('Z', '')
    return {'gravatar_hash': gravatar_hash(email),
            'username': name,
            'message': msg,
            'timestamp': datestr}

Timeline(size=(12, 12),
         data=list(starmap(entry, sorted(commits(), reverse=True)[:NUM_ITEMS])))

Title('Latest commits in {repo}'.format(**text))
Description('Newest commit pushed at {newest}'.format(**text))