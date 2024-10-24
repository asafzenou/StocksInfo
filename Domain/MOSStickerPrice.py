import yfinance as yf


class MOSStickerPrice:
    def __init__(self, company_symbol, present):
        """
        Initialize MOSStickerPrice class with company symbol and present value.

        Args:
        - company_symbol (str): The symbol of the company.
        - present (float): Present value or current valuation factor.

        Attributes:
        - __stock (dict): information of the stock obtained using yfinance (private attribute).
        - __present (float): Present value or current valuation factor (private attribute).
        - __f_gr (float): Future growth rate (private attribute).
        - __eps (float): Earnings Per Share (EPS) value (private attribute).
        """
        # Retrieve stock information for the given company symbol
        self.__stock = yf.Ticker(company_symbol).info
        self.__present = present
        self.__f_gr = 0
        self.__eps = 0

    def mos_calculate(self):
        """
        Calculate the Margin of Safety (MOS) Sticker Price based on future growth rates.

        Calculates the projected EPS for the next 10 years based on future growth rate.
        Determines the future Price/Earnings (P/E) ratio and the ten-year projected value.
        Discounts the ten-year projected value over 10 years at a 15% rate to derive MOS Sticker Price.

        Returns:
        - float: MOS (Margin of Safety) Sticker Price.
        """
        # Retrieve the trailing EPS (Earnings Per Share) from the stock information
        eps = float(self.__stock["trailingEps"])
        self.__eps = eps

        # Set future growth rate and present growth rate
        future_gr = self.__present
        self.__f_gr = future_gr

        # Calculate EPS for the next 10 years based on future growth rate
        for i in range(10):
            eps = eps * (1 + future_gr)

        # Calculate future Price/Earnings (P/E) ratio and ten-year projected value
        future_pe = 2 * future_gr * 100
        ten_year_value = future_pe * eps

        # Discount the ten-year projected value over 10 years at a 15% rate
        for i in range(10):
            ten_year_value = ten_year_value / 1.15

        # Calculate the MOS (Margin of Safety) Sticker Price
        mos_sticker_price = ten_year_value / 2
        return mos_sticker_price
