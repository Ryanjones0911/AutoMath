import tkinter as tk
import tkinter.ttk
from tkinter import ttk
import VariableInput

#create and name the main window & set window size to 500x500
window = tk.Tk(className="AutoMath")
label = tk.Label(window, text="Automatically calculate complex formulas (WIP)")
label.pack()
window.geometry("500x500")

buttonframe = tk.Frame(window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)
buttonframe.columnconfigure(4, weight=1)
buttonframe.columnconfigure(5, weight=1)


#create menu buttons that will spawn different windows for their corresponding functions
add = ttk.Button(buttonframe, text="Add 2 nums", command=VariableInput.Add2Nums)
sub = ttk.Button(buttonframe, text="Sub 2 nums",  command=VariableInput.Sub2Nums)
mult = ttk.Button(buttonframe, text="Mult 2 nums", command=VariableInput.Mult2Nums)
div = ttk.Button(buttonframe, text="Div 2 nums",  command=VariableInput.Div2Nums)
kE = ttk.Button(buttonframe, text="Kinetic Energy", command=VariableInput.KineticEnergy)
quit = ttk.Button(buttonframe, text="Quit", command=quit)



#render buttons to screen
add.grid(row=0, column=0)
sub.grid(row=0, column=1)
mult.grid(row=0, column=2)
div.grid(row=1, column=0)
kE.grid(row=1, column=1)
quit.grid(row=1, column=2)

buttonframe.pack()


#runs main window indefinitely until manually killed
window.mainloop()