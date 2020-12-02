from solutions.SolutionTemplate import SolutionTemplate


class DayOneSolution(SolutionTemplate):

    def __init__(self, input_file_name):
        super().__init__(input_file_name)
        self.solution_set = self.create_solution_set()

    def part_a(self):
        print("Day One, part A")
        # Iterate over each item in the set, see if it's counterpart is ALSO in the set
        for item in self.solution_set:
            if 2020 - item in self.solution_set:
                print(item*(2020-item))
                break

    def part_b(self):
        print("Day One, part B")
        # Iterate over each item
        for item in self.solution_set:
            found = False
            for sub_item in self.solution_set:
                if 2020 - item - sub_item in self.solution_set:
                    found = True
                    print(item*sub_item*(2020-item-sub_item))
                    break
            if found:
                break

    def create_solution_set(self):
        solution_set = set()
        for item in self.input_contents:
            solution_set.add(int(item))

        return solution_set

