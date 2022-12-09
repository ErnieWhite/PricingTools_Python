import tkinter as tk
from tkinter import ttk
import utility
import pyperclip


class UnitBasisFrame(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        vcmd = (self.register(self.validate), '%P')
        ivcmd = (self.register(self.on_invalid), )

        # create StringVar
        self.unit_price_var = tk.StringVar()
        self.basis_value_var = tk.StringVar()
        self.decimals_var = tk.StringVar()

        self.multiplier_var = tk.StringVar()
        self.discount_var = tk.StringVar()
        self.markup_var = tk.StringVar()
        self.gross_profit_var = tk.StringVar()

        # create the widgets
        self.unit_price_label = ttk.Label(self, text='Unit Price')
        self.basis_value_label = ttk.Label(self, text='Basis Value')
        self.decimals_label = ttk.Label(self, text='Decimals')

        self.unit_price_entry = ttk.Entry(
            self,
            validate='key',
            textvariable=self.unit_price_var,
            validatecommand=vcmd,
            invalidcommand=ivcmd,
        )
        self.basis_value_entry = ttk.Entry(
            self,
            validate='key',
            textvariable=self.basis_value_var,
            validatecommand=vcmd,
            invalidcommand=ivcmd,
        )
        self.decimals_combo = ttk.Combobox(
            self,
            values=('Auto', '1', '2', '3', '4', '5', '6'),
            textvariable=self.decimals_var,
        )
        self.decimals_combo.set('Auto')

        self.multiplier_formula_entry = ttk.Entry(self, textvariable=self.multiplier_var, state='readonly')
        self.discount_formula_entry = ttk.Entry(self, textvariable=self.discount_var, state='readonly')
        self.markup_formula_entry = ttk.Entry(self, textvariable=self.markup_var, state='readonly')
        self.gross_profit_formula_entry = ttk.Entry(self, textvariable=self.gross_profit_var, state='readonly')

        self.multiplier_formula_copy_button = ttk.Button(self, text='Copy', command=self.copy_multiplier_formula)
        self.discount_formula_copy_button = ttk.Button(self, text='Copy', command=self.copy_discount_formula)
        self.markup_formula_copy_button = ttk.Button(self, text='Copy', command=self.copy_markup_formula)
        self.gross_profit_formula_copy_button = ttk.Button(self, text='Copy', command=self.copy_gross_profit_formula)

        self.unit_price_label.grid(row=0, column=0, sticky='w')
        self.unit_price_entry.grid(row=0, column=1, sticky='ew')
        self.multiplier_formula_entry.grid(row=0, column=2, sticky='ew')
        self.multiplier_formula_copy_button.grid(row=0, column=3)

        self.basis_value_label.grid(row=1, column=0, sticky='w')
        self.basis_value_entry.grid(row=1, column=1, sticky='ew')
        self.discount_formula_entry.grid(row=1, column=2, sticky='ew')
        self.discount_formula_copy_button.grid(row=1, column=3)

        self.decimals_label.grid(row=2, column=0, sticky='w')
        self.decimals_combo.grid(row=2, column=1, sticky='ew')
        self.markup_formula_entry.grid(row=2, column=2, sticky='ew')
        self.markup_formula_copy_button.grid(row=2, column=3)

        self.gross_profit_formula_entry.grid(row=3, column=2, sticky='ew')
        self.gross_profit_formula_copy_button.grid(row=3, column=3)

        self.unit_price_var.trace('w', self.update_formulas)
        self.basis_value_var.trace('w', self.update_formulas)


    def update_formulas(self, var, index, mode):
        if not self.unit_price_var.get() or not self.basis_value_var.get():
            self.clear_formulas()
            return
        if float(self.unit_price_var.get()) == 0 or float(self.basis_value_var.get()) == 0:
            self.clear_formulas()
            return
        multiplier = float(self.unit_price_var.get()) / float(self.basis_value_var.get())
        multiplier_formula = utility.find_multiplier_formula(multiplier)
        discount_formula = utility.find_discount_formula(multiplier)
        markup_formula = utility.find_markup_formula(multiplier)
        gross_profit_formula = utility.find_gross_profit_formula(multiplier)
        self.multiplier_var.set(multiplier_formula)
        self.discount_var.set(discount_formula)
        self.markup_var.set(markup_formula)
        self.gross_profit_var.set(gross_profit_formula)

    @staticmethod
    def validate(value) -> bool:
        if value == '':
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False

    def copy_multiplier_formula(self):
        pyperclip.copy(self.multiplier_var.get())

    def copy_discount_formula(self):
        pyperclip.copy(self.discount_var.get())

    def copy_markup_formula(self):
        pyperclip.copy(self.markup_var.get())

    def copy_gross_profit_formula(self):
        pyperclip.copy(self.gross_profit_var.get())

    def clear_formulas(self):
        self.multiplier_var.set('')
        self.discount_var.set('')
        self.markup_var.set('')
        self.gross_profit_var.set('')

    def on_invalid(self):
        pass



if __name__ == '__main__':
    app = tk.Tk()

    app.title('Find Formula')

    frame = UnitBasisFrame(app)
    frame.pack()

    app.mainloop()
