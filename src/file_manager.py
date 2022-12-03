class file_manager:
    def __init__(self, filename):
        self.filename = filename
        
    def write_file(self, instructions):
        file = open("../"+self.filename, "a")

        for instruction in instructions:
            file.write(instruction+"\n")
