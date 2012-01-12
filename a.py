import blockdiag
import blockdiag.parser
import blockdiag.drawer
import blockdiag.builder
from blockdiag.utils.fontmap import FontMap
from blockdiag.utils.bootstrap import Application
from blockdiag.utils.bootstrap import create_fontmap
import util.dummy as ud

class DummyOption(ud.DummyConfig):
    default  =  dict(type = "png", 
                     output = "dummy.png", 
                     fontmap = None, 
                     antialias = False, 
                     nodoctype = False, 
                     font = []
                     )
    

FONT = ["/usr/share/fonts/truetype/ttf-japanese-gothic.ttf"]

class DummyApplication(Application):
    options = DummyOption(output="b.png", font=FONT)
    module = blockdiag
    def parse_diagram(self, string):
        return self.module.parser.parse_string(string)

    def run(self, string):
        self.create_fontmap()
        return self.build_diagram(self.parse_diagram(string))
        
DummyApplication().run(u"diagram { a -> b;}")
