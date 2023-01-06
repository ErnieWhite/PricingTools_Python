import tkinter as tk

import adjustformula
import basisvalue
import calculateformulas
import convertformula


class App(tk.Tk):
    CALCULATE_FORMULA = 'Calculate Formula'
    FIND_BASIS = 'Find Basis Value'
    CONVERT_FORMULA = 'Convert Formula'
    ADJUST_FORMULA = 'Adjust Formula'

    def __init__(self) -> None:
        super().__init__()

        self.current_frame = None

        self.find_basis_value_frame = basisvalue.BasisValue(self)
        self.find_formulas_frame = calculateformulas.CalculateFormulas(self)
        self.formula_converter_frame = convertformula.ConvertFormula(self)
        self.adjust_formula_frame = adjustformula.AdjustFormula(self)

        menubar = tk.Menu()
        self.config(menu=menubar)

        view_menu = tk.Menu(menubar, tearoff=False)
        view_menu.add_command( label=App.FIND_BASIS, command=self.load_find_basis_value_frame)
        view_menu.add_command( label=App.CALCULATE_FORMULA, command=self.load_find_formulas_frame)
        view_menu.add_command( label=App.CONVERT_FORMULA, command=self.load_formula_converter_frame)
        view_menu.add_command( label=App.ADJUST_FORMULA, command=self.load_adjust_formula_frame)

        menubar.add_cascade( label='View', menu=view_menu, underline=0)

        self.load_formula_converter_frame()

    def swap_frames(self, frame):
        if self.current_frame is not None:
            self.current_frame.forget()
        self.current_frame = frame
        frame.pack(padx=10, pady=10)
        self.title('Pricing Tool - ' + frame.title)

    def load_find_formulas_frame(self):
        self.swap_frames(self.find_formulas_frame)

    def load_find_basis_value_frame(self):
        self.swap_frames(self.find_basis_value_frame)

    def load_formula_converter_frame(self):
        self.swap_frames(self.formula_converter_frame)

    def load_adjust_formula_frame(self):
        self.swap_frames(self.adjust_formula_frame)


if __name__ == '__main__':
    app = App()

    app.mainloop()
