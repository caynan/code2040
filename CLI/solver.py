from datetime import datetime, timedelta

def solve_reverse_string(to_reverse):
    ans = {'string': to_reverse[::-1]}

    return ans

def solve_haystack(input_dictionary):
    needle = input_dictionary['needle']
    haystack = input_dictionary['haystack']

    # It's guranteed that there is a needle on the haystack
    index = haystack.index(needle)

    ans = {'needle': index}

    return ans

def solve_prefix(input_dictionary):
    prefix = input_dictionary['prefix']
    array = input_dictionary['array']

    array = [string for string in array if not string.startswith(prefix)]

    ans = {'array': array}

    return ans

def solve_dating(input_dictionary):
    datestamp = input_dictionary['datestamp']
    interval = input_dictionary['interval']

    # Convert data to datetime format
    datestamp = datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
    interval = timedelta(0, interval)

    # Calculate & format answer
    ans = datestamp + interval
    ans = ans.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    ans = {'datestamp': ans}

    return ans
