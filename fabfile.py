
from datetime import datetime

from fabric.api import lcd, local, task


@task
def build():
    local(
        'pandoc '
        '--smart '
        '--to=revealjs '
        '--output=gh-pages/index.html '
        '--standalone '
        '--slide-level=2 '
        '-V theme=moon '
        'git-workshop.md'
        )


@task
def publish(msg=None):
    now = datetime.now()
    msg = msg or ('Published on {}.'.format(now.strftime('%c')))

    build()
    with lcd('gh-pages'):
        local('git add --all')
        local('git commit -m "{}"'.format(msg))
        local('git push')

    local('git add gh-pages')
    local('git commit -m "{}"'.format(msg))
    local('git push')

