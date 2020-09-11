# Escribir una función que convierta un número decimal en
# binario y otra que convierta un número binario en decimal.
def decimalToBinary(d):
    binaryList = []
    rest = d
    while (1):
        print(rest)
        if rest == 1:
            binaryList.append(1)
            break
        elif rest % 2 != 0:
            binaryList.append(1)
        else:
            binaryList.append(0)
        rest = round(rest / 2)
    return binaryList


print(decimalToBinary(53))
