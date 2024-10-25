import yfinance as yf


class Extract:
    def __init__(self, symbol):
        self.__stock = yf.Ticker(symbol)
        self.__eps = float(self.__stock.info["trailingEps"])
        self.__forward_eps = float(self.__stock.info.get('forwardEps'))
        self.__dividend_yield = float(self.__stock.info.get('dividendYield'))
        self.__pe_ratio = float(self.__stock.info.get('trailingPE'))
        self.__market_cap = float(self.__stock.info.get('marketCap'))
        self.__total_debt = float(self.__stock.info.get('totalDebt'))
        self.__total_cash = float(self.__stock.info.get('totalCash'))
        self.__ev = float(self.__stock.info.get('enterpriseValue'))
        self.__ebitda = float(self.__stock.info.get('ebitda'))
        self.__enterprise_to_ebitda = float(self.__stock.info.get('enterpriseToEbitda'))
        self.__income_statement = self.__stock.financials  # there ebit inside
        self.__quarterly_income_statement = self.__stock.quarterly_financials # TODO: check for TTM EBIT
        self.__cash_flow = self.__stock.cash_flow
        self.__ebit_quarterly = self.__calc_ebit_quarterly()

        x = "x"

    def __calc_ebit_quarterly(self):
        latest_period = (quarterly_income_statement.columns[0]).strftime('%Y-%m-%d')
        ebit = quarterly_income_statement.loc['EBIT', latest_period]
        return ebit, latest_period


msft = yf.Ticker("MSFT")
quarterly_income_statement = msft.quarterly_financials
latest_period = (quarterly_income_statement.columns[0]).strftime('%Y-%m-%d')
ebit = quarterly_income_statement.loc['EBIT', latest_period]
x = Extract("AAPL")




