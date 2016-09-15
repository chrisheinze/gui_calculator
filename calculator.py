import tkinter as tk
import sympy
from sympy import SympifyError


class Calculator(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.expression = ''
        self.calc_exp_list = list()
        self.input_display_list = list()
        self.master.title('Calculator!')
        self.grid()

        self.input_display = tk.Label(self, text='', bg='white', width=35, height=2)
        self.input_display.grid(column=0, row=0, columnspan=4)

        self.output_display = tk.Label(self, text='', bg='white', width=35)
        self.output_display.grid(column=0, row=1, columnspan=4)

        # First Button Row
        self.button_lp = tk.Button(self, text='(', width=5, command=lambda: self.add_char('(', '('))
        self.button_lp.grid(column=0, row=2)

        self.button_rp = tk.Button(self, text=')', width=5, command=lambda: self.add_char(')', ')'))
        self.button_rp.grid(column=1, row=2)

        self.button_sqrt = tk.Button(self, text='√', width=5, command=lambda: self.add_char('√(', 'sqrt('))
        self.button_sqrt.grid(column=2, row=2)

        self.button_div = tk.Button(self, text='÷', width=5, command=lambda: self.add_char('÷', '/'))
        self.button_div.grid(column=3, row=2)

        # Second Button Row
        self.button_7 = tk.Button(self, text='7', width=5, command=lambda: self.add_char('7', '7'))
        self.button_7.grid(column=0, row=3)

        self.button_8 = tk.Button(self, text='8', width=5, command=lambda: self.add_char('8', '8'))
        self.button_8.grid(column=1, row=3)

        self.button_9 = tk.Button(self, text='9', width=5, command=lambda: self.add_char('9', '9'))
        self.button_9.grid(column=2, row=3)

        self.button_mul = tk.Button(self, text='×', width=5, command=lambda: self.add_char('×', '*'))
        self.button_mul.grid(column=3, row=3)

        # Third Button Row
        self.button_4 = tk.Button(self, text='4', width=5, command=lambda: self.add_char('4', '4'))
        self.button_4.grid(column=0, row=4)

        self.button_5 = tk.Button(self, text='5', width=5, command=lambda: self.add_char('5', '5'))
        self.button_5.grid(column=1, row=4)

        self.button_6 = tk.Button(self, text='6', width=5, command=lambda: self.add_char('6', '6'))
        self.button_6.grid(column=2, row=4)

        self.button_minus = tk.Button(self, text='-', width=5, command=lambda: self.add_char('-', '-'))
        self.button_minus.grid(column=3, row=4)

        # Fourth Button Row
        self.button_1 = tk.Button(self, text='1', width=5, command=lambda: self.add_char('1', '1'))
        self.button_1.grid(column=0, row=5)

        self.button_2 = tk.Button(self, text='2', width=5, command=lambda: self.add_char('2', '2'))
        self.button_2.grid(column=1, row=5)

        self.button_3 = tk.Button(self, text='3', width=5, command=lambda: self.add_char('3', '3'))
        self.button_3.grid(column=2, row=5)

        self.button_plus = tk.Button(self, text='+', width=5, command=lambda: self.add_char('+', '+'))
        self.button_plus.grid(column=3, row=5)

        # Fifth Button Row
        self.button_0 = tk.Button(self, text='0', width=5, command=lambda: self.add_char('0', '0'))
        self.button_0.grid(column=0, row=6)

        self.button_dec = tk.Button(self, text='.', width=5, command=lambda: self.add_char('.', '.'))
        self.button_dec.grid(column=1, row=6)

        self.button_back = tk.Button(self, text='Back', width=5, command=lambda: self.backspace())
        self.button_back.grid(column=2, row=6)

        self.button_back = tk.Button(self, text='Clear', width=5, command=lambda: self.clear())
        self.button_back.grid(column=3, row=6)

        # Fifth Button Row
        self.button_equal = tk.Button(self, text='Calculate!', width=10, command=lambda: self.eval_exp_new(False))
        self.button_equal.grid(column=0, row=7, columnspan=2)

        self.button_clear = tk.Button(self, text='Dec.', width=10, command=lambda: self.eval_exp_new(True))
        self.button_clear.grid(column=2, row=7, columnspan=2)

        self.info_bar = tk.Label(self, text='Calculator V1.0')
        self.info_bar.grid(column=0, row=8, columnspan=4)

    def add_char(self, display_val, act_val):
        self.input_display_list.append(display_val)
        self.calc_exp_list.append(act_val)
        self.input_display['text'] = ''.join(i for i in self.input_display_list)
        print(self.input_display_list, '|', self.calc_exp_list)

    def backspace(self):
        self.input_display_list = self.input_display_list[:-1]
        self.calc_exp_list = self.calc_exp_list[:-1]
        self.input_display['text'] = ''.join(i for i in self.input_display_list)
        print(self.input_display_list, '|', self.calc_exp_list)

    def clear(self):
        self.input_display_list, self.calc_exp_list = list(), list()
        self.input_display['text'], self.output_display['text'] = '', ''
        print(self.input_display_list, '|', self.calc_exp_list)

    def eval_exp_new(self, dec):
        self.expression = ''
        print(self.input_display_list, '|', self.calc_exp_list)
        for exp in self.calc_exp_list:
            self.expression += exp
        if dec:
            try:
                self.output_display['text'] = sympy.N(sympy.sympify(self.expression))
            except SympifyError:
                self.output_display['text'] = 'ERROR, bro!'
        else:
            try:
                self.output_display['text'] = sympy.sympify(self.expression)
            except SympifyError:
                self.output_display['text'] = 'ERROR, bro!'


def main():
    Calculator().mainloop()

main()
