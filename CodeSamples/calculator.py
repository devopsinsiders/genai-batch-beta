# We have to create a calculator that will take input from user for two values and take one more input to decide what to do with those values that can be sum, minus and multiple and divide and output the result.

print("PROGRAM TO CALCULATE SUM")
no_of_values = input("Kitni Value chahiye? ")
op = input("Kya karna hai? (+,-,*,/)? ")
if op == "+" or op == "-":
    result = 0 
else: 
    result = 1

for i in range(0, int(no_of_values), 1):
    inputMessage = "Enter Value " + str(i+1) + ": "
    inputVar = input(inputMessage)

    if op == "+":
        result = result + int(inputVar)
    elif op == "-":
        result = result - int(inputVar)
    elif op == "*":
        result = result * int(inputVar)
    elif op == "/":
        if i == 0:
            result = int(inputVar)
        else:
            result = result / int(inputVar)

print(result)
# 0 1 2 3 4









# value1 = input("Enter Value 1: ")
# value2 = input("Enter Value 2: ")

# op = input("What do you want to do today? (sum,multiply,divide,minus): ")

# if op == "sum":
#     sum = int(value1) + int(value2)
#     print("The Sum is: " + str(sum))
# elif op == "multiply":
#     multipication = int(value1) * int(value2)
#     print("The multipication is: " + str(multipication))
# elif op == "divide":
#     division = int(value1) / int(value2)
#     print("The division is: " + str(division))
# elif op == "minus":
#     minus = int(value1) - int(value2)
#     print("The minus is: " + str(minus))
# else:
#     print("Tu Gadha hai... Screen nahi padti aati kya?")