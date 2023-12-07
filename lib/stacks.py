
def is_balanced(string):
    # keep track of opening brackets
    stack = []

    dictionaryMapping = {')': '(', '}': '{', ']': '['}

    for item in string:
        if item in dictionaryMapping.values():
            # push opening brackets to stack
            stack.append(item)
        elif item in dictionaryMapping.keys():
            # if stack is empty/no corresponding match
            if not stack or stack.pop() != dictionaryMapping[item]:

                return False
    # if stack is empty/expression is balanced
    return not stack

# test
expression1 = "([]{})"
expression2 = "([)]"

# Check if expressions are balanced and print the result
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
