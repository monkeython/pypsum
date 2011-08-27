from pypsum.application import pypsum
from google.appengine.ext.webapp.util import run_wsgi_app
if __name__ == '__main__':
    run_wsgi_app(pypsum)
