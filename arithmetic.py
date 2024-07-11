def arithmetic_operations(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"


def string_manipulation(s, action):
    if action == 'uppercase':
        return s.upper()
    elif action == 'lowercase':
        return s.lower()
    elif action == 'reverse':
        return s[::-1]
    elif action == 'length':
        return len(s)
    else:
        return "Invalid action"


if __name__ == "__main__":
   
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter the operation (add, subtract, multiply, divide): ")
    
    result = arithmetic_operations(num1, num2, op)
    print("The result of {} between {} and {} is: {}".format(op, num1, num2, result))
    
    
    print("\nString Manipulation")
    string_input = input("Enter a string: ")
    action = input("Enter the action (uppercase, lowercase, reverse, length): ")
    
    manipulated_string = string_manipulation(string_input, action)
    print("The result of {} action on the string '{}' is: {}".format(action, string_input, manipulated_string))
    
 
    print("\nConditional Statements")
    number = int(input("Enter a number: "))
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
