import random

class basic_generator_functions:
    def generate_register(self):
        selector = random.randint(0, 31)
        registers = "x" + str(selector)
    
        return (registers)

    def generate_instruction_name(self, instruction_names):
        selector = random.randint(0, len(instruction_names) - 1)
        instruction = instruction_names[selector]

        return instruction