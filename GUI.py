from customtkinter import *
from colors import *
from functools import partial


# Modified from https://python-hub.com/calculator-app-in-python-customtkinter/
class Calculator(CTk):
    # BUTTON TEXT
    list_buttons = ['AC', '+/-', '%', '÷', 'X', '-', '+', '=', ',']

    def __init__(self):
        super().__init__()
        # Screen variables
        self.title("Calculator")
        self.geometry("365x255")  # "400x250"
        self.configure(fg_color=BG_COLOR)
        self.configure(text_color=WHITE)

        # Label Widgets attributes
        self.entry_width = 400  # width of Entry widgets
        self.entry_height = 50
        self.sticky = "NSEW"

        self.display = CTkEntry(master=self, width=self.entry_width, height=self.entry_height,
                                fg_color=BLACK, font=('Arial', 25), placeholder_text='')
        self.display.grid(row=0, column=0, columnspan=11, sticky=self.sticky)

        # Number Button Widgets attributes
        self.button_width = int(self.entry_width / 4 - 20)  # width of Button widget
        self.col = 0  # for scientific calculater self.col = 7

        # Button 7
        self.button_7 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                  fg_color=GRAY, text_color=WHITE,
                                  text='7', command=partial(self.set_number, '7'))
        self.button_7.grid(row=2, column=0 + self.col, sticky=self.sticky, padx=3, pady=3)

        # Button 8
        self.button_8 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                  fg_color=GRAY, text_color=WHITE,
                                  text='8', command=partial(self.set_number, '8'))
        self.button_8.grid(row=2, column=1 + self.col, sticky=self.sticky, padx=3, pady=3)

        # Button 9
        self.button_9 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                  fg_color=GRAY, text_color=WHITE,
                                  text='9', command=partial(self.set_number, '9'))
        self.button_9.grid(row=2, column=2 + self.col, sticky=self.sticky, padx=3, pady=3)

        # Button 4
        self.button_4 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                  fg_color=GRAY, text_color=WHITE,
                                  text='4', command=partial(self.set_number, '4'))
        self.button_4.grid(row=3, column=0 + self.col, sticky=self.sticky, padx=3, pady=3)

        # Button 5
        self.button_5 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                  fg_color=GRAY, text_color=WHITE,
                                  text='5', command=partial(self.set_number, '5'))
        self.button_5.grid(row=3, column=1 + self.col, sticky=self.sticky, padx=3, pady=3)

        # Button 6
        self.button_6 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                  fg_color=GRAY, text_color=WHITE,
                                  text='6', command=partial(self.set_number, '6'))
        self.button_6.grid(row=3, column=2 + self.col, sticky=self.sticky, padx=3, pady=3)

        # Button 1
        self.button_1 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                  fg_color=GRAY, text_color=WHITE,
                                  text='1', command=partial(self.set_number, '1'))
        self.button_1.grid(row=4, column=0 + self.col, sticky=self.sticky, padx=3, pady=3)

        # Button 2
        self.button_2 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                  fg_color=GRAY, text_color=WHITE,
                                  text='2', command=partial(self.set_number, '2'))
        self.button_2.grid(row=4, column=1 + self.col, sticky=self.sticky, padx=3, pady=3)

        # Button 3
        self.button_3 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                  fg_color=GRAY, text_color=WHITE,
                                  text='3', command=partial(self.set_number, '3'))
        self.button_3.grid(row=4, column=2 + self.col, sticky=self.sticky, padx=3, pady=3)

        # Button 0
        self.button_0 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                  fg_color=GRAY, text_color=WHITE,
                                  text='0', command=partial(self.set_number, '0'))
        self.button_0.grid(row=5, column=0 + self.col, columnspan=2, sticky=self.sticky, padx=3, pady=3)

        # Operations Button Widgets attributes
        ## First Row
        self.op_button_1 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                     text=Calculator.list_buttons[0], command=self.all_clear,
                                     fg_color=GRAFFITE, text_color=WHITE)
        self.op_button_1.grid(row=1, column=0 + self.col, sticky=self.sticky, padx=3, pady=3)
        self.op_button_2 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                     text=Calculator.list_buttons[1], command=partial(self.operate, '+/-'),
                                     fg_color=GRAFFITE, text_color=WHITE)
        self.op_button_2.grid(row=1, column=1 + self.col, sticky=self.sticky, padx=3, pady=3)
        self.op_button_3 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                     text=Calculator.list_buttons[2], command=partial(self.operate, '%'),
                                     fg_color=GRAFFITE, text_color=WHITE)
        self.op_button_3.grid(row=1, column=2 + self.col, sticky=self.sticky, padx=3, pady=3)
        self.op_button_4 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                     text=Calculator.list_buttons[3], command=partial(self.operate, '÷'),
                                     fg_color=ORANGE, text_color=BLACK)
        self.op_button_4.grid(row=1, column=3 + self.col, sticky=self.sticky, padx=3, pady=3)

        ## Last Column
        self.op_button_5 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                     text=Calculator.list_buttons[4], command=partial(self.operate, 'X'),
                                     fg_color=ORANGE, text_color=BLACK)
        self.op_button_5.grid(row=2, column=3 + self.col, sticky=self.sticky, padx=3, pady=3)
        self.op_button_6 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                     text=Calculator.list_buttons[5], command=partial(self.operate, '-'),
                                     fg_color=ORANGE, text_color=BLACK)
        self.op_button_6.grid(row=3, column=3 + self.col, sticky=self.sticky, padx=3, pady=3)
        self.op_button_7 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                     text=Calculator.list_buttons[6], command=partial(self.operate, '+'),
                                     fg_color=ORANGE, text_color=BLACK)
        self.op_button_7.grid(row=4, column=3 + self.col, sticky=self.sticky, padx=3, pady=3)
        self.op_button_8 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                     text=Calculator.list_buttons[7], command=self.evaluate,
                                     fg_color=ORANGE, text_color=BLACK)
        self.op_button_8.grid(row=5, column=3 + self.col, sticky=self.sticky, padx=3, pady=3)

        ## Comma Button
        self.op_button_9 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
                                     text=Calculator.list_buttons[8], command=self.comma,
                                     fg_color=GRAY, text_color=WHITE)
        self.op_button_9.grid(row=5, column=2 + self.col, sticky=self.sticky, padx=3, pady=3)

        ## Scientific Buttons
        # self.op_button_10 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
        #                              text=f'2\N{SUPERSCRIPT }', command=self.change_buttons,
        #                              fg_color=GRAFFITE, text_color=WHITE)
        # self.op_button_10.grid(row=2, column=0, sticky=self.sticky, padx=3, pady=3)
        #
        # self.op_button_11 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
        #                              text=f'x\N{SUPERSCRIPT TWO}', command=self.all_clear,
        #                              fg_color=GRAFFITE, text_color=WHITE)
        # self.op_button_11.grid(row=2, column=1, sticky=self.sticky, padx=3, pady=3)
        #
        # self.op_button_12 = CTkButton(master=self, width=self.button_width, font=('Arial', 25),
        #                              text=f'x\N{SUPERSCRIPT THREE}', command=self.all_clear,
        #                              fg_color=GRAFFITE, text_color=WHITE)
        # self.op_button_12.grid(row=2, column=2, sticky=self.sticky, padx=3, pady=3)

        # Number Variables
        self.num1 = None
        self.num2 = None
        self.operation = None

    @staticmethod
    def _transform_dot2comma(obj):
        assert type(obj) != str, 'Parameter must be a string!'
        return str(obj).replace('.', ',')

    @staticmethod
    def _transform_comma2dot(shown_number):
        return shown_number.replace(',', '.')

    def _verify_comma(self, shown_number):
        if shown_number == '':
            display_number = shown_number
        else:
            if ',' in shown_number:
                display_number = float(self._transform_comma2dot(shown_number))
            else:
                display_number = int(shown_number)
        return display_number

    def all_clear(self):
        self.display.delete(0, END)

    def change_sign(self):
        display_number = self._verify_comma(self.display.get())
        display_number *= -1
        display_number = self._transform_dot2comma(display_number)
        self.display.configure(placeholder_text=display_number)

    def percentage(self):
        display_number = self._verify_comma()
        display_number /= 100
        display_number = self._transform_dot2comma(display_number)
        self.display.configure(placeholder_text=display_number)

    def comma(self):
        if ',' in self.display.get():
            pass
        else:
            new_n = self.display.get()
            self.display.delete(0, END)
            self.display.insert(0, new_n + ',')

    def set_number(self, n):
        assert type(n) == str, 'Argument must be a string'
        if self.display.get() == 0 or self.display.get() == '':
            new_n = n
        else:
            new_n = self.display.get() + n
        self.display.delete(0, END)
        self.display.insert(0, new_n)

    def operate(self, op):
        self.num1 = self.display.get()
        self.num1 = self._verify_comma(self.num1)
        self.operation = op
        self.display.delete(0, END)

    def evaluate(self):
        if self.operation not in ['+', '-', 'X', '÷']:
            self.display.delete(0, END)
            if self.operation == '+/-':
                self.display.insert(0, self._transform_dot2comma(-self.num1))
            elif self.operation == '%':
                self.display.insert(0, self._transform_dot2comma(self.num1 / 100))
        else:
            self.num2 = self._verify_comma(self.display.get())
            self.display.delete(0, END)
            if self.operation == '+':
                self.display.insert(0, self._transform_dot2comma(sum((self.num1, self.num2))))
            elif self.operation == '-':
                self.display.insert(0, self._transform_dot2comma(sum((self.num1, -self.num2))))
            elif self.operation == 'X':
                self.display.insert(0, self._transform_dot2comma(self.num1 * self.num2))
            elif self.operation == '÷':
                self.display.insert(0, self._transform_dot2comma(self.num1 / self.num2))
        self.num1, self.num2 = 0, 0

    def change_buttons(self):
        pass


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
