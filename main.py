import tkinter as tk

symbols = ['7', '8', '9', '/', '\u21BA', 'C', '4', '5', '6',
           '*', '(', ')', '1', '2', '3', '-', 'x\u00B2', '\u221A',
           '0', ',', '%', '+']

Color = '#f2f4f7'

def initializationWindow():
    root = tk.Tk()
    root.configure(bg=Color)
    root.geometry('460x375')
    root.title('Kalkulator')

    return root


def initializationScreen(root):
    screen = [tk.Label(root, bg='#C0CBCB', width=62, anchor='w', borderwidth=2) for i in range(3)]

    for i in range(len(screen)):
        screen[i].grid(row=i, columnspan=6, ipady=15, ipadx=1)

    return screen


def initializationBoxForData(root, screen):

    box_for_data = tk.Entry(root, borderwidth=0, highlightcolor='white', highlightbackground='white')
    box_for_data.grid(row=len(screen), columnspan=6, ipadx=160, ipady=10)

    info = tk.Label(root, bg='white', width=62, anchor='w', borderwidth=2)
    info.grid(row=len(screen)+1, columnspan=6, ipady=15, ipadx=1)

    return box_for_data, info


def buttonClick(box_for_data, symbol):
    def f():
        if symbol == '\u21BA':
            text = box_for_data.get()[:-1]
            box_for_data.delete(0, tk.END)
            box_for_data.insert(0, text)
        elif symbol == 'C':
            box_for_data.delete()
        elif symbol == 'x\u00B2':
            box_for_data.insert(tk.END, '^2')
        else:
            box_for_data.insert(tk.END, symbol)

    return f


def calculate(box_for_data, screen, info):
    def if_correct_last_character(text):
        i = 1

        while text[-1] == ')':
            i += 1

        return text[-i].isdigit()

    def if_multiple_operators(text):

        for i in range(len(text)):
            if not text[i].isdigit() and not text[i + 1].isdigit():
                return True

        return False

    def changeSignOfPower(text):

        for i in range(len(text)):
            if text[i] == '^':
                text = text[:i] + '**' + text[i+1:]
        return text

    def f():
        text = box_for_data.get()

        if not if_correct_last_character(text) or if_multiple_operators(text):
            info['text'] = 'Błędne wyrażenie'

        else:
            for i in range(1, len(screen)):
                if screen[i]['text']:
                    screen[i - 1]['text'] = screen[i]['text']

            if '^' in text:
                expression = changeSignOfPower(text)
                screen[-1]['text'] = text + ' = ' + str(eval(expression))
            else:
                screen[-1]['text'] = text + ' = ' + str(eval(text))

    return f


def initializationButtons(root, screen, info):
    buttons = [tk.Button(root, text=symbol, bg='light grey', borderwidth=0.5) for symbol in symbols]

    margin = 30
    j = len(screen) + 2
    for i in range(len(buttons)):
        if i % 6 == 0:
            j += 1
        buttons[i].grid(row=j, column=i % 6, ipady=5, ipadx=margin)
        buttons[i].configure(command=buttonClick(box_for_data, buttons[i]['text']))

    equal_sign = tk.Button(root, text='=', bg='#00BFFF', borderwidth=0, command=calculate(box_for_data, screen, info))

    equal_sign.grid(row=len(screen) + 6, column=4, columnspan=2, ipady=5, ipadx=70)

    return buttons


if __name__ == '__main__':

    root = initializationWindow()

    screen = initializationScreen(root)

    box_for_data, info = initializationBoxForData(root, screen)

    buttons = initializationButtons(root, screen, info)

    root.mainloop()
