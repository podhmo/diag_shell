import json

class JSexpEvalWay(object):
    def __init__(self, env):
        self.env = env

    def parse(self, value):
        tree = json.loads(value)
        return tree

    def eval(self, method, args):
        params = [method]
        for e in args:
            params.append(self.apply(e))
        return self.apply(params)

    def apply(self, params):
        if isinstance(params, list):
            method, args = params[0], params[1:]
            return getattr(self.env, method)(*args)
        else:
            return params

class Env(object):
    def add(self, x, y):
        return x + y

class EvalatorFactory(object):
    def __init__(self, way, env):
        self.evalator = way(env)

    def eval(self, expr):
        tree = self.evalator.parse(expr)
        return self.evalator.eval(tree[0], tree[1:])

ea = EvalatorFactory(JSexpEvalWay, Env())
print ea.eval(json.dumps(["add", 1, 2]))
print ea.eval(json.dumps(["add", ["add", 10, 30], 2]))

