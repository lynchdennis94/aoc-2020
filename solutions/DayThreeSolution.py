from solutions.SolutionTemplate import SolutionTemplate


class DayThreeSolution(SolutionTemplate):

    def __init__(self, input_file_name):
        super().__init__(input_file_name)
        # . = open, # = tree
        self.tree_map = self.get_full_tree_map()

    def part_a(self):
        print("Day Three, part A")
        # Right 3, down 1, starting at 0,0
        print(self.check_hits_on_slope(3, 1))


    def part_b(self):
        print("Day Three, part B")
        a = self.check_hits_on_slope(1, 1)
        b = self.check_hits_on_slope(3, 1)
        c = self.check_hits_on_slope(5, 1)
        d = self.check_hits_on_slope(7, 1)
        e = self.check_hits_on_slope(1, 2)
        print(a*b*c*d*e)

    def check_hits_on_slope(self, horizontal_move, vertical_move):
        tree_count = 0
        row_counter = 0
        col_counter = 0
        while row_counter < len(self.tree_map):
            if self.tree_map[row_counter][col_counter] == '#':
                tree_count += 1
            row_counter += vertical_move
            col_counter += horizontal_move
        return tree_count

    def get_full_tree_map(self):
        number_of_rows = len(self.input_contents)
        tree_map = []
        for input_line in self.input_contents:
            # Get the line, copy until the length of the line is >= 8*number of rows (extra buffer)
            temp_input_line = input_line
            while len(temp_input_line) < number_of_rows*8:
                temp_input_line += input_line
            tree_map.append(temp_input_line)
        return tree_map