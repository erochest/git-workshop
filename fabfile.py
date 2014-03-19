
from datetime import datetime

from fabric.api import lcd, local, task


THEME = 'solarized'


@task
def build():
    local(
        'pandoc '
        '--smart '
        '--to=revealjs '
        '--css=css/style.css '
        '--output=gh-pages/index.html '
        '--standalone '
        '--slide-level=2 '
        '-V theme={} '
        'git-workshop.md'.format(THEME)
        )


@task
def publish(msg=None):
    now = datetime.now()
    msg = msg or ('Published on {}.'.format(now.strftime('%c')))

    build()
    with lcd('gh-pages'):
        local('git checkout gh-pages')
        local('git add --all')
        local('git commit -m "{}"'.format(msg))
        local('git push')

    local('git add gh-pages')
    local('git commit -m "{}"'.format(msg))
    local('git push')

