from pecan import expose, redirect
from webob.exc import status_map

import wsme.pecan
from wsme.types import Base


class Pair(Base):
    left = unicode
    right = unicode

    def __init__(self, *args, **kwds):
        print 'Pair', args, kwds
        super(Pair, self).__init__(*args, **kwds)


class RootController(object):

    @expose(generic=True, template='index.html')
    def index(self):
        return dict()

    @index.when(method='POST')
    def index_post(self, q):
        redirect('http://pecan.readthedocs.org/en/latest/search.html?q=%s' % q)

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)

    @wsme.pecan.wsexpose([unicode], [unicode])
    def strings(self, input):
        return input

    @wsme.pecan.wsexpose([Pair], [Pair])
    def pairs(self, input):
        return input
