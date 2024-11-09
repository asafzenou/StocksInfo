from Domain.GetCompanyValue import GetCompanyValue
import pandas as pd
import numpy as np
import openpyxl

def round_number(num):
    return np.round(num, 3) if num is not None else None

def analyze_stocks():
    """
    Analyze stock information and categorize stocks based on calculated values.

    Reads stock symbols from a file, retrieves their information using yfinance, and categorizes them
    based on calculated values into 'to buy', 'not to buy', and 'not went through' categories.
    Displays the categorized results in the GUI.
    """
    entry_growth_rate = float(input('Enter growth rate in %: '))
    entry_cby = float(input('Enter corporate bond yield in %: '))

    future_gr = float(entry_growth_rate) / 100
    corporate_bond_yield = float(entry_cby) / 100

    try:
        with open('stocks.txt', 'r') as file:
            lines = file.read().splitlines()
            lines = [line for line in lines if line.strip()]

            lst = []
            not_went_through = []

            for symbol in lines:
                try:
                    company = GetCompanyValue(symbol, future_gr, corporate_bond_yield)
                    company_val = company.get_val()
                    company_name = company.get_company_name()
                    current_share_price = float(company.get_company_current_price())
                    # stock_info = [
                    #     f"{company_name}({symbol})",
                    #     f"Current Price: {current_share_price},\n",
                    #     f"  Buy Price: {int(max(company_val[:2]))} --> Rule 1 mos :{company_val[0]}"
                    #     f"\n   Rule 1 ten cap: {company_val[1]}"
                    #     f"\n   Benjamin Graham: {company_val[2]}"
                    #     f"\n   Peter Lynch: {company_val[3]}"
                    #     f"\n   EV Ebitda Ratio: {company_val[4]}\n\n"
                    # ]
                    sector = company_val[0]
                    industry = company_val[1]
                    mos = np.round(company_val[2], 3)
                    ten_cap = np.round(company_val[3], 3)
                    benjamin_graham = (float(np.round(company_val[4][0], 3)), float(np.round(company_val[4][1], 3)))
                    peter_lynch = (company_val[5][0], float(np.round(company_val[5][1], 3)))
                    ev_ebitda_ratio = np.round(company_val[6], 3)
                    ps = round_number(company_val[7])
                    pb = round_number(company_val[8])
                    pe = round_number(company_val[9])
                    dividend = round_number(company_val[10])
                    ev_sales = round_number(company_val[11])
                    stock_info = [company_name, sector, industry, symbol, current_share_price, mos,
                                  ten_cap, benjamin_graham, peter_lynch, ev_ebitda_ratio, ps, pb,
                                  pe, dividend, ev_sales]
                    lst.append(stock_info)
                except Exception:
                    not_went_through.append(symbol)
            return lst, not_went_through


            # Here you can add code to display the results or handle the lst and not_went_through variables

    except FileNotFoundError:
        print("Error: The file 'stocks.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
def lst_ordered(lst):
    if len(lst) > 0:
        get_max_len_first = len(max(lst, key=lambda x: len(x[0]))[0])
        get_max_len_second = len(max(lst, key=lambda x: len(x[1]))[1])
        get_max_len_third = len(max(lst, key=lambda x: len(str(x[2])))[2])
        for i, item in enumerate(lst):
            item_zero = (" " * (get_max_len_first - len(item[0]))) + item[0]
            item_one = (" " * (get_max_len_second - len(item[1]))) + item[1]
            item_two = (" " * (get_max_len_third - len(str(item[2])))) + str(item[2])
            lst[i] = f"{item_zero} {item_one} {item_two}"
    return lst


if __name__ == '__main__':
    lst, not_went_through = analyze_stocks()
    df_lst = pd.DataFrame(lst, columns=[
        'Company',
        'Sector',
        'Industry',
        'Ticker',
        'Current Price',
        'Rule 1 MOS',
        'Rule 1 Ten Cap',
        'Benjamin Graham',
        'Peter Lynch',
        'EV/EBITDA Ratio',
        'ps',
        'pb',
        'pe',
        'dividend',
        'ev_sales'
    ])

    # Print the dataframes to verify
    print("DataFrame of Successfully Retrieved Companies:")
    print(df_lst)

    if not_went_through:
        df_not_went_through = pd.DataFrame(not_went_through, columns=['Didnt Work'])
        print("\nDataFrame of Companies That Did Not Work:")
        print(df_not_went_through)

    df_lst.to_excel('StocksToBuy.xlsx', index=False)
    df_lst.to_csv('StocksToBuy.csv', index=False)

