from ..riscv.base_generator import basic_generator_functions

class gen_r_instruction(basic_generator_functions):
    def __init__(self):
        self.instructions_name = ["add", "sub", "xor", "or", "and"]

    def generate_instruction(self, quantity):
        generated_instruction = []

        for _ in range(quantity):
            instruction_name = self.generate_instruction_name(self.instructions_name)
            register1 = self.generate_register()
            register2 = self.generate_register()
            register3 = self.generate_register()
            generated_instruction.append(instruction_name+" "+register1+","+register2+","+register3)
        return generated_instruction
    