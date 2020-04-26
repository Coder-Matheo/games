import numpy as np
import random

class SudukoGame:
    suduko_table = np.zeros((9, 9))

    #Put Random Number in the Table
    def number_table(self):
        for index in range(6):
            global putNum
            num1 = random.randrange(1, 9)
            num2 = random.randrange(1, 9)
            rNum = np.arange(1,9)
            putNum = self.suduko_table[num1][num2] = rNum[index]

    def userInput(self):
        #execute the function for random number inside the table
        self.number_table()
        for _ in range(100):
            print("Choose a number from 1-9 for rows and columns")
            col_pos = int(input('Enter your position (row)Number: '))
            col_pos = col_pos - 1                                           #index will start from 1:1 instead of 0:0
            row_pos = int(input('Enter your position (column) Number: '))
            row_pos = row_pos - 1
            val_num = float(input('Enter your Value Number: '))

            if val_num <= 9 and col_pos <= 9 and row_pos <= 9:
                val_num1 = val_num
                #checking the rows and columns, if the Value Number(inputted by the user) exist.
                if val_num1 not in self.suduko_table[:, row_pos] and val_num1 not in self.suduko_table[col_pos, :]:
                    if self.suduko_table[col_pos][row_pos] == 0.0:
                        self.suduko_table[col_pos][row_pos] = val_num1
                else:
                    print('Number Exist, Try another number')
            else:
                print('Invalid Input, Enter a number again')
            print(self.suduko_table)


if __name__ == "__main__":
    sud = SudukoGame()
    sud.userInput()