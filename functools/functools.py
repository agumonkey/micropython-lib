def partial(func, *args, **kwargs):
    def _partial(*more_args, **more_kwargs):
        kw = kwargs.copy()
        kw.update(more_kwargs)
        func(*(args + more_args), **kw)
    return _partial


def update_wrapper(wrapper, wrapped):
    # Dummy impl
    return wrapper

def wraps(wrapped):
    def _(new):
        def __(*p, **k):
            return new(*p, **k)
        new.__doc__ == wrapped.__doc__
        new.__name__ == wrapped.__name__
        return __
    return _

