#Calculator code
def enter_operand(operand_number):
    if operand_number=="first":
        n = int(input("Give me FIRST operand: "))
        return n
    else:
        m = int(input("Give me SECOND operand: "))
        return m

def choose_operation():
    print("What operation you want? \n 1 = Add \n 2 = Subtract \n 3 = Multiply \n 4 = Divide \n")
    operator = int(input("What do you choose: "))
    return operator


def perform_operation(operand1,operand2,operation):
    result = 0
    if (operation == 1):
        result = operand1+operand2
        return result
    elif (operation == 2):
        result = operand1-operand2
        return result
    elif (operation == 3):
        result =  operand1*operand2
        return result
    elif (operation == 4):
        result = operand1/operand2
        return result

def main():
    operator = choose_operation()
    operand1 = enter_operand("first")
    operand2 = enter_operand("second")
    result = perform_operation(operand1, operand2, operator)
    print("Result =", result)

main()