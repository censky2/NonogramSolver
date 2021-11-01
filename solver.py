# Global Variables
empty_row = 1
empty_col = 0


# Prints the grid
def print_grid(array):
    for i in range(1, len(array)):
        for j in range(1, len(array[0])):
            print(array[i][j], end='')
        print()


# Checks if all ranges are valid
def check_valid_ranges(x_size, y_size, array):
    # Check column ranges
    for i in range(1, 1 + y_size):
        counter = 0
        # Loop through each element in range
        for j in range(len(array[0][i])):
            counter += array[0][i][j]
            # Adds one for at least one spacer between color
            if j < len(array[0][i]) - 1:
                counter += 1
        # Minimum possible pixels can't be greater than number of columns
        if counter > len(array) - 1:
            return False

    # Check row ranges
    for i in range(1, 1 + x_size):
        counter = 0
        # Loop through each element in range
        for j in range(len(array[i][0])):
            counter += array[i][0][j]
            # Adds one for at least one spacer between color
            if j < len(array[i][0]) - 1:
                counter += 1
        # Minimum possible pixels can't be greater than number of rows
        if counter > len(array[0]) - 1:
            return False

    return True


# Checks if (row, col) pixel can be colored
# Note: Assumes previous (all pixels to the left and above the current pixel) pixels are valid!
def safe_pixel(array, row, col):
    # If empty row/column
    if safe_pixel_row(array, row, col):
        return safe_pixel_col(array, row, col)
    else:
        return False


# Checks if (row, col) pixel can be colored in row
def safe_pixel_row(array, row, col):
    row_range_index = 0  # Index of the current element in ranges array
    row_range_copy = array[row][0].copy()  # Copy of ranges array
    len_row_range_array = len(row_range_copy)  # Length of ranges array
    need_spacer = False  # Weather a space is needed between colors
    counter = 0  # Number of pixels that are "occupied"

    # Loops through all columns in row
    for i in range(1, len(array[row])):
        counter += 1
        if array[row][i][0] == 1 or i == col:  # Current pixel is colored
            if not need_spacer:
                row_range_copy[row_range_index] -= 1  # Decrements row range
                if row_range_copy[row_range_index] == 0:  # Moves onto new row range index
                    row_range_index += 1
                    need_spacer = True
                    if row_range_index == len_row_range_array:  # Used up all of the ranges
                        return True if i == col else False
            else:
                return False
            if i == col:
                break
        elif array[row][i][0] == 0:  # Resets spacer boolean if needed
            need_spacer = False

    if need_spacer:  # Accounts for current spacer
        counter += 1

    # Loop through each element in range
    for i in range(row_range_index, len(row_range_copy)):
        counter += row_range_copy[i]
        # Adds one for at least one spacer between color
        if i < len(row_range_copy) - 1:
            counter += 1
    # Minimum possible pixels can't be greater than number of rows
    if counter > len(array[0]) - 1:
        return False

    return True


# Checks if (row, col) pixel can be colored in col
def safe_pixel_col(array, row, col):
    col_range_index = 0  # Index of the current element in ranges array
    col_range_copy = array[0][col].copy()  # Copy of ranges array
    len_col_range_array = len(col_range_copy)  # Length of ranges array
    need_spacer = False  # Weather a space is needed between colors
    counter = 0  # Number of pixels that are "occupied"

    # Loops through all rows in a column
    for i in range(1, len(array)):
        counter += 1
        if array[i][col][0] == 1 or i == row:  # Current pixel is colored
            if not need_spacer:
                col_range_copy[col_range_index] -= 1  # Column row range
                if col_range_copy[col_range_index] == 0:  # Moves onto new column range index
                    col_range_index += 1
                    need_spacer = True
                    if col_range_index == len_col_range_array:  # Used up all of the ranges
                        return True if i == row else False
            else:
                return False
            if i == row:
                break
        elif array[i][col][0] == 0:  # Resets spacer boolean if needed
            need_spacer = False

    if need_spacer:  # Accounts for current spacer
        counter += 1

    # Loop through each element in range
    for i in range(col_range_index, len(col_range_copy)):
        counter += col_range_copy[i]
        # Adds one for at least one spacer between color
        if i < len(col_range_copy) - 1:
            counter += 1
    # Minimum possible pixels can't be greater than number of columns
    if counter > len(array) - 1:
        return False

    return True


# Checks if (row, col) pixel can be empty
# Note: Assumes previous (all pixels to the left and above the current pixel) pixels are valid!
def empty_pixel(array, row, col):
    # If empty row/column
    if empty_pixel_row(array, row, col):
        return empty_pixel_col(array, row, col)
    else:
        return False


# Checks if (row, col) pixel can be empty in row
def empty_pixel_row(array, row, col):
    row_range_index = 0  # Index of the current element in ranges array
    row_range_copy = array[row][0].copy()  # Copy of ranges array
    len_row_range_array = len(row_range_copy)  # Length of ranges array
    need_color = False  # Weather a pixel must be colored
    need_spacer = False  # Weather a space is needed between colors

    # Loops through all columns in row
    for i in range(1, len(array[row])):
        if array[row][i][0] == 1 or i > col:  # Current pixel is colored
            if not need_spacer:
                row_range_copy[row_range_index] -= 1  # Decrements row range
                if row_range_copy[row_range_index] == 0:  # Moves onto new row range index
                    need_color = False
                    need_spacer = True
                    row_range_index += 1
                    if row_range_index == len_row_range_array:  # Used up all of the ranges
                        return True
                else:
                    need_color = True
            else:
                need_spacer = False
        elif array[row][i][0] == 0 or i == col:  # Current pixel is empty
            need_spacer = False
            if need_color:
                return False

    return False


# Checks if (row, col) pixel can be empty in col
def empty_pixel_col(array, row, col):
    col_range_index = 0  # Index of the current element in ranges array
    col_range_copy = array[0][col].copy()  # Copy of ranges array
    len_col_range_array = len(col_range_copy)  # Length of ranges array
    need_color = False  # Weather a pixel needs to be colored
    need_spacer = False  # Weather a space is needed between colors

    # Loops through all columns in row
    for i in range(1, len(array)):
        if array[i][col][0] == 1 or i > row:  # Current pixel is colored
            if not need_spacer:
                col_range_copy[col_range_index] -= 1  # Decrements row range
                if col_range_copy[col_range_index] == 0:  # Moves onto new row range index
                    need_color = False
                    need_spacer = True
                    col_range_index += 1
                    if col_range_index == len_col_range_array:  # Used up all of the ranges
                        return True
                else:
                    need_color = True
            else:
                need_spacer = False
        elif array[i][col][0] == 0 or i == row:  # Current pixel is empty
            need_spacer = False
            if need_color:
                return False

    return False


def solve(array):
    # Uses global variables
    global empty_row, empty_col

    # Moves onto the next empty pixel
    empty_col += 1
    if empty_col == len(array[0]):
        empty_col = 1
        empty_row += 1
    # Indicates last pixel is complete
    if empty_row == len(array):
        return True

    for i in range(2):
        if i == 0:
            if safe_pixel(array, empty_row, empty_col):
                array[empty_row][empty_col][0] = 1
                if solve(array):
                    return True
                array[empty_row][empty_col][0] = -1
        else:
            if empty_pixel(array, empty_row, empty_col):
                array[empty_row][empty_col][0] = 0
                if solve(array):
                    return True
                array[empty_row][empty_col][0] = -1

    # Backtracks going back to the previous pixel
    empty_col -= 1
    if empty_col == 0:
        empty_col = len(array[0]) - 1
        empty_row -= 1

    return False
