class JoelGreenbeltFormulas:
    def __init__(self, ev_q, quarterly_income_statement, ebit_q):
        self.__ev_q = ev_q
        self.__quarterly_income_statement = quarterly_income_statement
        self.__ebit_q, self.__last_time = ebit_q

    def calc_ebit(self):
        return self.__ebit_q, str(self.__last_time)

    # def calc_earnings_yield(self):
    #     ebit_number, date = self.calc_ebit()
    #     if ebit_kind == "ebit_tmm":
    #         return ebit_kind, ebit_number/self.__ev, date
    #     return None
    #
    #
    #
    # def calc_return_on_capital(self):



