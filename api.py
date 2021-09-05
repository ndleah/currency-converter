import requests

_HOST_ = 'https://api.frankfurter.app'
_CURRENCIES_ = '/currencies'
_LATEST_ = '/latest'


def call_api(url: str) -> requests.models.Response:
    """
    Function that will call the specified API endpoint and return the response

    Parameters
    ----------
    url : str
        URL of the API endpoint to be called

    Pseudo-code
    ----------
    # => To be filled by student

    Returns
    -------
    requests.models.Response
        Response from API request
    """
    # => To be filled by student

    return None

def format_currencies_url() -> str:
    """
    Function that will format the URL to the currency endpoint

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    # => To be filled by student

    Returns
    -------
    str
        Formatted URL to the currency endpoint
    """
    # => To be filled by student

    return None


def get_currencies():
    """
    Function that will extract the currency codes available from the Frankfurter app as a list

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    # => To be filled by student

    Returns
    -------
    list
        Currency codes available from the Frankfurter app
    """
    # => To be filled by student

    return None


def format_latest_url(from_currency: str, to_currency: str) -> str:
    """
    Function that will format the URL to the latest endpoint

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    # => To be filled by student

    Returns
    -------
    str
        Formatted URL to the latest endpoint
    """
    # => To be filled by student

    return None

