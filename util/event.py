__all__ = ["EventHook", "EevntWrapper"]
class EventHook(object):
    def __init__(self):
        self.events = []

    def register(self, thunk):
        self.events.append(thunk)
        
    def apply(self, obj, request):
        for ev in self.events:
            v = ev(obj, request)
            if v is not None:
                request = v
        return request

class EventWrapper(object):
    def __init__(self):
        self.before_hook = EventHook()
        self.after_hook = EventHook()

    def before(self, thunk):
        self.before_hook.register(thunk)

    def after(self, thunk):
        self.after_hook.register(thunk)
        
    def wrap(self, obj, method_name):
        def wrapped(request):
            request = self.before_hook.apply(obj, request)
            response = getattr(obj, method_name)(obj)
            response = self.after_hook.apply(obj, response)
            return response
        setattr(obj, method_name, wrapped)
        return obj
