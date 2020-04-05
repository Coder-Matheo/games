import re
hexa = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
decimalvalue = []

def hexaToDeci():
    while True:
        hexanum = input('Enter your Hexadecimal value  : ')
        allowed = re.findall('[a-fA-F0-9]', hexanum)
        for i in hexanum:
            if len(allowed) == len(hexanum):
                if (i.isdigit() == True):        # separate the number and letter from input
                    i = int(i)
                    decimalvalue.insert(0,hexa[i])
                elif (i.isalpha() == True):
                    i = i.upper()
                    decimalvalue.insert(0,hexa[i])
            else:
                print("Invalid input!")

        for j in range(0,len(decimalvalue)):
            Exponent  = 16 ** j
            decimalvalue[j] = decimalvalue[j] * Exponent
        print('Result Hexa to Decimal : ',sum(decimalvalue))
        print()
        decimalvalue.clear()



if __name__ == "__main__":
    hexaToDeci()
