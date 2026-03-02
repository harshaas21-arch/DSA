assembly_instruction = {
    '+': "add",
    '-': "sub",
    '*': "mul",
    '/': "div"
}

inst = input("Enter the operation to be converted to the instruction: \n").replace(" ","")
list_user_input = list(inst)
#print(list_user_input)

#for i in range(0, len(inst)):
 #   if(inst[i] == '+' or '-' or '*' or '/'):
  #      res = assembly_instruction.get(inst, 0)
   #     print(f"Instructions involved {res} \n")

#print(f"your instruction is {res}")

#print(len(list_user_input))

if(len(list_user_input) == 5):
    opcode = assembly_instruction.get(list_user_input[3])
    dest1 = list_user_input[0]  
    op1 = list_user_input[2]     
    op2 = list_user_input[4]     

    if opcode:
        print(f"{opcode} {dest1}, {op1}, {op2}")
    else:
        print(f"Error: Operator '{list_user_input[3]}' not found in dictionary.")

elif(len(list_user_input) == 7):
    opcode1 = assembly_instruction.get(list_user_input[3])
    opcode2 = assembly_instruction.get(list_user_input[5])
    dest2 = list_user_input[0]
    op1 = list_user_input[2]
    op2 = list_user_input[4]
    op3 = list_user_input[6]
    if opcode1:
        print(f"{opcode1} t0, {op1}, {op2}")
    else:
        print(f"Error: Operator '{list_user_input[3]}' not found in dictionary.")

    if opcode2:
        print(f"{opcode2} {dest2}, t0, {op3}")
    else:
        print(f"Error: Operator '{list_user_input[3]}' not found in dictionary.")

elif(len(list_user_input) == 9):
    opcode1 = assembly_instruction.get(list_user_input[3])
    opcode2 = assembly_instruction.get(list_user_input[5])
    opcode3 = assembly_instruction.get(list_user_input[7])

    dest2 = list_user_input[0]
    op1 = list_user_input[2]
    op2 = list_user_input[4]
    op3 = list_user_input[6]
    op4 = list_user_input[8]

    if opcode1:
        print(f"{opcode1} t0, {op1}, {op2}")
    else:
        print(f"Error: Operator '{list_user_input[3]}' not found in dictionary.")

    if opcode2:
        print(f"{opcode2} t1, t0, {op3}")
    else:
        print(f"Error: Operator '{list_user_input[3]}' not found in dictionary.")

    if opcode3:
        print(f"{opcode3} {dest2}, t1, {op4}")
    else:
        print(f"Error: Operator '{list_user_input[3]}' not found in dictionary.")