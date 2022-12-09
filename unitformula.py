import tkinter as tk
from tkinter import ttk
import utility
import pyperclip
import re


class UnitFormulaFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        self.multiplier = 0

        float_vcmd = (self.register(self.validate_float), '%P')
        formula_vcmd = (self.register(self.validate_formula), '%P')
        ivcmd = (self.register(self.on_invalid), )

        self.unit_price_var = tk.StringVar()
        self.formula_var = tk.StringVar()
        self.basis_price_var = tk.StringVar()

        # create the widgets
        self.unit_price_label = ttk.Label(self, text='Unit Price')
        self.formula_label = ttk.Label(self, text='Formula')
        self.calculated_basis_label = ttk.Label(self, text='Basis Value')
        self.copy_button = ttk.Button(self, text='Copy')

        self.unit_price_entry = ttk.Entry(self, textvariable=self.unit_price_var)
        self.formula_entry = ttk.Entry(self, textvariable=self.formula_var)
        self.calculated_basis_entry = ttk.Entry(self, state='readonly', textvariable=self.basis_price_var)

        self.unit_price_label.grid(row=0, column=0, sticky='w')
        self.unit_price_entry.grid(row=0, column=1, sticky='we')

        self.formula_label.grid(row=1, column=0, sticky='w')
        self.formula_entry.grid(row=1, column=1, sticky='we')

        self.calculated_basis_label.grid(row=2, column=0, sticky='w')
        self.calculated_basis_entry.grid(row=2, column=1, sticky='we')
        self.copy_button.grid(row=3, column=1, sticky='we')

    def validate_float(self, value):
        if value == '':
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False

    def validate_formula(self, value):
        print('validate')
        if value == '':
            return True
        value = value.upper()
        if re.search(r'^[\*,X,D][-,\+]?\d*\.?\d*$', value):
            return True
        if re.search(r'^[-,\+]?\d*\.?\d*$', value):
            return True
        if value == 'G' or re.search(r'^GP[-,\+]?\d*\.?\d*$', value):
            return True
        return False

    def update_basis_price(self):
        basis_price = self.unit_price_var.get * self.muliplier

    def on_invalid(self):
        pass


if __name__ == '__main__':
    app = tk.Tk()

    app.title('Find Basis Value')

    frame = UnitFormulaFrame(app)
    frame.pack()

    app.mainloop()
