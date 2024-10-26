
class BenjaminGrahamFormula:
    def __init__(self, user_input_yield, user_input_future_growth, eps):
        self.__user_input_yield = user_input_yield
        self.__user_input_future_growth = user_input_future_growth
        self.__eps = eps

    def get_range(self):
        return self.__calc_lower_range(), self.__calc_upper_range()

    def __calc_upper_range(self):
        eps = self.__eps
        future_g_input = self.__user_input_future_growth * 100
        yield_input = self.__user_input_yield * 100
        upper = (eps * (8.5 + (2 * future_g_input)) * 4.4)/yield_input
        return upper

    def __calc_lower_range(self):
        eps = self.__eps
        future_g_input = self.__user_input_future_growth * 100
        yield_input = self.__user_input_yield * 100
        lower = (eps * (7.5 + (1.5 * future_g_input)) * 4.4) / yield_input
        return lower
