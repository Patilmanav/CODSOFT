# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.

class ArithmaticOperations:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        return self.num1 / self.num2
    
    def mod(self):
        return self.num1 % self.num2
    
if __name__ == '__main__':
    
    while True:
        n1 = int(input("\n\nEnter First Number: "))
        n2 = int(input("Enter Second Number: "))
        ao = ArithmaticOperations(n1,n2)
        print("1. Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulas")
        
        while True:
            
            n = int(input("Enter your Choice: or press 0 to quit!! : "))
            match n:
                case 1:
                    ans = f"Addition of {n1} + {n2} = {ao.add()}"
                
                case 2:
                    ans = f"Subtraction of {n1} - {n2} = {ao.sub()}"
                    
                case 3:
                    ans = f"Multiplication of {n1} * {n2} = {ao.mul()}"
                    
                case 4:
                    ans = f"Division of {n1} / {n2} = {ao.div()}"
                    
                case 5:
                    ans = f"Remainder of {n1} / {n2} = {ao.mod()}"
                    
                case 0:
                    print("Exiting...")
                    break
                
                case _:
                    print("Wrong input... Selecte again!!")
                    ans = "Answer is: null"
        
            print(f"\n\n{ans}\n\n")
        ch = input("Enter TO Continue or Enter Q/q to Quit...")
        if ch=="Q" or ch == "q":
            break
                