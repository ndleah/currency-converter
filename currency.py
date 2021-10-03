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
    SET CURRENCIES TO get_currencies()
    LIST CURRENCIES

    # define the function:
    FUNCTION check_valid_currency(currency)
    BEGIN FUNCTION
        IF currency included in CURRENCIES list THEN
            RETURN True
        ELSE
            RETURN False
    END FUNCTION

    Returns
    -------
    bool
        True if the currency code is valid otherwise False
    """

    if currency in CURRENCIES:
        return True
    else:
        return False

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

        self.inverse_rate = round(1/self.rate, 5)

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
        return "Today's " + "(" + self.date + ")" + " conversion rate from " + self.from_currency + " to "+self.to_currency + " is " + str(self.rate) + ". The inverse rate is " + str(self.inverse_rate)


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
    # define the function:
    FUNCTION check_valid_currency(currency)
    BEGIN FUNCTION
        SET variable_1 TO get the code for the origin currency
        SET variable_2 TO get the code for the destination currency
        SET variable_3 TO get the amount to be converted
        SET variable_4 TO get the the conversion rate
        SET variable_5 TO get the date when the conversion rate was recorded

        CREATE currency object TO call the Currency class with above objects as parameters
        CALL the reverse_rate() of currency object TO get the inverse rate
        RETURN currency object
    END FUNCTION

    Returns
    -------
    Currency
        Instantiated Currency
    """
    from_currency = result.get("base")
    to_currency = list(result.get("rates").keys())[0]
    amount = result.get("amount")
    rate = result.get("rates").get(to_currency)
    date = result.get("date")

    currency = Currency(from_currency, to_currency, amount, rate, None, date)
    currency.reverse_rate()

    return currency
