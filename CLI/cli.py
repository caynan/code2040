# coding: utf-8
import click
import code2040
import solver
import six
import pickle
import os.path
from code2040_client import ClientAPI




# Controller Functions
def get_token(api, email, github):
    token = api.register(email, github)
    click.echo('\nyour API token is %s\n' % token['token'])

    return token

def get_status(api, token):
    status = api.get_status(token)
    if isinstance(status, six.string_types):
        click.echo(status)
    else:
        click.echo('\n')
        for key in status:
            if status[key]:
                click.echo(key)
        click.echo('\n')
    click.pause()


# Auxiliar Functions
def get_info(user_dict):
    email = user_dict['email']
    github = user_dict['github']
    token = user_dict['token']

    click.echo(
        '\n\tEmail: %s\n\tGithub: %s\n\tToken: %s\n' % (email, github, token)
    )
    click.pause()


# Persistence
## load info to `.code2040_data.p`
def load_user_data():
    user_data = {}
    if os.path.exists('.code2040_data.p'):
        user_data = pickle.load( open('.code2040_data.p', 'rb') )

    return user_data

## save info to `.code2040_data.p`
def save_user_data(user_data):
    pickle.dump( user_data, open('.code2040_data.p', 'wb') )


# Solve Problems
def __phaseI(api, token):
    click.echo('Solving Phase I...')
    data = api.get_reverse_string(token)
    solve = solver.solve_reverse_string(data)
    api.post_reverse_string(token, solve)
    click.echo('\tinput: %s\n\tsolution: %s\n' % (data, solve))


def __phaseII(api, token):
    click.echo('Solving Phase II')
    data = api.get_haystack(token)
    solve = solver.solve_haystack(data)
    api.post_haystack(token, solve)
    click.echo('\tinput: %s\n\tsolution: %s\n' % (data, solve))


def __phaseIII(api, token):
    click.echo('Solving Phase III')
    data = api.get_prefix(token)
    solve = solver.solve_prefix(data)
    api.post_prefix(token, solve)
    click.echo('\tinput: %s\n\tsolution: %s\n' % (data, solve))


def __phaseIV(api, token):
    click.echo('Solving Phase IV')
    data = api.get_dating(token)
    solve = solver.solve_dating(data)
    api.post_dating(token, solve)
    click.echo('\tinput: %s\n\tsolution: %s\n' % (data, solve))



@click.group()
def cli():
    """
    This scripts serves as a client for the CODE2040 API Challenge.

    Just Call `$ code2040 menu`
    """
    pass


@cli.command()
def menu():
    """ A simple menu to easily iterate over API """

    # Global Variables
    user = load_user_data()
    if user.has_key('token'):
        TOKEN = user['token']
    else:
        TOKEN = None

    API = ClientAPI()

    menu = 'main'
    while True:
        if menu == 'main':
            click.clear()
            if TOKEN is None:
                click.echo('Main menu:')
                click.echo('    r: get token')
                click.echo('    q: quit')
            else:
                click.echo('Main menu:')
                click.echo('    s: solve problems')
                click.echo('    g: get status')
                click.echo('    r: get token')
                click.echo('    i: get info')
                click.echo('    q: quit')

            char = click.getchar()
            if char == 'r':
                menu = 'register'
            elif char == 's':
                __phaseI(API, TOKEN)
                __phaseII(API, TOKEN)
                __phaseIII(API, TOKEN)
                __phaseIV(API, TOKEN)
                click.pause()

            elif char == 'g':
                get_status(API, TOKEN)

            elif char == 'i':
                get_info(user)

            elif char == 'q':
                menu = 'quit'

            else:
                click.echo('Invalid input')

        elif menu == 'register':
            click.clear()
            click.echo('Register menu:')
            if TOKEN is None:
                email = click.prompt(
                    '   Please enter the registered email'
                )
                github = click.prompt(
                    '   Please enter the github repo'
                )
                TOKEN = get_token(API, email, github)
                user = {'email': email, 'github': github, 'token': TOKEN}
                menu = 'main'
            else:
                click.echo('    n: get new token')
                click.echo('    b: back')
                char = click.getchar()
                if char == 'n':
                    TOKEN = None
                elif char == 'b':
                    menu = 'main'
                else:
                    click.echo('Invalid input')

        elif menu == 'quit':
            save_user_data(user)
            click.echo("I'll save your progress! See Ya!")
            return
