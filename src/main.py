import sys
import file_manager
import random

from parameter_reader                           import parameter_reader         as parameter_reader
from instructions_generator.riscv.i_type        import gen_i_instruction        as i_type_generator
from instructions_generator.riscv.r_type        import gen_r_instruction        as r_type_generator
from instructions_generator.riscv.s_type        import gen_s_instruction        as s_type_generator
from instructions_generator.riscv.i_load_type   import gen_i_load_instruction   as l_type_generator

def main():

    param_reader = parameter_reader()
    r_instruction_generator = r_type_generator()
    i_instruction_generator = i_type_generator()
    s_insturction_generator = s_type_generator()
    l_instruction_generator = l_type_generator()

    R, I, S, L,randomize,filename = param_reader.read(sys.argv)
    fl_manager = file_manager.file_manager(filename)

    r_instructions_list = r_instruction_generator.generate_instruction(R)
    i_instructions_list = i_instruction_generator.generate_instruction(I)
    s_instructions_list = s_insturction_generator.generate_instruction(S)
    l_instructions_list = l_instruction_generator.generate_instruction(L)
    
    # if we need to randomize instructions inside list
    if randomize == True:
        instructions = []

        for index in range(len(r_instructions_list)):
            instructions.append(r_instructions_list[index])
        for index2 in range(len(i_instructions_list)):
            instructions.append(i_instructions_list[index2])
        for index3 in range(len(s_instructions_list)):
            instructions.append(s_instructions_list[index3])
        for index4 in range(len(l_instructions_list)):
            instructions.append(l_instructions_list[index4])
        
        random.shuffle(instructions)
        random.shuffle(instructions)
        fl_manager.write_file(instructions)
    else:
        fl_manager.write_file(r_instructions_list)
        fl_manager.write_file(i_instructions_list)
        fl_manager.write_file(s_instructions_list)
        fl_manager.write_file(l_instructions_list)

if __name__ == "__main__":
    main()