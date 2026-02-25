
def calculate(expression):
    return eval(expression)

if __name__ == "__main__":
    expression = "3 + 7 * 2"
    result = calculate(expression)
    print(f"The result of {expression} is {result}")
