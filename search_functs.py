import dicts
def get_by_social(nested_dict, value, prepath=()):
    for k, v in nested_dict.items():
        path = prepath + (k,)
        if v == value: # found value
            return path
        elif hasattr(v, 'items'): # v is a dict
            p = get_by_social(v, value, path) # recursive call
            if p is not None:
                return p





