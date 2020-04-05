decimalValue = []

def binTodec():
    while True:
        binaryNum = input("Enter a binary Number : ")
        for i in binaryNum:
            decimalValue.insert(0, int(i))

        for j in range(0, len(binaryNum)):
            exponent = 2 ** j
            decimalValue[j] = decimalValue[j] * exponent

        print(sum(decimalValue))
        decimalValue.clear()


if __name__ == "__main__":
    binTodec()
