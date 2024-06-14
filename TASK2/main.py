from tkinter import Tk,Entry,Label,Button,IntVar,ttk,StringVar
from Arithmatic_operations import ArithmaticOperations

class GUI():
    def __init__(self,master) -> None:
        self.n1 = IntVar()
        self.n2 = IntVar()
        self.option = StringVar(value="Select Option")

        # Configure the main window
        master.geometry("300x300")
        master.resizable(False, False)

        # Styles
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10), padding=5)
        style.configure("TLabel", font=("Arial", 10), padding=5)
        style.configure("TEntry", font=("Arial", 10), padding=5)
        style.configure("TCombobox", font=("Arial", 10), padding=5)

        # Create and place the first number label and entry
        lbl1 = ttk.Label(master, text="Enter Number 1: ")
        lbl1.grid(column=0, row=1, padx=10, pady=5, sticky="w")
        e1 = ttk.Entry(master, textvariable=self.n1)
        e1.grid(column=1, row=1, padx=10, pady=5, sticky="e")

        # Create and place the second number label and entry
        lbl2 = ttk.Label(master, text="Enter Number 2: ")
        lbl2.grid(column=0, row=2, padx=10, pady=5, sticky="w")
        e2 = ttk.Entry(master, textvariable=self.n2)
        e2.grid(column=1, row=2, padx=10, pady=5, sticky="e")

        # Options for arithmetic operations
        values = ["Addition", "Subtraction", "Multiplication", "Division", "Remainder"]
        cb = ttk.Combobox(master, values=values, textvariable=self.option)
        cb.grid(column=0, row=3, columnspan=2, padx=10, pady=5)

        # Create and place the button
        btn = ttk.Button(master, text="Calculate", command=self.btnClick)
        btn.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

        # Create and place the result label
        self.lbl = ttk.Label(master, text="")
        self.lbl.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

    def btnClick(self):
        n1 = self.n1.get()
        n2 = self.n2.get()
        ao = ArithmaticOperations(n1,n2)
        ans = ""
        try:
            match self.option.get():
                case "Addition":
                    ans = f"Addition of {n1} + {n2} = {ao.add()}"
                
                case "Subtraction":
                    ans = f"Subtraction of {n1} - {n2} = {ao.sub()}"
                    
                case "Multiplication":
                    ans = f"Multiplication of {n1} * {n2} = {ao.mul()}"
                    
                case "Division":
                    ans = f"Division of {n1} / {n2} = {ao.div()}"
                
                case "Remainder":
                    ans = f"Remainder of {n1} / {n2} = {ao.mod()}"
                    
                case _:
                    ans = "Please select the option..."
        except Exception as e:
            ans = "Error: ",e
                
        self.lbl.config(text=ans)

root = Tk()
root.title("Basic Calculator")
GUI(root)
root.mainloop()
        