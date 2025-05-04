expression = input("Expression: ").split()

operator = expression[1]
op1 = float(expression[0])
op2 = float(expression[2])

result = 0
match operator:
    case "+":
        result = op1 + op2
    case "-":
        result = op1 - op2
    case "*":
        result = op1 * op2
    case "/":
        result = op1 / op2

print(f"{result:.1f}")
