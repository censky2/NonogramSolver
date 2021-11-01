import solver
import time


def test_safe_pixel_1():
    rows = 5
    cols = 5
    grid = [[[-1 for z in range(1)] for y in range(cols + 1)] for x in range(rows + 1)]
    expected = [(1, 1), (1, 3)]
    result = []

    grid[0] = [[0], [1], [0], [1], [0], [0]]
    grid[1][0] = [1, 1]
    grid[2][0] = [0]
    grid[3][0] = [0]
    grid[4][0] = [0]
    grid[5][0] = [0]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if solver.safe_pixel(grid, i, j):
                result.append((i, j))

    print(result)

    if result == expected:
        return True
    else:
        return False


def test_safe_pixel_2():
    rows = 5
    cols = 5
    grid = [[[-1 for z in range(1)] for y in range(cols + 1)] for x in range(rows + 1)]
    expected = [(1, 1), (1, 3), (2, 1), (3, 1), (3, 3), (5, 4)]
    result = []

    grid[0] = [[0], [2], [0], [3], [1], [5]]
    grid[1][0] = [1, 1]
    grid[2][0] = [1, 1, 1]
    grid[3][0] = [3]
    grid[4][0] = [0]
    grid[5][0] = [1]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if solver.safe_pixel(grid, i, j):
                result.append((i, j))

    if result == expected:
        return True
    else:
        return False


def test_empty_pixel_1():
    rows = 1
    cols = 5
    grid = [[[-1 for z in range(1)] for y in range(cols + 1)] for x in range(rows + 1)]
    expected = [(1, 4), (1, 5)]
    result = []

    grid[0] = [[0], [1], [1], [1], [1], [1]]
    grid[1]= [[3], [1], [-1], [-1], [-1], [-1]]


    for i in range(1, rows + 1):
        for j in range(2, cols + 1):
            if solver.empty_pixel(grid, i, j):
                result.append((i, j))

    print(result)
    if result == expected:
        return True
    else:
        return False


def test_empty_pixel_2():
    rows = 5
    cols = 5
    grid = [[[-1 for z in range(1)] for y in range(cols + 1)] for x in range(rows + 1)]
    expected = [(1, 1), (1, 2), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (5, 2)]
    result = []

    grid[0] = [[0], [2], [0], [3], [1], [5]]
    grid[1][0] = [1, 1]
    grid[2][0] = [1, 1, 1]
    grid[3][0] = [3]
    grid[4][0] = [0]
    grid[5][0] = [1]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if solver.empty_pixel(grid, i, j):
                result.append((i, j))

    if result == expected:
        return True
    else:
        return False


def test_solve_1():
    rows = 5
    cols = 5
    grid = [[[-1 for z in range(1)] for y in range(cols + 1)] for x in range(rows + 1)]
    expected = [[[0], [1], [0], [1], [0], [0]],
                [[1, 1], [1], [0], [1], [0], [0]],
                [[0], [0], [0], [0], [0], [0]],
                [[0], [0], [0], [0], [0], [0]],
                [[0], [0], [0], [0], [0], [0]],
                [[0], [0], [0], [0], [0], [0]]]

    grid[0] = [[0], [1], [0], [1], [0], [0]]
    grid[1][0] = [1, 1]
    grid[2][0] = [0]
    grid[3][0] = [0]
    grid[4][0] = [0]
    grid[5][0] = [0]

    solver.solve(grid)

    if grid == expected:
        return True
    else:
        return False


