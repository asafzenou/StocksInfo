import tkinter as tk
from tkinter import ttk
import yfinance as yf
import GetCompanyValue

# Function to format the list for display
def lst_ordered(lst):
    """
    Format the list elements for display in a visually aligned manner.

    Args:
    - lst (list): List of tuples representing data to be formatted.

    Returns:
    - list: Formatted list for display.
    """
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

# Function to get company information
def get_company_info():
    """
    Retrieve company information based on the provided company symbol.

    Fetches various financial data using the yfinance library and displays it in the GUI.
    """
    company_symbol = entry_company_symbol.get()
    try:
        stock = yf.Ticker(company_symbol)
        eps = (float(stock.info["trailingEps"]))
        share_outstanding = int(stock.info["sharesOutstanding"])
        fcf = int(stock.info["freeCashflow"])
        fcf_per_share = fcf/share_outstanding
        current_share_price = int(stock.info["currentPrice"])
        operating_cash_flow = int(stock.info["operatingCashflow"])
        tax = int(stock.get_financials()[stock.get_financials().keys()[0]]["TaxProvision"])
        capital_exp = int(stock.get_cash_flow()[stock.get_cash_flow().keys()[0]]["CapitalExpenditure"])

        # Display the results in the GUI
        result_text_company.config(text=f"Capital Expenditure: {add_commas(capital_exp)}\n"
                                        f"Tax: {add_commas(tax)}\n"
                                        f"Operating Cash Flow: {add_commas(operating_cash_flow)}\n"
                                        f"Current Share Price: {add_commas(current_share_price)}\n"
                                        f"Free Cash Flow: {add_commas(fcf)}\n"
                                        f"Shares Outstanding: {add_commas(share_outstanding)}\n"
                                        f"Earnings Per Share (EPS): {(eps)}\n"
                                        f"FCF Ratio: {add_commas(int(current_share_price/fcf_per_share))}\n\n")  # You can calculate FCF Ratio


    except Exception as e:
        result_text_company.config(text=f"Error: {e}")

# Function to analyze stocks
def analyze_stocks():
    """
    Analyze stock information and categorize stocks based on calculated values.

    Reads stock symbols from a file, retrieves their information using yfinance, and categorizes them
    based on calculated values into 'to buy', 'not to buy', and 'not went through' categories.
    Displays the categorized results in the GUI.
    """
    future_gr = float(entry_growth_rate.get()) / 100

    try:
        with open('stocks.txt', 'r') as file:
            lines = file.read().splitlines()
            lines = [line for line in lines if line.strip()]

            not_went_through = []
            not_to_buy = []
            to_buy = []

            for symbol in lines:
                try:
                    company_info = yf.Ticker(symbol).info
                    company_name = company_info["longName"]
                    stock = yf.Ticker(symbol)
                    company_val = GetCompanyValue.GetCompanyValue(symbol, future_gr).get_val()
                    int_company_val = []
                    current_share_price = int(stock.info["currentPrice"])
                    for i in range(len(company_val)):
                        int_company_val.append(int(company_val[i]))
                    stock_info = [f"{company_name}({symbol})",f"Current Price: {current_share_price},", f"Buy Price: {int(max(company_val))} --> {int_company_val}"]
                    max_val = max(company_val)
                    if 0 <= max_val >= stock.info["currentPrice"]:
                        to_buy.append(stock_info)
                    else:
                        not_to_buy.append(stock_info)
                except Exception:
                    not_went_through.append(symbol)

            buy = lst_ordered(to_buy)
            not_buy = lst_ordered(not_to_buy)

            # Create a frame to contain the labels
            result_frame = tk.Frame(tab_stock_analysis)
            result_frame.pack(fill=tk.BOTH, expand=True)

            # Create a scrollbar for the frame
            scrollbar = tk.Scrollbar(result_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Create a canvas within the frame
            canvas = tk.Canvas(result_frame, yscrollcommand=scrollbar.set)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            scrollbar.config(command=canvas.yview)

            # Create a frame within the canvas to hold the labels
            inner_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

            # Function to update scroll region
            def _on_frame_configure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))

            inner_frame.bind("<Configure>", _on_frame_configure)

            # Place the labels inside the inner frame
            to_buy_label = tk.Label(inner_frame, text="GO AND BUY:\n" + '\n'.join(buy))
            to_buy_label.pack()

            not_to_buy_label = tk.Label(inner_frame, text="Wait and Don't Buy:\n" + '\n'.join(not_buy))
            not_to_buy_label.pack()

            not_went_through_label = tk.Label(inner_frame, text="Did not work:\n" + '\n'.join(not_went_through))
            not_went_through_label.pack()

            # Update the canvas window when the inner frame changes size
            inner_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
    except Exception as e:
        # Update an existing label to display the error message
        not_went_through_label.config(text=f"Error: {e}")

