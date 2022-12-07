"""

"""
import tkinter as tk
from tkinter import ttk
import re
import pyperclip

import utility


class ConverterFrame(ttk.Frame):
    """

    """
    def __init__(self, container):
        """

        :param container:
        """
        super().__init__(container)

        self.multiplier = 0

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
        self.current_formula_entry = ttk.Entry(self)
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
        self.current_formula_label.grid(column=0, row=0, sticky='w')
        self.current_formula_entry.grid(column=1, row=0)

        # place the separator
        self.separator.grid(column=0, row=1, columnspan=3, pady=5, sticky='we')

        # place the multiplier widgets
        self.multiplier_formula_label.grid(column=0, row=2, sticky='w')
        self.multiplier_formula_entry.grid(column=1, row=2)
        self.multiplier_formula_button.grid(column=2, row=2)

        # place the discount widgets
        self.discount_formula_label.grid(column=0, row=3, sticky='w')
        self.discount_formula_entry.grid(column=1, row=3)
        self.discount_formula_button.grid(column=2, row=3)

        # place the markup widget
        self.markup_formula_label.grid(column=0, row=4, sticky='w')
        self.markup_formula_entry.grid(column=1, row=4)
        self.markup_formula_button.grid(column=2, row=4)

        # place the gross profit widgets
        self.gross_profit_formula_label.grid(column=0, row=5, sticky='w')
        self.gross_profit_formula_entry.grid(column=1, row=5)
        self.gross_profit_formula_button.grid(column=2, row=5)

    def setup_bindings(self):
        """

        :return:
        """
        self.current_formula_entry.bind('<Return>', self.handle_formula_change_event)

    def handle_formula_change_event(self, event):
        value = event.widget.get()
        self.multiplier = utility.calculate_multiplier(value)
        self.update_multiplier()
        self.update_discount()
        self.update_markup()
        self.update_gross_profit()

        print(value, self.multiplier)

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
    def validate(self, value: str) -> bool:
        value = value.upper()
        try:
            if value[0] in ['*', 'X', 'D']:
                return float(value[1:]) == float(value[1:])
            if value[0] in ['-', '+']:
                return float(value) == float(value)
        except (ZeroDivisionError, ValueError):
            return False
        print(f'validate: {value}')

    @staticmethod
    def on_invalid(self):
        print('on invalid')


if __name__ == '__main__':
    app = tk.Tk()

    app.title('Convert Formula')

    frame = ConverterFrame(app)
    frame.pack()

    app.mainloop()