def test_solve_2():
    rows = 7
    cols = 10
    grid = [[[-1 for z in range(1)] for y in range(cols + 1)] for x in range(rows + 1)]
    expected = [[[0], [1], [5], [6], [6], [6], [6], [5], [4], [4], [2]],
                [[2], [0], [0], [0], [1], [1], [0], [0], [0], [0], [0]],
                [[4, 2], [0], [0], [1], [1], [1], [1], [0], [1], [1], [0]],
                [[9], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
                [[9], [0], [1], [1], [1], [1], [1], [1], [1], [1], [1]],
                [[9], [1], [1], [1], [1], [1], [1], [1], [1], [1], [0]],
                [[6], [0], [1], [1], [1], [1], [1], [1], [0], [0], [0]],
                [[2, 2], [0], [1], [1], [0], [1], [1], [0], [0], [0], [0]]]

    grid[0] = [[0], [1], [5], [6], [6], [6], [6], [5], [4], [4], [2]]
    grid[1][0] = [2]
    grid[2][0] = [4, 2]
    grid[3][0] = [9]
    grid[4][0] = [9]
    grid[5][0] = [9]
    grid[6][0] = [6]
    grid[7][0] = [2, 2]

    return solver.solve(grid)


def test_solve_3():
    rows = 5
    cols = 5
    grid = [[[-1 for z in range(1)] for y in range(cols + 1)] for x in range(rows + 1)]
    expected = [[[0], [3, 1], [2], [2, 1], [1, 1], [2]],
                [[4], [1], [1], [1], [1], [0]],
                [[3], [1], [1], [1], [0], [0]],
                [[1], [1], [0], [0], [0], [0]],
                [[1], [0], [0], [0], [0], [1]],
                [[1, 3], [1], [0], [1], [1], [1]]]

    grid[0] = [[0], [3, 1], [2], [2, 1], [1, 1], [2]]
    grid[1][0] = [4]
    grid[2][0] = [3]
    grid[3][0] = [1]
    grid[4][0] = [1]
    grid[5][0] = [1, 3]

    solver.solve(grid)
    solver.print_grid(grid)

    if grid == expected:
        return True
    else:
        return False


def test_solve_4():
    rows = 25
    cols = 25
    grid = [[[-1 for z in range(1)] for y in range(cols + 1)] for x in range(rows + 1)]

    grid[0] = [[0], [1, 1, 1, 6, 5], [5, 1, 1, 5], [2, 3, 1, 3], [2, 3, 2, 3], [1, 8],
               [1, 1, 3, 4, 3], [4, 3, 3, 1], [3, 7, 2], [10, 1, 2, 2], [2, 6, 1],
               [2, 6, 3, 2], [3, 5, 2, 2], [7, 1, 3, 3, 6], [1, 3, 13], [3, 1, 11, 1],
               [3, 6], [5, 1, 1, 1], [6, 7], [5, 1, 5], [2, 3, 5],
               [1, 1, 2, 9], [1, 8], [3, 5, 2, 7, 1], [9, 2, 4, 1], [12, 2, 1]]
    grid[1][0] = [2, 6, 3, 3]
    grid[2][0] = [1, 4, 6, 3]
    grid[3][0] = [3, 2, 7, 3]
    grid[4][0] = [3, 1, 2, 4, 2]
    grid[5][0] = [1, 7, 3, 3]
    grid[6][0] = [2, 6, 1, 3]
    grid[7][0] = [2, 5, 1, 5]
    grid[8][0] = [4, 3]
    grid[9][0] = [1, 8, 3]
    grid[10][0] = [5, 1, 1]
    grid[11][0] = [8, 1, 1, 3]
    grid[12][0] = [4, 2, 2, 3]
    grid[13][0] = [3, 2, 4]
    grid[14][0] = [2, 1, 3, 3]
    grid[15][0] = [2, 2, 3, 3]
    grid[16][0] = [1, 4, 3]
    grid[17][0] = [2, 1, 1, 5, 3]
    grid[18][0] = [1, 3, 1, 1, 4, 4]
    grid[19][0] = [7, 1, 5, 4]
    grid[20][0] = [4, 3, 1, 6]
    grid[21][0] = [2, 2, 3, 8]
    grid[22][0] = [2, 1, 4, 6]
    grid[23][0] = [6, 4, 3, 1]
    grid[24][0] = [6, 2, 1, 2, 4]
    grid[25][0] = [11, 3, 2, 3]

    if solver.solve(grid):
        solver.print_grid(grid)
        return True
    return False


def test_solve_5():
    rows = 10
    cols = 10
    grid = [[[-1 for z in range(1)] for y in range(cols + 1)] for x in range(rows + 1)]

    grid[0] = [[0], [4], [1, 8], [5], [4], [3],
               [2, 4], [1, 1, 1, 2], [3], [5], [6]]
    grid[1][0] = [4, 1]
    grid[2][0] = [4]
    grid[3][0] = [6]
    grid[4][0] = [3]
    grid[5][0] = [2, 1]
    grid[6][0] = [1, 2]
    grid[7][0] = [2, 5]
    grid[8][0] = [2, 1, 3]
    grid[9][0] = [2, 5]
    grid[10][0] = [2, 2, 2]

    return solver.solve(grid)


if __name__ == "__main__":
    start_time = time.time()
    # print("Success") if test_safe_pixel_1() else print("Failure")
    # print("Success") if test_safe_pixel_2() else print("Failure")
    # print("Success") if test_empty_pixel_1() else print("Failure")
    # print("Success") if test_empty_pixel_2() else print("Failure")
    # print("Success") if test_solve_1() else print("Failure")
    # print("Success") if test_solve_2() else print("Failure")
    # print("Success") if test_solve_3() else print("Failure")
    print("Success") if test_solve_4() else print("Failure")
    # print("Success") if test_solve_5() else print("Failure")

    print("%s seconds" % (time.time() - start_time))
