assembly_instruction = {
    '+': "add",
    '-': "sub",
    '*': "mul",
    '/': "div"
}

inst = input("Enter the operation: \n").replace(" ", "")
list_user_input = list(inst)

if len(list_user_input) >= 5:
    dest_final = list_user_input[0]
    first_op = list_user_input[2]
    
    # We iterate through the operators, starting at index 3, skipping by 2
    # indices: 3, 5, 7...
    temp_count = 0
    current_src = first_op

    for i in range(3, len(list_user_input), 2):
        operator_sym = list_user_input[i]
        next_op = list_user_input[i+1]
        opcode = assembly_instruction.get(operator_sym)
        
        if not opcode:
            print(f"Error: Unknown operator {operator_sym}")
            break

        # Determine the destination for this specific line
        # If it's the LAST operator in the string, use the final destination (e.g., 'y')
        # Otherwise, use a temporary register (t0, t1, etc.)
        if i + 2 >= len(list_user_input):
            target = dest_final
        else:
            target = f"t{temp_count}"
        
        # Print the instruction
        print(f"{opcode} {target}, {current_src}, {next_op}")
        
        # Prepare for the next loop: the current result becomes the next source
        current_src = target
        temp_count += 1
else:
    print("Expression too short. Use format y=a+b")
