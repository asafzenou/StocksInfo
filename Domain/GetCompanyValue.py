from Domain.MOSStickerPrice import MOSStickerPrice
#from PayBackTime import PayBackTime
from Domain.TenCap import TenCap
from Domain.Extract import Extract
from Domain.BenjaminGrahamFormula import BenjaminGrahamFormula
from Domain.PeterLynchFormula import PeterLynchFormula
from Domain.EvEbitdaRatio import EvEbitdaRatio
# from Domain.JoelGreenbeltFormulas import JoelGreenbeltFormulas


class GetCompanyValue:
    def __init__(self, company_symbol, future_growth_rate, corporate_bond_yield):
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
        self.__future_growth_rate = future_growth_rate
        self.__corporate_bond_yield = corporate_bond_yield
        self.__extract = Extract(self.__company_symbol)

    def get_val(self):
        """
        Calculate and retrieve company value metrics.

        This method calculates and retrieves the Margin of Safety (MOS) Sticker Price,
        Ten Cap value, and potentially Payback Time (commented out for now).

        Returns:
        - tuple: Calculated values including MOS Sticker Price and Ten Cap value.
        """


        # --------- Rule 1 -----------------
        # Calculate MOS (Margin of Safety) Sticker Price
        mos = MOSStickerPrice(self.__company_symbol, self.__future_growth_rate).mos_calculate()

        # Calculate Ten Cap value
        ten_cap = TenCap(self.__company_symbol).get_value()

        # Calculate Payback Time (currently commented out)
        # pay_back_time = PayBackTime(self.__company_symbol, self.__present).get_value()
        # Return calculated values

        benjamin_grham = BenjaminGrahamFormula(user_input_yield=self.__corporate_bond_yield,
                                               user_input_future_growth=self.__future_growth_rate,
                                               eps=self.__extract.get_eps()).get_range()

        # string, float
        peter_lynch = PeterLynchFormula(future_growth=self.__future_growth_rate,
                                        dividend_yield=self.__extract.get_dividend_yield(),
                                        pe_ratio=self.__extract.get_pe_ratio()).formula_result()

        # joel_greenblet = JoelGreenbeltFormulas()

        ev_ebitda_ratio = EvEbitdaRatio(self.__extract.get_ev(),
                                        self.__extract.get_ebitda()).get_ev_ebitda_ratio()

        sector = self.__extract.get_sector()
        industry = self.__extract.get_industry()
        ps = self.__extract.get_ps_ratio()
        pb = self.__extract.get_pb_ratio()
        pe = self.__extract.get_pe_ratio()
        dividend = self.__extract.get_dividend_yield()
        ev_sales = self.__extract.get_ev_sales()
        return (sector, industry, mos, ten_cap, benjamin_grham,
                peter_lynch, ev_ebitda_ratio, ps, pb, pe, dividend,
                ev_sales)

    def get_company_name(self):
        return self.__extract.get_company_name()

    def get_company_current_price(self):
        return self.__extract.get_company_current_price()