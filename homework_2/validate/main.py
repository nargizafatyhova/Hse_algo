def validate_stack_sequences(pushed, popped):
    if len(pushed) != len(popped):
        return False

    stack = []
    popped_index = 0

    for value in pushed:
        stack.append(value)

        while stack and stack[-1] == popped[popped_index]:
            stack.pop()
            popped_index += 1

    return not stack
