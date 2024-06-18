import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from forex_python.converter import CurrencyRates
import yfinance as yf

class CurrencyConverter:
    def _init_(self, root):
        self.root = root
        self.root.title("Currency Converter")

        # Currency conversion variables
        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()

        # GUI components
        ttk.Label(root, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(root, textvariable=self.amount_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(root, text="From Currency:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Combobox(root, textvariable=self.from_currency_var, values=self.get_currency_list()).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(root, text="To Currency:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Combobox(root, textvariable=self.to_currency_var, values=self.get_currency_list()).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(root, text="Convert", command=self.convert_currency).grid(row=3, column=0, columnspan=2, pady=10)

        # Matplotlib figure for graphical representation
        self.figure, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, pady=10)

    def get_currency_list(self):
        # Add or modify currencies as needed
        return ["INR", "USD", "AUD", "GBP", "JPY"]

    def convert_currency(self):
        try:
            amount = self.amount_var.get()
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            # Fetch real-time exchange rates
            c = CurrencyRates()
            exchange_rate = c.get_rate(from_currency, to_currency)

            converted_amount = amount * exchange_rate
            result_text = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"

            # Display result
            result_label = ttk.Label(self.root, text=result_text)
            result_label.grid(row=3, column=0, columnspan=2, pady=10)

            # Fetch historical exchange rates using yfinance
            data = yf.download(f"{from_currency}{to_currency}=X", start="2018-01-01", end="2023-01-01")
            data['Close'].plot(ax=self.ax, title=f"{from_currency}/{to_currency} Exchange Rate Over 5 Years")
            self.ax.set_xlabel("Date")
            self.ax.set_ylabel(f"{from_currency}/{to_currency} Exchange Rate")

            self.canvas.draw()

        except Exception as e:
            print(f"Error: {e}")

# Create Tkinter window
root = tk.Tk()
app = CurrencyConverter(root)
root.mainloop()