import blockdiag
import blockdiag.parser
import blockdiag.drawer
import blockdiag.builder
from util.dummy import DummyOption
from blockdiag.utils.bootstrap import Application

class DummyApplication(Application):
    module = blockdiag

    def __init__(self, options):
        self.options = options

    def parse_diagram(self, string):
        return self.module.parser.parse_string(string)
    
    def run(self, string):
        self.create_fontmap()
        return self.build_diagram(self.parse_diagram(string))

class CommandMixin(object):
    def blockdiag(self, string):
        return self.app.run(string)

class DiagShell(CommandMixin):
    def __init__(self, app):
        self.app = app

app = DummyApplication(DummyOption())
import extend
app = extend.extend(app)
shell = DiagShell(app)

shell.blockdiag(u"diagram { a -> b;}")

