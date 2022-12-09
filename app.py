import tkinter as tk

import unitformula
import formulaconverter
import unitbasisframe


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.current_frame = None

        self.unit_formula_frame = unitformula.UnitFormulaFrame(self)
        self.unit_basis_frame = unitbasisframe.UnitBasisFrame(self)
        self.formula_converter_frame = formulaconverter.ConverterFrame(self)

        menubar = tk.Menu()
        self.config(menu=menubar)

        view_menu = tk.Menu(menubar, tearoff=False)
        view_menu.add_command(
            label='Unit Formula',
            command=self.load_unit_formula_frame,
        )
        view_menu.add_command(
            label='Unit Basis',
            command=self.load_unit_basis_frame,
        )
        view_menu.add_command(
            label='Formula Converter',
            command=self.load_formula_converter_frame,
        )

        menubar.add_cascade(
            label='View',
            menu=view_menu,
            underline=0
        )

        self.load_unit_basis_frame()

    def load_unit_basis_frame(self):
        if self.current_frame:
            self.current_frame.forget()
        self.current_frame = self.unit_basis_frame
        self.current_frame.pack()
        self.title('Pricing Tool - Unit Basis')

    def load_unit_formula_frame(self):
        if self.current_frame:
            self.current_frame.forget()
        self.current_frame = self.unit_formula_frame
        self.current_frame.pack()
        self.title('Pricing Tool - Unit Formula')

    def load_formula_converter_frame(self):
        if self.current_frame:
            self.current_frame.forget()
        self.current_frame = self.formula_converter_frame
        self.current_frame.pack()
        self.title('Pricing Tool - Formula Converter')


if __name__ == '__main__':
    app = App()

    app.mainloop()
