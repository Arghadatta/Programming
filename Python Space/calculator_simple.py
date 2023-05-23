# A simple calculator with basic arithmatic tasks and allows only two operands or numbers

function_req = str(input("Enter your desired function to do : "))

var1 = int(input("Enter the first number : "))
var2 = int(input("Enter the second number : "))

if function_req == "Addition":
    print("The sum of numbers inputted is :",var1+var2)
if function_req == "Subtraction":
    print("The sum of numbers inputted is :",var1-var2)

