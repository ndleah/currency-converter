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
    # define the function: 
    FUNCTION call_api(STRING url)
    BEGIN FUNCTION
        SET response TO make a GET request from url
        RETURN response
    END FUNCTION

    Returns
    -------
    requests.models.Response
        Response from API request
    """
    response = requests.get(url)
    return response

def format_currencies_url() -> str:
    """
    Function that will format the URL to the currency endpoint

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    # define the function: 
    FUNCTION format_currencies_url()
    BEGIN FUNCTION
        SET currencies_URL TO concatanate string into a URL with currency endpoint
        RETURN currencies_URL
    END FUNCTION

    -------
    str
        Formatted URL to the currency endpoint
    """
    currencies_URL = _HOST_+ _CURRENCIES_

    return currencies_URL


def get_currencies():
    """
    Function that will extract the currency codes available from the Frankfurter app as a list

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    # define the function: 
    FUNCTION get_currencies()
    STRING url
    BEGIN FUNCTION
        SET data TO return a JSON object of the currencies URL
        SET key_extract TO convert the JSON object result into a list
        RETURN key_extract
    END FUNCTION
    
    Returns
    -------
    list
        Currency codes available from the Frankfurter app
    """

    data = call_api(format_currencies_url()).json()
    key_extract = list(data.keys())

    return key_extract


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
    # Define the function
    FUNCTION format_latest_url(from_currency, to_currency)
        STRING from_currency
        STRING to_currency
        SET latest_URL TO concatanate string into a URL with latest endpoint
        RETURN key_extract
    END FUNCTION

    Returns
    -------
    str
        Formatted URL to the latest endpoint
    """
    latest_URL = _HOST_+ _LATEST_ + "?from="+from_currency+"&to="+to_currency
    
    return latest_URL

