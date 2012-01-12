import uuid
import os

class UniqPath(object):
    def __init__(self, prefix="./", suffix=".dat"):
        self.prefix = prefix
        self.suffix = suffix

    def _has_suffix(self, string):
        return not os.path.splitext(string)[1] == ""
    
    def _add_suffix(self, generated):
        if self._has_suffix(generated):
            return generated
        else:
            return generated + self.suffix
        
    def generate(self):
        middle = uuid.uuid4().hex
        return self._add_suffix(os.path.join(self.prefix, middle))
