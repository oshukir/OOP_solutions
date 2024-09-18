def make_class(*attrs):
    class Class(object):
        def __init__(self, *args):
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)
    return Class