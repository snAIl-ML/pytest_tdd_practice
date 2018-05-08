'Capital example'
def capital_case(xyz):
    'Function example'
    if not isinstance(xyz, str):
        raise TypeError('Please provide a string argument')
    return xyz.capitalize()
