import yfinance as yf


class Extract:
    def __init__(self, symbol):
        self.__stock = yf.Ticker(symbol)
        self.__stock_info = self.__stock.info
        # self.__financials = self.__stock.financials
        self.__eps = float(self.__stock_info["trailingEps"])
        print(self.__eps)
        self.__forward_eps = float(self.__stock_info.get('forwardEps'))
        try:
            self.__dividend_yield = float(self.__stock_info.get('dividendYield'))
        except Exception:
            self.__dividend_yield = 0
        self.__pe_ratio = float(self.__stock_info.get('trailingPE'))
        self.__ebitda = float(self.__stock_info.get('ebitda')) # TODO
        self.__enterprise_to_ebitda = float(self.__stock_info.get('enterpriseToEbitda'))
        self.__quarterly_income_statement = self.__stock.quarterly_financials
        self.__cash_flow = self.__stock.cash_flow
        self.__ebit_quarterly = self.__calc_ebit_quarterly()
        self.__ev = float(self.__stock_info.get('enterpriseValue'))


    def __calc_ebit_quarterly(self):
        latest_period = (self.__quarterly_income_statement.columns[0]).strftime('%Y-%m-%d')
        ebit = self.__quarterly_income_statement.loc['EBIT', latest_period]
        return ebit, latest_period

    def get_eps(self):
        return self.__eps

    def get_future_eps(self):
        return self.__forward_eps

    def get_dividend_yield(self):
        return self.__dividend_yield

    def get_pe_ratio(self):
        return self.__pe_ratio

    def get_ev(self):
        return self.__ev

    def get_ebitda(self):
        return self.__ebitda

    def get_company_name(self):
        company_info = self.__stock.info
        company_name = company_info["longName"]
        return company_name

    def get_company_current_price(self):
        return self.__stock_info["currentPrice"]

# x = Extract("AAPL")




