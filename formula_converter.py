"""

"""
import tkinter as tk
from tkinter import ttk

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
        self.current_formula_label = ttk.Label(self, text='Current')
        self.multiplier_formula_label = ttk.Label(self, text='Multiplier')
        self.discount_formula_label = ttk.Label(self, text='Discount')
        self.markup_formula_label = ttk.Label(self, text='Markup')
        self.gross_profit_formula_label = ttk.Label(self, text='Gross Profit')

        # create the entries
        self.current_formula_entry = ttk.Entry(self)
        self.multiplier_formula_entry = ttk.Entry(self)
        self.discount_formula_entry = ttk.Entry(self)
        self.markup_formula_entry = ttk.Entry(self)
        self.gross_profit_formula_entry = ttk.Entry(self)

        # create the copy buttons
        self.multiplier_formula_button = ttk.Button(self, text="Copy")
        self.discount_formula_button = ttk.Button(self, text="Copy")
        self.markup_formula_button = ttk.Button(self, text="Copy")
        self.gross_profit_formula_button = ttk.Button(self, text="Copy")

        self.place_widgets()
        self.setup_bindings()

        self.pack()

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
        self.current_formula_label.bind('<Return>', self.handle_formula_change_event)


    def handle_formula_change_event(self, event):
        value = event.widget.get()
        self.multiplier = utility.calculate_multiplier(value)

        print(value, self.multiplier)

    @staticmethod
    def validate(self, value):
        print(f'validate: {value}')
        return True

    @staticmethod
    def on_invalid(self):
        print('on invalid')


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Formula Converter")


if __name__ == '__main__':
    app = App()

    frame = ConverterFrame(app)

    app.mainloop()
