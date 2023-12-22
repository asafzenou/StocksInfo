import tkinter as tk
import yfinance as yf

def get_company_info():
    """
    Get company information based on the provided company symbol.
    Retrieves various financial data using the yfinance library and displays it in the GUI.

    This function retrieves data such as Trailing EPS, Shares Outstanding, Free Cash Flow (FCF),
    Current Share Price, Operating Cash Flow, Tax Provision, and Capital Expenditure.

    Displays the results in the GUI.

    Raises:
    - Exception: If an error occurs during data retrieval.

    Returns:
    - None
    """
    company_symbol = entry_company_symbol.get()
    try:
        stock = yf.Ticker(company_symbol)
        eps = float(stock.info["trailingEps"])
        share_outstanding = stock.info["sharesOutstanding"]
        fcf = stock.info["freeCashflow"]
        current_share_price = stock.info["currentPrice"]
        operating_cash_flow = stock.info["operatingCashflow"]
        tax = stock.get_financials()[stock.get_financials().keys()[0]]["TaxProvision"]
        capital_exp = stock.get_cash_flow()[stock.get_cash_flow().keys()[0]]["CapitalExpenditure"]

        # Display the results in the GUI
        result_text.config(text=f"Capital Expenditure: {capital_exp}\n"
                                f"Tax: {tax}\n"
                                f"Operating Cash Flow: {operating_cash_flow}\n"
                                f"Current Share Price: {current_share_price}\n"
                                f"Free Cash Flow: {fcf}\n"
                                f"Shares Outstanding: {share_outstanding}\n"
                                f"Earnings Per Share (EPS): {eps}\n"
                                f"FCF Ratio: ?")  # You can calculate FCF Ratio

    except Exception as e:
        result_text.config(text=f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Get Company Info")

# Company symbol input
label_company_symbol = tk.Label(root, text="Enter company symbol:")
label_company_symbol.pack()
entry_company_symbol = tk.Entry(root)
entry_company_symbol.pack()

# Button to get company info
get_info_button = tk.Button(root, text="Get Company Info", command=get_company_info)
get_info_button.pack()

# Display results
result_text = tk.Label(root, text="")
result_text.pack()

# Start the GUI
root.mainloop()
