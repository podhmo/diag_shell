import copy
__all__ = ["DummyConfig"]

class DummyConfig(object):
    default = {}
    def validate(self, config):
        return True

    def __init__(self, **params):
        config = copy.copy(self.default)
        config.update(params)
        if not self.validate(config):
            raise Exception
        bind(self, config)

def bind(obj, config):
    for k, v in config.items():
        setattr(obj, k, v)
    return obj
