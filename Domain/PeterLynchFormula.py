
class PeterLynchFormula:
    def __init__(self, future_growth, dividend_yield, pe_ratio):
        self.__future_growth = future_growth
        self.__dividend_yield = dividend_yield
        self.__pe_ratio = pe_ratio

    def __calc_formula(self):
        """Output is 0 to whatever"""
        future_growth = self.__future_growth * 100
        div_yield = self.__dividend_yield * 100
        output = ((future_growth + div_yield) / self.__pe_ratio)
        return output

    def formula_result(self):
        calc = self.__calc_formula()
        if calc < 1:
            return "OverValued", calc
        if calc <= 1.5:
            return "FairlyValued", calc
        if calc <= 2:
            return "UnderValued", calc
        else:
            return "ExtremelyUnderValued", calc


    