# Function to handle option selection
def choose_option():
    """
    Handle the selection of options based on the chosen tab.

    Determines the selected tab in the GUI and triggers the appropriate function based on the tab selection.
    """
    selected_tab = notebook.index(notebook.select())
    if selected_tab == 0:
        get_company_info()
    elif selected_tab == 1:
        analyze_stocks()

def add_commas(number):
    """
    Add commas to a number for better formatting.

    Args:
    - number (int/float): Number to be formatted.

    Returns:
    - str: Formatted number with commas.
    """
    # Convert the number to a string and reverse it
    number_str = str(number)[::-1]

    # Split the reversed string into groups of three digits
    groups = [number_str[i:i + 3] for i in range(0, len(number_str), 3)]

    # Join the groups with commas and reverse the result
    result = ",".join(groups)[::-1]

    return result

def add_text_bottom(root, text):
    """
    Add text at the bottom of the GUI window.

    Args:
    - root (tk.Tk): Root window of the GUI.
    - text (str): Text to be displayed at the bottom.

    Returns:
    - None
    """

    label = tk.Label(root, text=text)
    label.pack(side=tk.BOTTOM)

# Create the main window
root = tk.Tk()
root.title("Stock Helper")

# Create a notebook (tabs) for each functionality
notebook = ttk.Notebook(root)

# Tab for entering company symbol
tab_company_info = ttk.Frame(notebook)
notebook.add(tab_company_info, text='Company Info')

label_company_symbol = tk.Label(tab_company_info, text="Enter company symbol:")
label_company_symbol.pack()
entry_company_symbol = tk.Entry(tab_company_info)
entry_company_symbol.pack()

get_info_button = tk.Button(tab_company_info, text="Get Company Info", command=choose_option)
get_info_button.pack()

result_text_company = tk.Label(tab_company_info, text="")
result_text_company.pack()


text = "Created by Asaf Zenou, inspired by Rule Number 1 Workshop. It's important to note that the formulas themselves for the calculation were taken from YouTube and this is not advice for buying or selling stocks."
add_text_bottom(root, text)

# Tab for entering future growth rate
tab_stock_analysis = ttk.Frame(notebook)
notebook.add(tab_stock_analysis, text='Stocks Analysis')

label_growth_rate = tk.Label(tab_stock_analysis, text="Enter future growth rate (>= 15):")
label_growth_rate.pack()
entry_growth_rate = tk.Entry(tab_stock_analysis)
entry_growth_rate.pack()

analyze_button = tk.Button(tab_stock_analysis, text="Analyze Stocks", command=choose_option)
analyze_button.pack()

to_buy_label = tk.Label(tab_stock_analysis, text="", width=100)
to_buy_label.pack()
not_to_buy_label = tk.Label(tab_stock_analysis, text="", width=100)
not_to_buy_label.pack()
not_went_through_label = tk.Label(tab_stock_analysis, text="", width=100)
not_went_through_label.pack()

# Pack the notebook
notebook.pack()

# Start the GUI
root.mainloop()
