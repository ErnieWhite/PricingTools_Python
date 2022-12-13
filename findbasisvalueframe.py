import tkinter as tk
from tkinter import ttk
import utility
import pyperclip
import re


class FindBasisValueFrame(ttk.Frame):
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
        self.copy_button = ttk.Button(self, text='Copy', command=self.copy_basis_price)

        self.unit_price_entry = ttk.Entry(
            self,
            textvariable=self.unit_price_var,
            validate='key',
            validatecommand=float_vcmd,
            invalidcommand=ivcmd,
        )
        self.formula_entry = ttk.Entry(
            self,
            textvariable=self.formula_var,
            validate='key',
            validatecommand=formula_vcmd,
            invalidcommand=ivcmd,
        )
        self.calculated_basis_entry = ttk.Entry(self, state='readonly', textvariable=self.basis_price_var)

        self.unit_price_label.grid(row=0, column=0, sticky='w')
        self.unit_price_entry.grid(row=0, column=1, sticky='we')

        self.formula_label.grid(row=1, column=0, sticky='w')
        self.formula_entry.grid(row=1, column=1, sticky='we')

        self.calculated_basis_label.grid(row=2, column=0, sticky='w')
        self.calculated_basis_entry.grid(row=2, column=1, sticky='we')
        self.copy_button.grid(row=3, column=1, sticky='we')

        self.unit_price_var.trace_add('write', self.update_basis_price)
        self.formula_var.trace_add('write', self.update_basis_price)

    @staticmethod
    def validate_float(value):
        if value == '':
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_formula(value):
        print(f'validate: formula {value}')
        if value == '':
            return True
        value = value.upper()
        if re.search(r'^[*XD][-+]?\d*\.?\d*$', value):
            return True
        if re.search(r'^[-+]\d*\.?\d*$', value):
            return True
        if value == 'G' or re.search(r'^GP[-+]?\d*\.?\d*$', value):
            return True
        return False

    def update_basis_price(self, *args):
        print('update basis price')
        self.formula_var.set(self.formula_var.get().upper())
        if not utility.valid_formula(self.formula_var.get()):
            self.clear_basis()
            return
        if self.unit_price_var.get() == '' or self.formula_var.get() == '':
            self.clear_basis()
            return
        self.multiplier = utility.calculate_multiplier(self.formula_var.get())
        if self.multiplier == 0:
            self.clear_basis()
            return
        self.basis_price_var.set(str(float(self.unit_price_var.get()) / self.multiplier))

    def clear_basis(self):
        self.basis_price_var.set('')

    def on_invalid(self):
        pass

    def copy_basis_price(self):
        pyperclip.copy(self.basis_price_var.get())


if __name__ == '__main__':
    app = tk.Tk()

    app.title('Find Basis Value')

    frame = FindBasisValueFrame(app)
    frame.pack()

    app.mainloop()
