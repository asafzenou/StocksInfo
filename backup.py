# import tkinter as tk
# from tkinter import ttk
# import yfinance as yf
# from Domain import GetCompanyValue
#
#
# # Function to format the list for display
# def lst_ordered(lst):
#     if len(lst) > 0:
#         get_max_len_first = len(max(lst, key=lambda x: len(x[0]))[0])
#         get_max_len_second = len(max(lst, key=lambda x: len(x[1]))[1])
#         get_max_len_third = len(max(lst, key=lambda x: len(str(x[2])))[2])
#         for i, item in enumerate(lst):
#             item_zero = (" " * (get_max_len_first - len(item[0]))) + item[0]
#             item_one = (" " * (get_max_len_second - len(item[1]))) + item[1]
#             item_two = (" " * (get_max_len_third - len(str(item[2])))) + str(item[2])
#             lst[i] = f"{item_zero} {item_one} {item_two}"
#     return lst
#
# # Function to get company information
# def get_company_info():
#     company_symbol = entry_company_symbol.get()
#     try:
#         stock = yf.Ticker(company_symbol)
#         eps = (float(stock.info["trailingEps"]))
#         share_outstanding = int(stock.info["sharesOutstanding"])
#         fcf = int(stock.info["freeCashflow"])
#         fcf_per_share = fcf/share_outstanding
#         current_share_price = int(stock.info["currentPrice"])
#         operating_cash_flow = int(stock.info["operatingCashflow"])
#         tax = int(stock.get_financials()[stock.get_financials().keys()[0]]["TaxProvision"])
#         capital_exp = int(stock.get_cash_flow()[stock.get_cash_flow().keys()[0]]["CapitalExpenditure"])
#
#         # Display the results in the GUI
#         result_text_company.config(text=f"Capital Expenditure: {add_commas(capital_exp)}\n"
#                                         f"Tax: {add_commas(tax)}\n"
#                                         f"Operating Cash Flow: {add_commas(operating_cash_flow)}\n"
#                                         f"Current Share Price: {add_commas(current_share_price)}\n"
#                                         f"Free Cash Flow: {add_commas(fcf)}\n"
#                                         f"Shares Outstanding: {add_commas(share_outstanding)}\n"
#                                         f"Earnings Per Share (EPS): {(eps)}\n"
#                                         f"FCF Ratio: {add_commas(int(current_share_price/fcf_per_share))}\n\n")  # You can calculate FCF Ratio
#
#
#     except Exception as e:
#         result_text_company.config(text=f"Error: {e}")
#
# # Function to analyze stocks
# def analyze_stocks():
#     future_gr = float(entry_growth_rate.get()) / 100
#
#     try:
#         with open('stocks.txt', 'r') as file:
#             lines = file.read().splitlines()
#             lines = [line for line in lines if line.strip()]
#
#             not_went_through = []
#             not_to_buy = []
#             to_buy = []
#
#             for symbol in lines:
#                 try:
#                     company_info = yf.Ticker(symbol).info
#                     company_name = company_info["longName"]
#                     stock = yf.Ticker(symbol)
#                     company_val = GetCompanyValue.GetCompanyValue(symbol, future_gr).get_val()[:2]
#                     int_company_val = []
#                     current_share_price = int(stock.info["currentPrice"])
#                     for i in range(len(company_val)):
#                         int_company_val.append(int(company_val[i]))
#                     stock_info = [symbol,current_share_price,int_company_val]
#                     max_val = max(company_val)
#                     if 0 <= max_val >= stock.info["currentPrice"] and (int_company_val[0] > 0 and int_company_val[1] > 0) and (int_company_val[0] * 3 > int_company_val[1] and int_company_val[1] * 3 > int_company_val[0]):
#                         print(stock_info)
#                         to_buy.append(stock_info)
#                     else:
#                         not_to_buy.append(stock_info)
#                 except Exception:
#                     not_went_through.append(symbol)
#
#             # Display the results
#             # buy = lst_ordered(to_buy)
#             # not_buy = lst_ordered(not_to_buy)
#             # for i in to_buy:
#             #     print(i)
#             to_buy_label.config(text="GO AND BUY:\n" + '\n'.join(to_buy))
#             # not_to_buy_label.config(text="Wait and Don't Buy:\n" + '\n'.join(not_buy))
#             # not_went_through_label.config(text="Did not work:\n" + '\n'.join(not_went_through))
#     except Exception as e:
#         # Update an existing label to display the error message
#         not_went_through_label.config(text=f"Error: {e}")
#
# # Function to handle option selection
# def choose_option():
#     selected_tab = notebook.index(notebook.select())
#     if selected_tab == 0:
#         get_company_info()
#     elif selected_tab == 1:
#         analyze_stocks()
#
# def add_commas(number):
#     # Convert the number to a string and reverse it
#     number_str = str(number)[::-1]
#
#     # Split the reversed string into groups of three digits
#     groups = [number_str[i:i + 3] for i in range(0, len(number_str), 3)]
#
#     # Join the groups with commas and reverse the result
#     result = ",".join(groups)[::-1]
#
#     return result
#
# # Create the main window
# root = tk.Tk()
# root.title("Stock Helper")
#
# # Create a notebook (tabs) for each functionality
# notebook = ttk.Notebook(root)
#
# # Tab for entering company symbol
# tab_company_info = ttk.Frame(notebook)
# notebook.add(tab_company_info, text='Company Info')
#
# label_company_symbol = tk.Label(tab_company_info, text="Enter company symbol:")
# label_company_symbol.pack()
# entry_company_symbol = tk.Entry(tab_company_info)
# entry_company_symbol.pack()
#
# get_info_button = tk.Button(tab_company_info, text="Get Company Info", command=choose_option)
# get_info_button.pack()
#
# result_text_company = tk.Label(tab_company_info, text="")
# result_text_company.pack()
#
# # Tab for entering future growth rate
# tab_stock_analysis = ttk.Frame(notebook)
# notebook.add(tab_stock_analysis, text='Stocks Analysis')
#
# label_growth_rate = tk.Label(tab_stock_analysis, text="Enter future growth rate (>= 15):")
# label_growth_rate.pack()
# entry_growth_rate = tk.Entry(tab_stock_analysis)
# entry_growth_rate.pack()
#
# analyze_button = tk.Button(tab_stock_analysis, text="Analyze Stocks", command=choose_option)
# analyze_button.pack()
#
# to_buy_label = tk.Label(tab_stock_analysis, text="")
# to_buy_label.pack()
# not_to_buy_label = tk.Label(tab_stock_analysis, text="")
# not_to_buy_label.pack()
# not_went_through_label = tk.Label(tab_stock_analysis, text="")
# not_went_through_label.pack()
#
# # Pack the notebook
# notebook.pack()
#
# # Start the GUI
# root.mainloop()
