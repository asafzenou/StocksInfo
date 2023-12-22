import yfinance as yf

class PayBackTime:
    def __init__(self, ticker, present):
        """
        Initialize PayBackTime class with the ticker symbol and present value.

        Args:
        - ticker (str): Ticker symbol of the company.
        - present (float): Present value or current valuation factor.

        Attributes:
        - __ticker (yfinance.Ticker): Instance of the yfinance Ticker for the provided symbol (private attribute).
        - __growth (float): Present growth rate (private attribute).
        - __share_outstanding (float): Number of shares outstanding (private attribute).
        - __fcf (float): Free Cash Flow (FCF) value (private attribute).
        - __current_share_price (float): Current share price (private attribute).
        - __finance_dict (dict): Dictionary to store financial information (private attribute).
        """
        # Initialize necessary attributes using the provided ticker symbol and growth rate
        self.__ticker = yf.Ticker(ticker)
        self.__growth = present
        self.__share_outstanding = self.__ticker.info["sharesOutstanding"]
        self.__fcf = self.__ticker.info["freeCashflow"]
        self.__current_share_price = self.__ticker.info["currentPrice"]
        self.__finance_dict = {}

    def get_value(self):
        """
        Calculate and retrieve the estimated Payback Time.

        Calculates Free Cash Flow projections for the next 9 years based on the growth rate.
        Estimates cumulative Free Cash Flow and computes the payback time in 8 years.

        Returns:
        - float: Estimated payback time in 8 years.
        """
        # Calculate Free Cash Flow projections for the next 9 years
        free_cash_flow = []
        temp_fcf = self.__fcf

        for i in range(9):
            free_cash_flow.append(temp_fcf)
            temp_fcf = temp_fcf * (1 + self.__growth)

        # Calculate the cumulative Free Cash Flow and estimate the payback time
        cumulative_fcf = sum(free_cash_flow[1:])
        eight_year_payback = cumulative_fcf / self.__share_outstanding
        return eight_year_payback
