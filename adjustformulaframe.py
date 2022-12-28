import tkinter as tk
from tkinter import ttk


class AdjustFormulaFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # create the tk vars
        self.spinner_value = tk.DoubleVar(value=0)

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
        self.multiplier_display = ttk.Entry(self, state="readonly")
        self.discount_display = ttk.Entry(self, state="readonly")
        self.markup_display = ttk.Entry(self, state="readonly")
        self.gross_profit_display = ttk.Entry(self, state="readonly")

        self.place_widgets()

        self.grid(row=0, column=0)

    def place_widgets(self):
        ttk.Label(self, text="Unit Price").grid(row=0, column=0)
        self.unit_price_entry.grid(row=0, column=1)
        ttk.Label(self, text="Unit Cost").grid(row=1, column=0)
        self.unit_cost_entry.grid(row=1, column=1)
        ttk.Label(self, text="Basis Value").grid(row=2, column=0)
        self.basis_value_entry.grid(row=2, column=1)
        ttk.Label(self, text="Decimals").grid(row=3, column=0)
        self.decimals_combo.grid(row=3, column=1)
        ttk.Label(self, text="GM Adjustment").grid(row=4, column=0)
        self.margin_spinner.grid(row=4, column=1)

        ttk.Label(self, text="Multiplier").grid(row=0, column=3)
        self.multiplier_display.grid(row=0, column=4)
        ttk.Label(self, text="Discount").grid(row=1, column=3)
        self.discount_display.grid(row=1, column=4)
        ttk.Label(self, text="Markup").grid(row=2, column=3)
        self.markup_display.grid(row=2, column=4)
        ttk.Label(self, text="Gross Profit").grid(row=3, column=3)
        self.gross_profit_display.grid(row=3, column=4)


if __name__ == "__main__":
    app = tk.Tk()
    frame = AdjustFormulaFrame(app)
    app.mainloop()
