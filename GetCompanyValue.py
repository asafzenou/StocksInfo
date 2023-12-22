from MOSStickerPrice import MOSStickerPrice
from PayBackTime import PayBackTime
from TenCap import TenCap

class GetCompanyValue:
    def __init__(self, company_symbol, present):
        """
        Initialize GetCompanyValue class with the company symbol and present value.

        Args:
        - company_symbol (str): The symbol of the company.
        - present (float): Present value or current valuation factor.

        Attributes:
        - __company_symbol (str): The symbol of the company (private attribute).
        - __present (float): Present value or current valuation factor (private attribute).
        """
        self.__company_symbol = company_symbol
        self.__present = present

    def get_val(self):
        """
        Calculate and retrieve company value metrics.

        This method calculates and retrieves the Margin of Safety (MOS) Sticker Price,
        Ten Cap value, and potentially Payback Time (commented out for now).

        Returns:
        - tuple: Calculated values including MOS Sticker Price and Ten Cap value.
        """
        # Calculate MOS (Margin of Safety) Sticker Price
        mos = MOSStickerPrice(self.__company_symbol, self.__present).mos_calculate()

        # Calculate Ten Cap value
        ten_cap = TenCap(self.__company_symbol).get_value()

        # Calculate Payback Time (currently commented out)
        # pay_back_time = PayBackTime(self.__company_symbol, self.__present).get_value()

        # Return calculated values
        return mos, ten_cap
