from util.gensym import UniqPath
from util.event import EventWrapper

def extend(app):
    wrapper = EventWrapper()
    uniq_path = UniqPath(suffix=".png")

    def rename(app, request):
        name = uniq_path.generate()
        app.options.rename(name)

    wrapper.before(rename)
    wrapper.wrap(app, "eval")
    return app

