import yfinance as yf
import datetime

class TenCap:
    def __init__(self, company_symbol):
        """
        Initialize TenCap class with the company symbol to calculate Ten Cap value.

        Args:
        - company_symbol (str): Symbol of the company for valuation.

        Attributes:
        - __ticker (yfinance.Ticker): Instance of the yfinance Ticker for the provided symbol (private attribute).
        - __operating_cash_flow (float): Operating cash flow of the company (private attribute).
        - __year (int): Current year (private attribute).
        - __month (int): Current month (private attribute).
        - __capital_expenditure (float): Capital expenditure of the company (private attribute).
        - __tax (float): Tax provision of the company (private attribute).
        - __share_outstanding (float): Number of shares outstanding (private attribute).
        """
        # Initialize class attributes using the provided company symbol
        self.__ticker = yf.Ticker(company_symbol)
        self.__operating_cash_flow = self.__ticker.info["operatingCashflow"]
        self.__year = datetime.date.today().year
        self.__month = int(datetime.date.today().month)
        self.__month_setter()
        self.__capital_expenditure = self.capital_exp_setter()
        self.__tax = self.__ticker.get_financials()[self.__ticker.get_financials().keys()[0]]["TaxProvision"]
        self.__share_outstanding = self.__ticker.info["sharesOutstanding"]

    def capital_exp_setter(self):
        """
        Set the Capital Expenditure attribute.

        Try to retrieve Capital Expenditure; if not available, set it to 30% of Operating Cash Flow.

        Returns:
        - float: Capital Expenditure value.
        """
        try:
            return self.__ticker.get_cash_flow()[self.__ticker.get_cash_flow().keys()[0]]["CapitalExpenditure"]
        except Exception:
            return 0.3 * self.__operating_cash_flow

    def __month_setter(self):
        """
        Set the month attribute to the previous month.

        Adjusts the month attribute to the previous month for calculations.
        """
        if self.__month == 1:
            self.__month = 12
        else:
            self.__month -= 1

    def get_value(self):
        """
        Calculate and retrieve the Ten Cap value.

        Calculate Ten Cap value based on the provided formula.

        Returns:
        - float: Ten Cap value.
        """
        return ((self.__operating_cash_flow + (self.__capital_expenditure * 0.7) + self.__tax) / self.__share_outstanding) * 10
