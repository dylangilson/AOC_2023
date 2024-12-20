import re

def run_program(register_a, register_b, register_c, program_instructions):
    instruction_pointer = 0
    output_values = []

    while instruction_pointer < len(program_instructions):
        registers = {0: 0, 1: 1, 2: 2, 3: 3, 4: register_a, 5: register_b, 6: register_c}
        opcode = program_instructions[instruction_pointer]
        operand = program_instructions[instruction_pointer + 1]

        if opcode == 0: register_a = register_a >> registers[operand] # adv: A = A // (2^operand)
        elif opcode == 1: register_b = register_b ^ operand # bxl: B = B ^ operand
        elif opcode == 2: register_b = 7 & registers[operand] # bst: B = operand % 8
        elif opcode == 3: 
            if register_a: instruction_pointer = operand - 2 # jnz: jump if A != 0
        elif opcode == 4: register_b = register_b ^ register_c # bxc: B = B ^ C
        elif opcode == 5: output_values.append(registers[operand] & 7) # out: output operand % 8
        elif opcode == 6: register_b = register_a >> registers[operand] # bdv: B = A // (2^operand)
        elif opcode == 7: register_c = register_a >> registers[operand] # cdv: C = A // (2^operand)

        instruction_pointer += 2

    return output_values

def part_one(register_a, register_b, register_c, program_instructions):
    print("Part One Solution: " + ','.join(map(str, run_program(register_a, register_b, register_c, program_instructions))))

def find_repeating_program(program_instructions):
    tasks_to_do = [(1, 0)]
    min_value = float('inf')

    for task_index, initial_value in tasks_to_do:
        for value in range(initial_value, initial_value + 8):
            if run_program(value, 0, 0, program_instructions) == program_instructions[-task_index:]:
                tasks_to_do.append((task_index + 1, value * 8))

                if task_index == len(program_instructions):
                    if value < min_value: min_value = value

    return min_value

def part_two(program_instructions):
    print("Part Two Solution: " + str(find_repeating_program(program_instructions)))

if __name__ == '__main__':
    register_a, register_b, register_c, *program_instructions = map(int, re.findall(r'\d+', open('input.txt').read()))

    part_one(register_a, register_b, register_c, program_instructions)
    part_two(program_instructions)
