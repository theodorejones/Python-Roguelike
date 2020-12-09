import tkinter as tk

global r
global c
global grid
grid = []
for x in range(8):
    grid.append([])
    for y in range(8):
        grid[x].append(0)
r = 4
c = 4
grid[r][c] = 1

def fahrenheit_to_celsius():
    if(entry.get() == "N"):
        if(r > 0):
            grid[r][c] = 0
            r = r + 1
            grid[r][c] = 1
    
    lbl_result["text"] = grid

# Set-up the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
entry = tk.Entry(master=frm_entry, width=10)

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
entry.grid(row=0, column=0, sticky="e")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()
