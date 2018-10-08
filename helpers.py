from inspect import isfunction

def repr_wrap(v):
    if isfunction(v):
        return v.__doc__

    return v