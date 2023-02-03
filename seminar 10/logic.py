import calc, Convertor

def button_click(text):
    primer = Convertor.convert_expression(text)
    result = calc.Calc(primer)
    return 