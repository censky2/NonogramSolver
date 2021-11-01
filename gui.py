import tkinter
import solver


def gui():
    window = tkinter.Tk()
    window.title("Pixel Solver")

    height_var = tkinter.IntVar()
    width_var = tkinter.IntVar()

    def get_height_width():
        height = height_var.get()
        width = width_var.get()
        height_var.set(0)
        width_var.set(0)
        window.destroy()
        show_grid(height, width)

    lbl_height = tkinter.Label(master=window, text="Height:")
    ent_height = tkinter.Entry(master=window, textvariable=height_var)
    lbl_width = tkinter.Label(master=window, text="Width:")
    ent_width = tkinter.Entry(master=window, textvariable=width_var)
    btn_height_width = tkinter.Button(master=window, text="Done", command=get_height_width)

    lbl_height.grid(row=0, column=0)
    ent_height.grid(row=0, column=1)
    lbl_width.grid(row=1, column=0)
    ent_width.grid(row=1, column=1)
    btn_height_width.grid(row=2, column=1)

    window.mainloop()


def show_grid(height, width):
    window = tkinter.Tk()
    screen_height = window.winfo_screenheight()
    screen_width = window.winfo_screenwidth()
    window.title("Pixel Solver")
    window.geometry(str(screen_width) + 'x' + str(screen_height))

    grid = [[-1 for x in range(width + 1)] for y in range(height + 1)]

    for i in range(height + 1):
        for j in range(width + 1):
            if i != 0 and j != 0:
                border_color = tkinter.Frame(master=window, background='black')
                lbl_pixel = tkinter.Label(master=border_color, bg='white', bd=0, width=int(screen_width/width/20))
                grid[i][j] = lbl_pixel
                lbl_pixel.pack(padx=1, pady=1)
                border_color.grid(row=i, column=j)
            else:
                string_var = tkinter.StringVar()
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    entry_pixel = tkinter.Entry(master=window, width=int(screen_width/width/20), textvariable=string_var)
                else:
                    entry_pixel = tkinter.Entry(master=window, textvariable=string_var)
                grid[i][j] = string_var
                entry_pixel.grid(row=i, column=j)

    def start_solve():
        arr = [[[-1 for z in range(1)] for y in range(width + 1)] for x in range(height + 1)]

        # Retrieve top entries
        for x in range(width + 1):
            if x != 0:
                arr[0][x] = grid[0][x].get().split(" ")

        for x in range(width + 1):
            for y in range(len(arr[0][x]) - 1, -1, -1):
                if arr[0][x][y] == '':
                    arr[0][x].pop(y)
                else:
                    arr[0][x][y] = int(arr[0][x][y])

        # Retrieve left entries
        for x in range(height + 1):
            if x != 0:
                arr[x][0] = grid[x][0].get().split(" ")

        for x in range(height + 1):
            for y in range(len(arr[x][0]) - 1, -1, -1):
                if arr[x][0][y] == '':
                    arr[x][0].pop(y)
                else:
                    arr[x][0][y] = int(arr[x][0][y])

        solver.solve(arr)

        for x in range(width + 1):
            for y in range(height + 1):
                if x != 0 and y != 0:
                    if arr[x][y][0] == 1:
                        grid[x][y].config(bg="black")

    btn_solve = tkinter.Button(master=window, text="Solve", command=start_solve)
    btn_solve.grid(row=height + 2, column=int(width / 2))

    window.mainloop()


gui()
