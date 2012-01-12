import blockdiag
import blockdiag.parser
import blockdiag.drawer
import blockdiag.builder
from blockdiag.utils.fontmap import FontMap
from blockdiag.utils.bootstrap import Application

from blockdiag.utils.bootstrap import create_fontmap

FONT = "/usr/share/fonts/truetype/ttf-japanese-gothic.ttf"
def option(_type="png", _output="dummy.png", _fontmap=None, _antialias=False, _nodoctype=False):
    class DummyOption(object):
        type = _type
        font = []
        output = _output
        fontmap = _fontmap
        antialias = _antialias
        nodoctype = _nodoctype
    return DummyOption

_option = option(_output="a.png")

class DummyApplication(Application):
    options = _option
    module = blockdiag
    def parse_diagram(self, string):
        return self.module.parser.parse_string(string)

    def run(self, string):
        self.create_fontmap()
        return self.build_diagram(self.parse_diagram(string))
        
DummyApplication().run(u"diagram { a -> b;}")
