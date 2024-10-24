
class PeterLynchFormula:
    def __init__(self, future_eps_growth, dividend_yield, pe_ratio):
        self.__future_eps_growth = future_eps_growth
        self.__dividend_yield = dividend_yield
        self.__pe_ratio = pe_ratio

    def __calc_formula(self):
        """Output is 0 to whatever"""
        output = ((self.__future_eps_growth + self.__dividend_yield) / self.__future_eps_growth)
        return output

    def formula_result(self):
        calc = self.__calc_formula()
        if calc < 1:
            return "OverValued"
        if calc <= 1.5:
            return "FairlyValued"
        if calc <= 2:
            return "UnderValued"
        else:
            return "ExtremelyUnderValued"


    