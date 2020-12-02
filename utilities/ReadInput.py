import os

class ReadInput:
    def __init__(self):
        self.input_dir_format = os.curdir + "/inputs/"
        print(os.path.abspath(os.getcwd()))

    def get_input(self, filename):

        with open(self.input_dir_format + filename) as file:
            for line in file:
                print(line)