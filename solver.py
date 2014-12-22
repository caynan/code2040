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
