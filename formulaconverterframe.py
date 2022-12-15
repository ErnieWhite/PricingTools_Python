"""

"""
import tkinter as tk
from tkinter import ttk
import re
import pyperclip

import utility


class FormulaConverterFrame(ttk.Frame):
    """

    """
    def __init__(self, container):
        """

        :param container:
        """
        super().__init__(container)
        vcmd = (self.register(self.validate), '%P')
        ivcmd = (self.register(self.on_invalid),)

        self.multiplier = 0

        # create the formula StringVar
        self.formula_string_var = tk.StringVar()

        # create the separator
        self.separator = ttk.Separator(self, orient='horizontal')

        # create the labels
        self.current_formula_label = ttk.Label(self, text='Formula')
        self.multiplier_formula_label = ttk.Label(self, text='Multiplier')
        self.discount_formula_label = ttk.Label(self, text='Discount')
        self.markup_formula_label = ttk.Label(self, text='Markup')
        self.gross_profit_formula_label = ttk.Label(self, text='Gross Profit')

        # create the StringVars
        self.multiplier_string_var = tk.StringVar()
        self.discount_string_var = tk.StringVar()
        self.markup_string_var = tk.StringVar()
        self.gross_profit_string_var = tk.StringVar()

        # create the entries
        self.current_formula_entry = ttk.Entry(
            self,
            validate='key',
            textvariable=self.formula_string_var,
            validatecommand=vcmd,
            invalidcommand=ivcmd,
        )
        self.multiplier_formula_entry = ttk.Entry(self, textvariable=self.multiplier_string_var, state='readonly')
        self.discount_formula_entry = ttk.Entry(self, textvariable=self.discount_string_var, state='readonly')
        self.markup_formula_entry = ttk.Entry(self, textvariable=self.markup_string_var, state='readonly')
        self.gross_profit_formula_entry = ttk.Entry(self, textvariable=self.gross_profit_string_var, state='readonly')

        # create the copy buttons
        self.multiplier_formula_button = ttk.Button(self, text="Copy", command=self.copy_multiplier_formula)
        self.discount_formula_button = ttk.Button(self, text="Copy", command=self.copy_discount_formula)
        self.markup_formula_button = ttk.Button(self, text="Copy", command=self.copy_markup_formula)
        self.gross_profit_formula_button = ttk.Button(self, text="Copy", command=self.copy_gross_profit_formula)

        self.place_widgets()
        self.setup_bindings()

    def place_widgets(self):
        """

        :return:
        """
        # place the current widget
        self.current_formula_label.grid(column=0, row=0, sticky='w', padx=2, pady=2)
        self.current_formula_entry.grid(column=1, row=0, padx=2, pady=2)

        # place the separator
        self.separator.grid(column=0, row=1, columnspan=3, pady=5, sticky='we')

        # place the multiplier widgets
        self.multiplier_formula_label.grid(column=0, row=2, sticky='w', padx=2, pady=2)
        self.multiplier_formula_entry.grid(column=1, row=2, padx=2, pady=2)
        self.multiplier_formula_button.grid(column=2, row=2, padx=2, pady=2)

        # place the discount widgets
        self.discount_formula_label.grid(column=0, row=3, sticky='w', padx=2, pady=2)
        self.discount_formula_entry.grid(column=1, row=3, padx=2, pady=2)
        self.discount_formula_button.grid(column=2, row=3, padx=2, pady=2)

        # place the markup widget
        self.markup_formula_label.grid(column=0, row=4, sticky='w', padx=2, pady=2)
        self.markup_formula_entry.grid(column=1, row=4, padx=2, pady=2)
        self.markup_formula_button.grid(column=2, row=4, padx=2, pady=2)

        # place the gross profit widgets
        self.gross_profit_formula_label.grid(column=0, row=5, sticky='w', padx=2, pady=2)
        self.gross_profit_formula_entry.grid(column=1, row=5, padx=2, pady=2)
        self.gross_profit_formula_button.grid(column=2, row=5, padx=2, pady=2)

    def setup_bindings(self):
        """

        :return:
        """
        # self.current_formula_entry.bind('<Return>', self.handle_formula_change_event)
        self.formula_string_var.trace('w', self.handle_formula_change_event)

    def handle_formula_change_event(self, *_):
        value = self.formula_string_var.get()
        value = value.upper()
        self.formula_string_var.set(value)

        print(value, utility.valid_formula(value))
        if utility.valid_formula(value):
            self.multiplier = utility.calculate_multiplier(value)
            self.update_multiplier()
            self.update_discount()
            self.update_markup()
            self.update_gross_profit()
        else:
            self.clear_calculated_formulas()

    def clear_calculated_formulas(self):
        self.multiplier_string_var.set('')
        self.discount_string_var.set('')
        self.markup_string_var.set('')
        self.gross_profit_string_var.set('')

    def update_multiplier(self):
        self.multiplier_string_var.set(utility.find_multiplier_formula(self.multiplier))

    def update_discount(self):
        self.discount_string_var.set(utility.find_discount_formula(self.multiplier))

    def update_markup(self):
        self.markup_string_var.set(utility.find_markup_formula(self.multiplier))

    def update_gross_profit(self):
        self.gross_profit_string_var.set(utility.find_gross_profit_formula(self.multiplier))

    def copy_multiplier_formula(self):
        pyperclip.copy(self.multiplier_formula_entry.get())

    def copy_discount_formula(self):
        pyperclip.copy(self.discount_formula_entry.get())

    def copy_markup_formula(self):
        pyperclip.copy(self.markup_formula_entry.get())

    def copy_gross_profit_formula(self):
        pyperclip.copy(self.gross_profit_formula_entry.get())

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

    app.title('Convert Formula')

    frame = FormulaConverterFrame(app)
    frame.pack()

    app.mainloop()