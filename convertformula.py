import tkinter as tk
from tkinter import ttk
import re
import pyperclip

import utility


class ConvertFormula(ttk.Frame):
    def __init__(self, container):
        """

        :param container:
        """
        super().__init__(container)

        self.title = 'Convert Formula'

        vcmd = (self.register(self.validate), '%P')
        ivcmd = (self.register(self.on_invalid),)

        # create the StringVars
        self.formula_string_var = tk.StringVar()
        self.decimals_var = tk.StringVar()
        self.multiplier_var = tk.StringVar()
        self.discount_var = tk.StringVar()
        self.markup_var = tk.StringVar()
        self.gross_profit_var = tk.StringVar()

        # create the separator
        self.separator = ttk.Separator(self, orient=tk.VERTICAL)

        # create the entries
        self.current_formula_entry = ttk.Entry(
            self,
            validate='key',
            textvariable=self.formula_string_var,
            validatecommand=vcmd,
            invalidcommand=ivcmd,
        )
        self.multiplier_formula_entry = ttk.Entry(self, textvariable=self.multiplier_var, state='readonly')
        self.discount_formula_entry = ttk.Entry(self, textvariable=self.discount_var, state='readonly')
        self.markup_formula_entry = ttk.Entry(self, textvariable=self.markup_var, state='readonly')
        self.gross_profit_formula_entry = ttk.Entry(self, textvariable=self.gross_profit_var, state='readonly')

        # create the combobox
        combo_items = ('Auto', '1', '2', '3', '4', '5', '6')
        self.decimals = ttk.Combobox(self, values=combo_items)

        # create the copy buttons
        # TODO: Replace the text with an image
        self.multiplier_formula_button = ttk.Button(
            self,
            text="Copy",
            command=lambda: self.copy_formula(self.multiplier_var),
        )
        self.discount_formula_button = ttk.Button(
            self,
            text="Copy",
            command=lambda: self.copy_formula(self.discount_var),
        )
        self.markup_formula_button = ttk.Button(
            self,
            text="Copy",
            command=lambda: self.copy_formula(self.markup_var),
        )
        self.gross_profit_formula_button = ttk.Button(
            self,
            text="Copy",
            command=lambda: self.copy_formula(self.gross_profit_var),
        )

        self.place_widgets()
        self.setup_bindings()

    def place_widgets(self):

        # place the formula widgets
        ttk.Label(self, text='Formula').grid(column=0, row=0, sticky='w', padx=2, pady=2)
        self.current_formula_entry.grid(column=1, row=0, padx=2, pady=2, sticky='ew')

        ttk.Label(self, text='Decimals').grid(column=0, row=1, sticky='w', padx=2, pady=2)
        self.decimals.grid(column=1, row=1, padx=2, pady=2, sticky='ew')
        self.decimals.current(0)

        # place the separator
        self.separator.grid(column=2, row=0, rowspan=6, pady=5, sticky='ns')

        # place the multiplier widgets
        ttk.Label(self, text='Multiplier').grid(column=3, row=0, sticky='w', padx=2, pady=2)
        self.multiplier_formula_entry.grid(column=4, row=0, padx=2, pady=2, sticky='ew')
        self.multiplier_formula_button.grid(column=5, row=0, padx=2, pady=2)

        # place the discount widgets
        ttk.Label(self, text='Discount').grid(column=3, row=1, sticky='w', padx=2, pady=2)
        self.discount_formula_entry.grid(column=4, row=1, padx=2, pady=2, sticky='ew')
        self.discount_formula_button.grid(column=5, row=1, padx=2, pady=2)

        # place the markup widget
        ttk.Label(self, text='Markup').grid(column=3, row=2, sticky='w', padx=2, pady=2)
        self.markup_formula_entry.grid(column=4, row=2, padx=2, pady=2, sticky='ew')
        self.markup_formula_button.grid(column=5, row=2, padx=2, pady=2)

        # place the gross profit widgets
        ttk.Label(self, text='Gross Profit').grid(column=3, row=3, sticky='w', padx=2, pady=2)
        self.gross_profit_formula_entry.grid(column=4, row=3, padx=2, pady=2, sticky='ew')
        self.gross_profit_formula_button.grid(column=5, row=3, padx=2, pady=2)

    def setup_bindings(self):
        self.formula_string_var.trace('w', self.handle_formula_change_event)
        self.decimals_var.trace('w', self.handle_formula_change_event)

    def handle_formula_change_event(self, *_):
        value = self.formula_string_var.get()
        value = value.upper()
        self.formula_string_var.set(value)

        self.clear_calculated_formulas()
        if utility.valid_formula(value):
            multiplier = utility.calculate_multiplier(value)
            self.multiplier_var.set(utility.find_multiplier_formula(multiplier))
            self.discount_var.set(utility.find_discount_formula(multiplier))
            self.markup_var.set(utility.find_markup_formula(multiplier))
            self.gross_profit_var.set(utility.find_gross_profit_formula(multiplier))

    def clear_calculated_formulas(self):
        self.multiplier_var.set('')
        self.discount_var.set('')
        self.markup_var.set('')
        self.gross_profit_var.set('')

    @staticmethod
    def copy_formula(string_var):
        pyperclip.copy(string_var.get())

    @staticmethod
    def validate(value) -> bool:
        print('validate')
        if value == '':
            return True
        value = value.upper()
        if re.search(r'^[*XD][-,+]?\d*\.?\d*$', value):
            return True
        if re.search(r'^[-+]\d*\.?\d*$', value):
            return True
        if value == 'G' or re.search(r'^GP[-+]?\d*\.?\d*$', value):
            return True
        return False

    @staticmethod
    def on_invalid():
        print('on invalid')


if __name__ == '__main__':
    app = tk.Tk()

    frame = ConvertFormula(app)
    frame.pack()
    app.title(frame.title)

    app.mainloop()
