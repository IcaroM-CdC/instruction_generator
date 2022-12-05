import sys

class parameter_reader:
    def __init__(self):
        pass
    def read(self, parameters):
    
        custom_output_filename_flag = False
        randomize_file_flag         = False
        type_r_flag                 = False
        type_i_flag                 = False
        type_s_flag                 = False
        type_i_load_flag            = False

        custom_output_filename = "output.asm"
        type_i_qnt = 0
        type_r_qnt = 0
        type_s_qnt = 0
        type_i_load_qnt = 0

        try:
            # if len(parameters) % 2 == 0:
            #     raise Exception("invalid amount of parameters")

            for index in range(len(parameters)):
                if parameters[index] == "-r":
                    if type_r_flag == False:
                        type_r_flag = True

                        if parameters[index + 1].isnumeric():
                            type_r_qnt = parameters[index + 1]
                        else:
                            raise Exception()
                    else:
                        raise Exception()

                if parameters[index] == "-i":
                    if type_i_flag == False:
                        type_i_flag = True
                        
                        if parameters[index + 1].isnumeric():
                            type_i_qnt = parameters[index + 1]
                        else:
                            raise Exception()
                    else:
                        raise Exception()
                
                if parameters[index] == "-il":
                    if type_i_load_flag == False:
                        type_i_load_flag = True
                        
                        if parameters[index + 1].isnumeric():
                            type_i_load_qnt = parameters[index + 1]
                        else:
                            raise Exception()
                    else:
                        raise Exception()

                if parameters[index] == "-s":
                    if type_s_flag == False:
                        type_s_flag = True
                        
                        if parameters[index + 1].isnumeric():
                            type_s_qnt = parameters[index + 1]
                        else:
                            raise Exception()
                    else:
                        raise Exception()

                if parameters[index] == "-o" or parameters[index] == "--out":
                    if custom_output_filename_flag == False:
                        custom_output_filename_flag = True;
                        custom_output_filename = parameters[index + 1]
                    else:
                        raise Exception()

                if parameters[index] == "-rd" or parameters[index] == "--randomize":
                    if randomize_file_flag == False:
                        randomize_file_flag = True;
                    else:
                        raise Exception()

                else:
                    continue

            if (type_i_flag == False):
                type_i_qnt = 0;
            if (type_r_flag == False):
                type_r_qnt = 0
            if (type_s_flag == False):
                type_s_qnt = 0    
            if (type_i_flag == False and type_r_flag == False and type_s_flag == False):
                raise Exception()

            return type_r_qnt, type_i_qnt, type_s_qnt, type_i_load_qnt, randomize_file_flag, custom_output_filename
        
        except Exception:

            print("invalid parameters")
            print("parameters must follow the format")
            print("[instruction flag] [instruction quantity]")
            print("suported instructions flag: -r -i")
            sys.exit()
            # return 0, 0, ""
