from code2040_client import ClientAPI

def solve_reverse_string(to_reverse):
    ans = {'string': to_reverse[::-1]}

    return ans

def solve_haystack(input_dictionary):
    needle = input_dictionary['needle']
    haystack = input_dictionary['haystack']

    index = None
    if needle in haystack:
        index = haystack.index(needle)

    ans = {'needle': index}

    return ans

def solve_prefix(input_dictionary):
    prefix = input_dictionary['prefix']
    array = input_dictionary['array']

    array = [string for string in array if not string.startswith(prefix)]

    ans = {'array': array}

    return ans
