from dataclasses import dataclass
from api import get_currencies

CURRENCIES = get_currencies()


def check_valid_currency(currency: str) -> bool:
    """
    Function that will check currency code is amongst the list of available currencies

    Parameters
    ----------
    currency : str
        Currency code to be checked

    Pseudo-code
    ----------
    # => To be filled by student

    Returns
    -------
    bool
        True if the currency code is valid otherwise False
    """

    # => To be filled by student

    return None


@dataclass
class Currency:
    """
    Class that represents a Currency conversion object. 

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    """
    from_currency: str = None
    to_currency: str = None
    amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    date: str = None

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate, round it to 5 decimal places and save it in the attribute inverse_rate

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        # => To be filled by student

    def format_result(self):
        """
        Methods returning the formatted successful message

        Parameters
        ----------
        None

        Returns
        -------
        str
            Formatted successful message
        """
        # => To be filled by student

        return None


def extract_api_result(result: dict) -> Currency:
    """
    Function that will extract the relevant fields from API result, instantiate a Currency class accordingly and
    calculate the inverse rate

    Parameters
    ----------
    result : dict
        Results of the API converted as dictionary

    Pseudo-code
    ----------
    # => To be filled by student

    Returns
    -------
    Currency
        Instantiated Currency
    """
    # => To be filled by student

    return None
