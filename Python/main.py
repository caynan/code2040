import re
import solver
from code2040_client import ClientAPI


def get_email():
    EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    email = ''
    while not EMAIL_REGEX.match(email):
        email = raw_input('Please Insert a Valid Email: ')

    return email


def get_github():
    URL_REGEX = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')

    github = ''
    while not URL_REGEX.match(github):
        github = raw_input('Please Insert your github repo: ')

    return github


def get_token(api):
    email = get_email()
    github = get_github()
    token = api.register(email, github)

    return token


def phaseI(api, token):
    print 'Solving Phase I...'
    data = api.get_reverse_string(token)
    solve = solver.solve_reverse_string(data)
    api.post_reverse_string(token, solve)
    print 'Phase I, Solved!!'


def phaseII(api, token):
    print 'Solving Phase II'
    data = api.get_haystack(token)
    solve = solver.solve_haystack(data)
    api.post_haystack(token, solve)
    print 'Phase II, Solved!!'

def phaseIII(api, token):
    print 'Solving Phase III'
    data = api.get_prefix(token)
    solve = solver.solve_prefix(data)
    api.post_prefix(token, solve)
    print 'Phase III, Solved!!'

def phaseIV(api, token):
    print 'Solving Phase IV'
    data = api.get_dating(token)
    solve = solver.solve_dating(data)
    api.post_dating(token, solve)
    print 'Phase IV, Solved!!'



def main():
    api = ClientAPI()

    # Request user for email/github and get token
    token = get_token(api)

    # Solve Phases and return result in all
    ## Phase I:
    phaseI(api, token)

    ## Phase II:
    phaseII(api, token)

    ## Phase III:
    phaseIII(api, token)

    ## Phase IV
    phaseIV(api, token)

    ## Status
    print api.get_status(token)

if __name__ == '__main__':
    main()
