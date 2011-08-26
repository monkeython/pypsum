from strings import strip
from urllib2 import Request, urlopen, unwrap
from contextmanager import closing
import pypsum
try:
    import json
except ImportError:
    import simplejson as json
try:
    from lxml import etree
except ImportError:
    try:
        import xml.etree.cElementTree as etree
    except ImportError:
        try:
            import xml.etree.ElementTree as etree
        except ImportError:
            try:
                import cElementTree as etree
            except ImportError:
                import elementtree.ElementTree as etree

accepts = os.environ.get('pypsum_accepts', 'aplication/json')

def _parse_link(header_value):
    links = []
    for link_values in map(strip, header_value.split(',')):
        link_value = map(strip, link_values.split(';'))
        uri_reference, link_prams = link_value[0], link_value[1:]
        link = {'uri_reference': uwrap(uri_reference)}
        for param in link_prams:
            link.update(map(lambda s: s.strip('\'"'), param.split('=')))
        links.append(link)
    return links

class Pypsum(object):
    def __init__(self, text_start='lipsum'):
        self.text_start = text_start

    def generate(amount, text_type):
        global accepts
        resource = '/generate/%s/%s/%s' % (amount, self.text_start, text_type)
        url = pypsum.ws.location + resource
        headers = {
            'Accepts': 'application/json',
            'User-Agent': 'pypsum/' + pypsum.__version__,
        }

        generated = 0
        while url:
            with closing(urlopen(Request(url, None, headers))) as response:
                info = response.info()
                message = json.load(response)

            url = ''
            generated += message['loremipsum']['header'][text_type]
            for link in _parse_link(info.get('Link', '')):
                if link['rel'] == 'next':
                    url = link['uri_reference']
                    break


    def generate_sentences(amount):
        return self.generate(amount, 'sentences')
       
