'Capital example'
def capital_case(x):
    'Function example'
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()
