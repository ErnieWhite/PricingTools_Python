import tkinter as tk
from tkinter import ttk


class AdjustFormulaFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # create the stringvars
        self.spinner_value = tk.DoubleVar(value=0)

        # create the labels
        ttk.Label(self, text="Unit Price").grid(row=0, column=0)
        ttk.Label(self, text="Unit Cost").grid(row=1, column=0)
        ttk.Label(self, text="Basis Value").grid(row=2, column=0)
        ttk.Label(self, text="Decimals").grid(row=3, column=0)
        ttk.Label(self, text="GM Adjustment").grid(row=4, column=0)

        ttk.Label(self, text="Multiplier").grid(row=0, column=3)
        ttk.Label(self, text="Discount").grid(row=1, column=3)
        ttk.Label(self, text="Markup").grid(row=2, column=3)
        ttk.Label(self, text="Gross Profit").grid(row=3, column=3)

        # create the entry widgets
        self.unit_price_entry = ttk.Entry(self)
        self.basis_value_entry = ttk.Entry(self)
        self.unit_cost_entry = ttk.Entry(self)

        # create the margin spinner
        self.margin_spinner = ttk.Spinbox(self, textvariable=self.spinner_value)

        # create the decimals combobox
        item_list = ("Auto", "1", "2", "3", "4", "5", "6")
        self.decimals_combo = ttk.Combobox(self, values=item_list)

        # create the formula display widgets


if __name__ == "__main__":
    app = tk.Tk()
    frame = AdjustFormulaFrame(app)
    app.mainloop()
