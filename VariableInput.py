import tkinter as tk
import tkinter.ttk
from tkinter import ttk
import MathFunctions

def Add2Nums():
    def calc():
        x = int(xInput.get())
        y = int(yInput.get())

        result = MathFunctions.Add2Nums(x,y)

        answer.config(text="Answer is: {}".format(result))
        
    newWindow = tk.Toplevel()
    newWindow.title("Add 2 nums")
    newWindow.geometry("500x500")

    buttonframe = tk.Frame(newWindow)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)

    xLabel = ttk.Label(buttonframe, text="Value 1:")
    xInput = ttk.Entry(buttonframe)

    yLabel = ttk.Label(buttonframe, text="Value 2:")
    yInput = ttk.Entry(buttonframe)

    xLabel.grid(row=0, column=0)
    xInput.grid(row=0, column=1)
    yLabel.grid(row=1, column=0)
    yInput.grid(row=1, column=1)

    buttonframe.pack()

    calc = ttk.Button(newWindow, text="Calculate", command=calc)
    calc.pack()

    answer = ttk.Label(newWindow, text=f"Answer is: ")
    answer.pack()

    quit = ttk.Button(newWindow, text="Back to Menu", command=newWindow.destroy)
    quit.pack()

def Sub2Nums():
    def calc():
        x = int(xInput.get())
        y = int(yInput.get())

        result = MathFunctions.Sub2Nums(x,y)

        answer.config(text="Answer is: {}".format(result))
        
    newWindow = tk.Toplevel()
    newWindow.title("Sub 2 nums")
    newWindow.geometry("500x500")

    buttonframe = tk.Frame(newWindow)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)

    xLabel = ttk.Label(buttonframe, text="Value 1:")
    xInput = ttk.Entry(buttonframe)

    yLabel = ttk.Label(buttonframe, text="Value 2:")
    yInput = ttk.Entry(buttonframe)

    xLabel.grid(row=0, column=0)
    xInput.grid(row=0, column=1)
    yLabel.grid(row=1, column=0)
    yInput.grid(row=1, column=1)

    buttonframe.pack()

    calc = ttk.Button(newWindow, text="Calculate", command=calc)
    calc.pack()

    answer = ttk.Label(newWindow, text=f"Answer is: ")
    answer.pack()

    quit = ttk.Button(newWindow, text="Back to Menu", command=newWindow.destroy)
    quit.pack()

def Mult2Nums():
    def calc():
        x = int(xInput.get())
        y = int(yInput.get())

        result = MathFunctions.Mult2Nums(x,y)

        answer.config(text="Answer is: {}".format(result))
        
    newWindow = tk.Toplevel()
    newWindow.title("Mult 2 nums")
    newWindow.geometry("500x500")

    buttonframe = tk.Frame(newWindow)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)

    xLabel = ttk.Label(buttonframe, text="Value 1:")
    xInput = ttk.Entry(buttonframe)

    yLabel = ttk.Label(buttonframe, text="Value 2:")
    yInput = ttk.Entry(buttonframe)

    xLabel.grid(row=0, column=0)
    xInput.grid(row=0, column=1)
    yLabel.grid(row=1, column=0)
    yInput.grid(row=1, column=1)

    buttonframe.pack()

    calc = ttk.Button(newWindow, text="Calculate", command=calc)
    calc.pack()

    answer = ttk.Label(newWindow, text=f"Answer is: ")
    answer.pack()

    quit = ttk.Button(newWindow, text="Back to Menu", command=newWindow.destroy)
    quit.pack()

def Div2Nums():
    def calc():
        x = int(xInput.get())
        y = int(yInput.get())

        result = MathFunctions.Div2Nums(x,y)

        answer.config(text="Answer is: {}".format(result))
        
    newWindow = tk.Toplevel()
    newWindow.title("Div 2 nums")
    newWindow.geometry("500x500")

    buttonframe = tk.Frame(newWindow)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)

    xLabel = ttk.Label(buttonframe, text="Value 1:")
    xInput = ttk.Entry(buttonframe)

    yLabel = ttk.Label(buttonframe, text="Value 2:")
    yInput = ttk.Entry(buttonframe)

    xLabel.grid(row=0, column=0)
    xInput.grid(row=0, column=1)
    yLabel.grid(row=1, column=0)
    yInput.grid(row=1, column=1)

    buttonframe.pack()

    calc = ttk.Button(newWindow, text="Calculate", command=calc)
    calc.pack()

    answer = ttk.Label(newWindow, text=f"Answer is: ")
    answer.pack()

    quit = ttk.Button(newWindow, text="Back to Menu", command=newWindow.destroy)
    quit.pack()

def KineticEnergy():
    def calc():
        m = int(xInput.get())
        v = int(yInput.get())

        result = MathFunctions.KineticEnergy(m,v)

        answer.config(text="KE = {}".format(result) + " J")
            
    newWindow = tk.Toplevel()
    newWindow.title("Calculate Kinetic Energy of an object (Joules)")
    newWindow.geometry("500x500")

    buttonframe = tk.Frame(newWindow)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)

    xLabel = ttk.Label(buttonframe, text="Mass (kg):")
    xInput = ttk.Entry(buttonframe)
    
    yLabel = ttk.Label(buttonframe, text="Velocity (m/s):")
    yInput = ttk.Entry(buttonframe)

    xLabel.grid(row=0, column=0)
    xInput.grid(row=0, column=1)
    yLabel.grid(row=1, column=0)
    yInput.grid(row=1, column=1)

    buttonframe.pack()

    calc = ttk.Button(newWindow, text="Calculate", command=calc)
    calc.pack()

    answer = ttk.Label(newWindow, text="KE = ")
    answer.pack()

    quit = ttk.Button(newWindow, text="Back to Menu", command=newWindow.destroy)
    quit.pack()