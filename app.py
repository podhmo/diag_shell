from util.gensym import UniqPath
from util.dummy import DummyOption

def make_application(_options):
    import blockdiag
    import blockdiag.parser
    import blockdiag.drawer
    import blockdiag.builder
    from blockdiag.utils.bootstrap import Application

    class DummyApplication(Application):
        options = _options
        module = blockdiag
        def parse_diagram(self, string):
            return self.module.parser.parse_string(string)

        def run(self, string):
            self.create_fontmap()
            return self.build_diagram(self.parse_diagram(string))
    return DummyApplication()

class DiagShell(object):
    def __init__(self, filename, option):
        self.option = option
        self.filename = filename

    def _filename(self):
        filename = self.filename
        if callable(filename):
            filename = filename()
        return filename

    def eval(self, string):
        filename = self._filename()
        self.option.output = filename
        app = make_application(self.option)
        app.run(string)
        return filename

uniq_path = UniqPath(suffix=".png")
shell = DiagShell(uniq_path.generate, DummyOption())
shell.eval(u"diagram { a -> b;}")
