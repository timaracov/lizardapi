class LizardAPI:
    def route(self, method: str, path: str = ""):
        def dec(func):
            def wrap(*args, **kwargs):
                return None
            return wrap
        return dec

    def mount_group(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        pass


class RouterGroup:
    def __init__(self, path: str):
        self.__path = path

    def route(self, method: str, path: str = ""):
        def dec(func):
            def wrap(*args, **kwargs):
                return None
            return wrap
        return dec

    def mount_group(self, *args, **kwargs):
        pass
