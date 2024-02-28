import os 
def add(n1, n2):
    '''addition function'''
    return n1 + n2
def subtract(n1, n2):
    '''subtraction function'''
    return n1 - n2
def multiply(n1, n2):
    '''multiplication function'''
    return n1 * n2
def divide(n1, n2):
    '''division function'''
    return n1 / n2
operations ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    from art import logo
    print(logo)
    num1=float(input("what's the first number?: "))


    for operator in operations:
        print(operator)

    should_continue =True
    while  should_continue:
        operation_symbol=input("pick an operation: ")

        num2=float(input("what's the second number?: "))

        calculation_function=operations[operation_symbol]
        answer=round(calculation_function(num1 , num2),2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        if input(f"type 'y' to continue calculating with the {answer}, or type 'n' to start a new calculation :  " )=='y':
            num1=answer
        else:
            os.system('cls')
            calculator()
            
calculator()  