import re

def infix_to_postfix(expression):
    """Converts a user-input arithmetic expression to postfix notation."""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    # Tokenize: separates variables/numbers from operators
    tokens = re.findall(r'[a-zA-Z0-9]+|[\+\-\*\/\(\)]', expression)
    
    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

def generate_assembly(postfix):
    """Generates RISC-V assembly instructions from postfix tokens."""
    stack = []
    assembly = []
    reg_count = 0
    ops = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'div'}
    
    for token in postfix:
        if token.isalnum():
            stack.append(token)
        else:
            arg2 = stack.pop()
            arg1 = stack.pop()
            dest = f"t{reg_count}"  # Temporary register
            
            instr = ops[token]
            assembly.append(f"{instr} {dest}, {arg1}, {arg2}")
            
            stack.append(dest)
            reg_count += 1
            
    return assembly

# --- Main Execution ---
# Using input() to get the expression from the user
user_expr = input("Enter an arithmetic expression (e.g., a+b*c): ")

try:
    postfix_result = infix_to_postfix(user_expr)
    assembly_code = generate_assembly(postfix_result)

    print(f"\n--- Original Expression: {user_expr} ---")
    print("--- Generated RISC-V Assembly ---")
    if not assembly_code:
        print("# No operations found.")
    else:
        for line in assembly_code:
            print(line)
except Exception as e:
    print(f"Error processing expression: {e}")
