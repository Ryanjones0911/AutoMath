def Add2Nums(x, y):
    return str(x + y)

def Sub2Nums(x, y):
    return str(x - y)

def Mult2Nums(x, y):
    return str(x * y)

def Div2Nums(x, y):
    result = x / y
    result = round(result, 2)
    return str(result)

def KineticEnergy(m, v):
    result = .5 * m * pow(v, 2)
    return str(result)