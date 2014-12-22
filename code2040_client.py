import json, requests

class ClientAPI(object):
    """
    A simple interface to interact with the CODE2040 API

    """

    def register(self, email, github):
        """
        Provide a inteface to register on the CODE2040 API.

        Args:
            email: a string with the same email address that you used to
                enroll with CODE2040.
            github: a string with the URL of the repository with your code.

        Returns:
            Return a Python Dictionary (json) with your token.
        """
        url = 'http://challenge.code2040.org/api/register'
        data = {'email': email, 'github': github}
        token = requests.post(url, data=json.dumps(data)).json()
        # format token to the way used in all requests
        token = {'token': token['result']}

        return token

    def __get_data(self, url, token):
        """
        Get data from the CODE2040 API using the given endpoint.

        Args:
            url: the endpoint location.
            token: dictionary with token given in registration.

        Returns:
            Return the provided response, the type depend on the request.
        """
        response = requests.post(url, data=json.dumps(token)).json()
        return response['result']

    def __post_data(self, url, data):
        """

        """
        # concatenate token and data dict into one.
        response = request.post(url, data=json.dumps(data)).json()

    def get_reverse_string(self, token):
        """
        Make a request to the ``getstring`` endpoint and get a string.

        Args:
            token: dictionary with token given in registration.

        Returns:
            Returns the string, that should be reversed.
        """
        url = 'http://challenge.code2040.org/api/getstring'
        response = self.__get_data(url, token)

        return response

    def post_reverse_string(self, token, answer):
        """

        """
        url = 'http://challenge.code2040.org/api/validatestring'
        conc = token.copy()
        conc.update(answer)
        response = self.__post_data(url, conc)

        return response['result']

    def get_haystack(self, token):
        """
        Make a request to the ``haystack`` endpoint and get a dictionary
        with a list and a string to be searched.

        Args:
            token: dictionary with token given in registration.

        Returns:
            Returns a dictionary with two values and keys. ``needle``,
            is a string. ``haystack``, is an array of strings.
        """
        url = 'http://challenge.code2040.org/api/haystack'
        response = self.__get_data(url, token)

        return response

    def get_prefix(self, token):
        """
        Make a request to the ``prefix`` endpoint and get a dictionary
        with a string and an array of strings.

        Args:
            token: dictionary with token given in registration.

        Returns:
            Returns a dictionary with two values and keys. ``prefix``,
            is a string. ``array``, is an array of strings.
        """
        url = 'http://challenge.code2040.org/api/prefix'
        response = self.__get_data(url, token)

        return response

    def get_dating(self, token):
        """
        Make a request to the ``time`` endpoint and get a dictionary with
        a string and a number.

        Args:
            token: dictionary with token given in registration.

        Returns:
            Returns a dictionary with two values and keys. ``datestamp``,
            is a string. ``interval``, is a number.

        """
        url = 'http://challenge.code2040.org/api/time'
        response = self.__get_data(url, token)

        return response
