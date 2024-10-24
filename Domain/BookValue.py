import yfinance as yf


class BookValue:
    def __init__(self, ticker_symbol):
        """
        Initialize BookValue class with the given stock ticker symbol.

        Args:
        - ticker_symbol (str): Stock ticker symbol

        Attributes:
        - stock (dict): information of the stock obtained using yfinance.
        - forward_PE (float): Forward Price to Earnings ratio.
        - estimated_eps (float): Estimated Earnings Per Share (EPS) based on forward PE ratio.
        - eps (float): Trailing Earnings Per Share (EPS).
        - annual_return (float): Assumed annual return rate.
        - estimated_peg_ratio (float): Estimated Price/Earnings to Growth (PEG) ratio.
        - historical_pegRatio (float): Historical Price/Earnings to Growth (PEG) ratio.
        - peg_ratio (float): Minimum of estimated and historical PEG ratios.
        - future_eps (float): Future Estimated Earnings Per Share (EPS).
        """
        self.stock = yf.Ticker(ticker_symbol).info
        self.forward_PE = self.stock["forwardPE"]
        self.estimated_eps = self.stock["currentPrice"] / self.forward_PE
        self.eps = float(self.stock["trailingEps"])
        self.annual_return = 1.15
        self.estimated_peg_ratio = self.stock["trailingPegRatio"]
        self.historical_pegRatio = self.stock["pegRatio"]
        self.peg_ratio = min(self.estimated_peg_ratio, self.historical_pegRatio)
        self.future_eps = self.eps

    def calculate_future_price(self, years=10):
        """
        Calculate the estimated future price based on projected EPS growth.

        Args:
        - years (int): Number of years to project into the future (default is 10).

        Returns:
        - dict: A dictionary containing future market price, sticker price, and safety margin.
        """
        for i in range(years):
            self.future_eps *= self.annual_return
        future_market_price = self.future_eps * self.peg_ratio
        sticker_price = 0.25 * future_market_price
        safety = sticker_price * 0.5
        return {
            "future_market_price": future_market_price,
            "sticker_price": sticker_price,
            "safety": safety
        }


# Example usage:
msft_book_value = BookValue("MSFT")
results = msft_book_value.calculate_future_price()
print(results)
