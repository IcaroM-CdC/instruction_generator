import random
from ..riscv.base_generator import basic_generator_functions

class gen_s_instruction(basic_generator_functions):
    def __init__(self):
        self.instructions_name = ["sh", "sb", "sw", "sd"]

    def generate_instruction(self, quantity):
        generated_instruction = []

        for _ in range(quantity):
            instruction_name = self.generate_instruction_name(self.instructions_name)
            register1 = self.generate_register()
            register2 = self.generate_register()
            immediate_offset = str(random.randint(0, 255))
            generated_instruction.append(instruction_name+" "+register1+","+immediate_offset+"("+register2+")")
        return generated_instruction
    