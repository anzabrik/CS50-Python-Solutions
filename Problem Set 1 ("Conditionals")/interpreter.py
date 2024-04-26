expr = input("Type in the expression: ")
expr_list = expr.split()

x = expr_list[0]
x = int(x)
operator = expr_list[1]
y = expr_list[2]
y = int(y)

match operator:
    case "/":
        z = float(x / y)
    case "+":
        z = float(x + y)
    case "-":
        z = float(x - y)
    case "*":
        z = float(x * y)
print(f"{z: 1}")

