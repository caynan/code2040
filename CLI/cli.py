# coding: utf-8
import click
import code2040
import solver
import six
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
                click.echo('    r: get token')
                click.echo('    s: solve problems')
                click.echo('    g: get status')
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
            click.echo('See Ya!')
            return
