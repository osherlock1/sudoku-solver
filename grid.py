#Class to make the grid

class Grid:
    def __init__(self):
        #Helper function to initiate the grid
        self.grid = self._create_grid()



    def solve(self, n):

        n = n + 1
        print(n)
        if n == 900:
            return False
    

        #Base Case
        row_idx, col_idx = self.find_empty_space()

        if row_idx == 23:
            print("Sudoku Solved")
            self.display_grid()
            return True
        
        #Recursive Case

        #Get info
        row = self.get_row(row_idx)
        col = self.get_column(col_idx)
        subbox_idx = self.get_sub_block_idx(row_idx, col_idx)
        subbox = self.get_sub_block(subbox_idx)
        self.display_grid()

        #Try all numbers in empty space
        for i in range(9):
            check = self.run_checks(row, col, subbox, i + 1)
            print(f"Row idx: {row_idx}, Col idx: {col_idx}, Subbox idx: {subbox_idx}, Test number: {i + 1} \n")
            self.display_grid()
            print("___________________________________")       

            if check:
                self.grid[row_idx][col_idx] = i + 1
                if self.solve(n) == True:
                    return True
                else:
                    print("Dead end")
                    self.grid[row_idx][col_idx] = 0


        
        

    def run_checks(self, row_index, column_index, subbox_index, number):
        row_check = self.check_row(number, row_index)

        column_check = self.check_column(number, column_index)

        subbox_check = self.check_subbox(number, subbox_index)

        if row_check and column_check and subbox_check:
            return True
        else:
            return False

    def check_row(self, number, row):

        for num in row:
            if num == number:
                return False
        return True
    
    def check_column(self, number, column):
        for num in column:
            if num == number:
                return False
        return True
    
    def check_subbox(self, number, subbox):
        #print(f"Subbox: {type(subbox)}")
        for num in subbox:
            if num == number:
                return False
        return True


    def _create_grid(self):

        #Helper function to intantiate empty sudoku grid
        full_grid = []

        for i in range(9):
            row = []
            for j in range(9):
                row.append(0)
            full_grid.append(row)
        
        return full_grid

    def display_grid(self):
        #Display grid with lines for easy viewing
        for i, row in enumerate(self.grid):

            if i % 3 == 0 and i != 0:
                print("-------------------")


            for j, num in enumerate(row):

                if j % 3 == 0 and j != 0:
                    print("|", end = "")
                if j == 8:
                    print(num)
                else:
                    print(str(num) + " ", end = "")

    def get_row(self, row_idx):
        #Return Row(list) based on input row index
        if row_idx <= 8 and row_idx >= 0:
            target_row = self.grid[row_idx]
            return target_row
        else:
            return print("Row index not in range")
        
    def get_column(self, column_idx):

        if column_idx <= 8 and column_idx >= 0:
            column = []
            #Loop through each row in the grid and return in index in the row from the column_idx
            for row in self.grid:
                column.append(row[column_idx])
            return column
        else:
            print("Column Index not in range")

    def get_sub_block(self, sub_block_index):

        if sub_block_index >= 0 and sub_block_index < 9:
            sub_block = []
            
            row_index = (sub_block_index // 3) * 3
            column_index = (sub_block_index % 3) * 3


            for i in range(3):
                for j in range(3):

                    cell_value = self.grid[row_index + i][column_index + j]
                    sub_block.append(cell_value)
                    
            return sub_block
        else:
            print("Sub Block Index out of range")

    def get_sub_block_idx(self, row_idx, column_idx):

        box_row = row_idx // 3
        box_column = column_idx // 3
        sub_block_idx = (box_row * 3) + box_column
        return sub_block_idx 

    def find_empty_space(self):
        for i, row in enumerate(self.grid):
            for j, num in enumerate(row):
                if num == 0:
                    row_idx = i
                    col_idx = j
                    return row_idx, col_idx
        return 23, 23




            




