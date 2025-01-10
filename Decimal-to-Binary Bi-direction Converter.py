from graphics import *
from button import Button

def main ():
    win, inputText, outputText, Convert, exit2, Reset = gui()
    p = win.getMouse()
    while not exit2.clicked(p):
        if inputText.getText() != "":
            Binary = get_actual_list(Convert, inputText, p)
            printSummary(Binary,outputText)
        else:
            number = getNubmer(outputText, Convert, p)
            convert_to_number(inputText,number)
        reset(Reset, p, inputText, outputText)
        p = win.getMouse()
    win.close()

def gui():
    win = GraphWin ("Decimal-to-Binary Bi-Converter", 815, 300)
    win.setCoords(0, 0, 3, 4)

    Text (Point(0.5,3), "   Decimal Number: ").draw(win)
    Text (Point(0.5,1), "Binary Number: ").draw(win)
    
    inputText = Entry(Point(1.8, 3), 62)
    inputText.setText("")
    inputText.draw(win)
    outputText = Entry(Point(1.8, 1), 62)
    outputText.setText("")
    outputText.draw(win)

    Convert = Button(win, Point(0.5, 2.3), 0.5, 0.5, "Convert")
    Convert.activate()

    exit2 = Button(win, Point(2.5, 2.3), 0.5, 0.5, "Exit")
    exit2.activate()

    Reset = Button(win, Point(1.5, 2.3), 0.5, 0.5, "Reset")
    Reset.activate()
    
    return win, inputText, outputText,Convert, exit2, Reset

def get0list(inputText):
    Decimal = eval(inputText.getText())
    pos = 1
    while Decimal > 0:
        Decimal = Decimal // 2
        if Decimal > 0:
            pos = pos + 1
    binary = [0] * pos
    
    return binary, pos

def get_actual_list(Convert, inputText, p):
    if Convert.clicked(p):
        Decimal = eval(inputText.getText())
        Binary, pos  = get0list(inputText)
        power = pos - 1
        n = 0
        while power >= 0:
            if Decimal >= 2**(power):
                Binary[n] = 1
            else:
                Binary[n] = 0
            Decimal = Decimal % 2**(power)
            power = power - 1
            n = n + 1 
        return Binary

def printSummary(Binary,outputText):
    if Binary != None:
        Binary_string = ""
        for i in Binary:
            Binary_string = Binary_string + str(i)

        outputText.setText(Binary_string)

def getNubmer(outputText, Convert, p):
    if Convert.clicked(p):
        binary = outputText.getText()
        number = 0
        b = len(binary)
        for i in range (b):
            b = b - 1
            number = number + (2**b)*(int(binary[i]))
        return number

def convert_to_number(inputText,number):
    if number != None:
        inputText.setText(str(number))

def reset(Reset, p, inputText, outputText):
    if Reset.clicked(p):
        inputText.setText("")
        outputText.setText("")

if __name__ == '__main__': main()

