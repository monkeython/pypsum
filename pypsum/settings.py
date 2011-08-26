import loremipsum
import os

# Default settings
NAME = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
WORDS_CAPACITY = 50
SENTENCES_CAPACITY = 10
PARAGRAPHS_CAPACITY = 5
DEBUG = True
TESTING = True
PROPAGATE_EXCEPTIONS = False
PRESERVE_CONTEXT_ON_EXCEPTION = True
SECRET_KEY = ''
SESSION_COOKIE_NAME = NAME
PERMANENT_SESSION_LIFETIME = 0
USE_X_SENDFILE = False
LOGGER_NAME = NAME
# SERVER_NAME = 'localhost'
MAX_CONTENT_LENGTH = 0
GENERATOR = loremipsum.Generator()

# Specialized settings objects
class Testing(object):
    TESTING = True

class Debug(Testing):
    DEBUG = True

class AppSpot(object):
    pass

