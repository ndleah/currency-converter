import sys
from api import call_api, format_latest_url
from currency import check_valid_currency, extract_api_result


def main():
    """
    Function that will check if there are enough input arguments provided.
    If so it will return the formatted result from the Frankfurter app.
    If not it will return an error message

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    # => To be filled by student

    Returns
    -------
    str
        Formatted API result or error message
    """
    # => To be filled by student

    return None


def get_rate(from_currency: str, to_currency: str):
    """
    Function that will check if provided currency codes are valid otherwise it will return error message.
    If both are valid, it will format the API url, make a request to it and format the result

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
        Formatted API result or error message
    """
    # => To be filled by student

    return None


if __name__ == "__main__":
    main()
