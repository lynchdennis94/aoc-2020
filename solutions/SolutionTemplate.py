from abc import ABC, abstractmethod


class SolutionTemplate(ABC):

    def __init__(self, input_file_name):
        full_input_file_name = "./inputs/" + input_file_name
        self.input_contents = []
        with open(full_input_file_name) as input_file:
            lines = input_file.readlines()
            for line in lines:
                self.input_contents.append(line.strip('\n'))

    def part_a(self):
        pass

    def part_b(self):
        pass
