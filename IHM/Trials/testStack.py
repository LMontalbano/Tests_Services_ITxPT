import tkinter as tk
from time import sleep

# A dummy `test` function
def test():
    # Delay in seconds
    delay = 2.0
    sleep(delay)
    print_to_gui('Files currently transferring')
    sleep(delay)
    print_to_gui('Currently merging all pdfs')
    sleep(delay)
    print_to_gui('PDFs have been merged')
    sleep(delay)
    print_to_gui('Finished!\nYou can click the "Run test"\n'
        'button to run the test again.')

# Display a string in `out_label`
def print_to_gui(text_string):
    out_label.config(text=text_string)
    # Force the GUI to update
    top.update()

# Build the GUI
top = tk.Tk()
top.wm_title("testest")
top.minsize(width=300, height=150)
top.maxsize(width=300, height=150)

b = tk.Button(top, text='Run test', command=test)
b.config(width=15, height=1)
b.pack()

# A Label to display output from the `test` function
out_label = tk.Label(text='Click button to start')
out_label.pack()

top.mainloop()