import numpy as np
import pandas as pd
import random as rn
import re


outer_row = ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C']
inner_row = [1, 2, 3, 1, 2, 3, 1, 2, 3]
index_number = list(zip(outer_row, inner_row))
index_number = pd.MultiIndex.from_tuples(index_number)

outer_col = ['D', 'D', 'D', 'E', 'E', 'E', 'F', 'F', 'F']
inner_col = [1, 2, 3, 1, 2, 3, 1, 2, 3]
columns_number = list(zip(outer_col, inner_col))
columns_number = pd.MultiIndex.from_tuples(columns_number)


class Suduko:
    df = pd.DataFrame(np.zeros((9, 9)), index=index_number, columns=columns_number)
    def random_number(self):
        for index in range(9):
            num1 = rn.randrange(1, 9)       #col
            num2 = rn.randrange(1, 9)       #rows
            rNum = np.arange(1, 10)         #random Number
            self.df.iloc[num1].iloc[num2] = rNum[index]


    def process(self):
        while True:
            row_pos = input('Enter your row (letter A-C) position: ').upper()
            row_posB = re.search('[A-C]', row_pos)      #B-boolean
            col_pos = input('Enter your col (letter D-F) position: ').upper()
            col_posB = re.search('[D-F]',col_pos)
            el_row_pos = input('Enter your row (Number 1-3) position: ')
            el_row_posB = re.search('[1-3]',el_row_pos)
            el_col_pos = input('Enter your col (Number 1-3) position: ')
            el_col_posB = re.search('[1-3]',el_col_pos)
            ValueNumber = input('Enter your Number 1-9: ')


            if row_posB and col_posB and el_col_posB and el_row_posB and float(ValueNumber) <= 9:
                el_row_pos = int(el_row_pos)
                el_col_pos = int(el_col_pos)
                ValueNumber = float(ValueNumber)
                content_check = list()
                for i in range(1,4):
                    for j in range(1,4):
                        checking_value_box = (self.df.loc[row_pos][col_pos][i][j] != ValueNumber)
                        content_check.append(checking_value_box)

                if all(content_check) and self.df.loc[row_pos, col_pos][el_col_pos][el_row_pos] == 0.0:

                    content_columns = list()
                    content_rows = list()
                    for ind in range(0, 9):
                        checking_value_col = self.df[col_pos][el_col_pos][ind] != ValueNumber
                        checking_value_row = self.df.loc[row_pos].loc[el_row_pos][ind] != ValueNumber
                        content_columns.append(checking_value_col)
                        content_rows.append(checking_value_row)

                    if all(content_columns) and all(content_rows):
                        self.df.loc[row_pos, col_pos][el_col_pos][el_row_pos] = ValueNumber
                    else:
                        print('Number already exist in row/column')
                else:
                    print('Number already exist in', row_pos,':',col_pos, 'position')
            else:
                print('Try again')
            print(self.df)


if __name__ == '__main__':
    s = Suduko()
    s.random_number()
    s.process()

