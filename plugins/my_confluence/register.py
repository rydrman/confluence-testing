import urllib

from pants.backend.docgen.targets.doc import Wiki
from pants.backend.docgen.tasks.confluence_publish import ConfluencePublish

from pants.build_graph.build_file_aliases import BuildFileAliases
from pants.goal.task_registrar import TaskRegistrar as task


def confluence_url_builder(page, config):

    title = config['title']

    url = 'https://somewhere.atlassian.net/wiki/%s/%s' % (
        config['space'],
        urllib.quote_plus(title))

    return title, url


confluence_wiki = Wiki(
    name='confluence',
    url_builder=confluence_url_builder
)


def build_file_aliases():

    return BuildFileAliases(

        objects={'confluence': confluence_wiki},

    )


class MyConfluence(ConfluencePublish):

    def wiki(self):

        return confluence_wiki

    def api(self):

        return 'confluence2'


def register_goals():

    task(
        name='confluence',
        action=MyConfluence,
    ).install()
