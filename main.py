import sys
from api import call_api, format_latest_url
from currency import CURRENCIES, check_valid_currency, extract_api_result


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
    # define the function:
    FUNCTION main()
        IF number of arguments < 3 THEN
            DISPLAY missing argument error message
        OTHERWISE:
            IF number of arguments = 3:
                IF the first argument doesn't have the same value as the second argument: 
                    SET a variable to call the function get_rate 
                    REUTRN DISPLAY the result a variable
                OTHERWISE:
                    DISPLAY API error message
            OTHERWISE:
                DISPLAY API error message
    END FUNCTION    

    Returns
    -------
    str
        Formatted API result or error message
    """
    if len(sys.argv) < 3:
        print("[ERROR] You haven't provided 2 currency codes")
    else:
        if len(sys.argv) == 3:
            if sys.argv[1] != sys.argv[2]: 
                final_result = get_rate(sys.argv[1], sys.argv[2]) 
                return print(final_result)
            else:
                print("There is an error with API call")
        else:
            print("There is an error with API call")
     

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
    # define the function:
    FUNCTION get_rate(currency_1, currency_2)
    STRING currency_1
    STRING currency_2
        SET a variable TO check currency valid of currency_1 (BOOLEAN)
        SET a variable TO check currency valid of currency_2 (BOOLEAN)
        SET a variable TO the url with latest endpoint

        IF both currency_1 AND currency_2 are True THEN
            SET a variable TO create a JSON object of API 
            SET a variable TO extract API results
            RETURN a formatted successful message
        OTHERWISE
            IF currency_1 is True AND currency_2 IS False:
                DISPLAY the error message
            IF currency_1 is False AND  currency_2 IS True:
                DISPLAY the error message
            OTHERWISE:
                DISPLAY the error message
        STOP THE CODE FROM CONTINUING EXECUTING
    END FUNCTION

    Returns
    -------
    str
        Formatted API result or error message
    """
    from_currency_result = check_valid_currency(from_currency)
    to_currency_result = check_valid_currency(to_currency)
    url = format_latest_url(from_currency, to_currency)
        
    if from_currency_result == True and to_currency_result == True:
        result = call_api(url).json()
        currency = extract_api_result(result)
        return currency.format_result()    
    else:
        if from_currency_result == True and to_currency_result == False:
            print(to_currency + " is not a valid option")
        elif from_currency_result == False and to_currency_result == True:
            print(from_currency + " is not a valid option")
        elif from_currency_result == False and to_currency_result == False:
            print(from_currency + " and " + to_currency + " is not a valid option")
    exit()

if __name__ == "__main__":
    main()
