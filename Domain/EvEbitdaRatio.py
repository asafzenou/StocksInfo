

class EvEbitdaRatio:
    def __init__(self, ev, ebitda):
        self.ev = ev
        self.ebitda = ebitda
        self.__ev_ebitda_ratio = ev/ebitda
        x = "x"

    def get_ev_ebitda_ratio(self):

        return self.__ev_ebitda_ratio
