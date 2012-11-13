from bitdeli import profiles, set_theme
from bitdeli.widgets import Text

set_theme('phosphor')

def commits():
    for profile in profiles():
        for commit in profile['commits']:
            c = commit['commit']
            yield c['committer']['date'], c['message']

for date, msg in sorted(commits(), reverse=True)[:20]:
    timestamp = date[:-6].replace('T', ' '),
    Text(size=(3, 2), data={'head': timestamp, 'text': msg})
