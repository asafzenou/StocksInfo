class JoelGreenbeltFormulas:
    def __init__(self, ev, quarterly_income_statement, ebit_q):
        self.__ev = ev
        self.__quarterly_income_statement = quarterly_income_statement
        self.__ebit_q, self.__last_time = ebit_q

    def calc_ebit(self):
        try:
            if self.__quarterly_income_statement.empty:
                raise Exception("Quarterly income statement data is not available.")
            if not self.__quarterly_income_statement.empty:
                # Ensure 'Operating Income' is in the DataFrame
                if 'Operating Income' in self.__quarterly_income_statement.index:
                    # Extract the 'Operating Income' row
                    operating_income_series = self.__quarterly_income_statement.loc['Operating Income']

                    # Ensure we have at least four quarters of data
                    if len(operating_income_series) >= 4:
                        # Get the most recent four quarters
                        last_four_quarters = operating_income_series.iloc[:4]
                    else:
                        raise Exception("Insufficient data: Less than four quarters available.")
                else:
                    raise Exception("'Operating Income' not found in the quarterly income statement.")
            else:
                raise Exception("Quarterly income statement data is not available.")

            if 'Operating Income' in self.__quarterly_income_statement.index and len(operating_income_series) >= 4:
                # Sum the Operating Income for the last four quarters
                ebit_ttm = last_four_quarters.sum()
                return "ebit_tmm", ebit_ttm, "tmm_date"
            else:
                raise Exception("Unable to calculate EBIT (TTM) due to insufficient data.")

        except Exception:
            return "ebit", self.__ebit_q, self.__last_time
