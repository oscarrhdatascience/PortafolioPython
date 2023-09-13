def are_parentheses_balanced(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

print(are_parentheses_balanced("(())()"))  # True
print(are_parentheses_balanced(")("))  # False
