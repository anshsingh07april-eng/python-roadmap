#Q13. Postfix expression. Evaluate "2 3 4 * +" (which means 2 + 3 * 4 = 14). Read each token: if it is a number, push it. If it is an operator, pop two numbers, apply it, and push the result. Test with "5 1 2 + 4 * + 3 -" (answer: 14).
def evaluate_postfix(expression):

    stack = []

    for token in expression.split():

        if token.lstrip("-").isdigit():
            stack.append(int(token))

        else:

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b

            elif token == "-":
                result = a - b

            elif token == "*":
                result = a * b

            elif token == "/":
                result = a / b

            else:
                raise ValueError("Invalid operator: " + token)

            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")

    return stack.pop()


expression1 = "2 3 4 * +"
print("Expression:", expression1)
print("Answer:", evaluate_postfix(expression1))

expression2 = "5 1 2 + 4 * + 3 -"
print("\nExpression:", expression2)
print("Answer:", evaluate_postfix(expression2))
