
class BenjaminGrahamFormula:
    def __init__(self, user_input_yield, user_input_future_growth, eps):
        self.__user_input_yield = user_input_yield
        self.__user_input_future_growth = user_input_future_growth
        self.__eps = eps

    def get_range(self):
        return self.__calc_lower_range(), self.__calc_upper_range()

    def __calc_upper_range(self):
        upper = self.__eps * (8.5 + (2 * self.__user_input_future_growth) * (4.4/self.__user_input_yield))
        return upper

    def __calc_lower_range(self):
        lower = self.__eps * (7.5 + (1.5 * self.__user_input_future_growth) * (4.4 / self.__user_input_yield))
        return lower
