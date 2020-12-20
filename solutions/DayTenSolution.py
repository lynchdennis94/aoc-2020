from solutions.SolutionTemplate import SolutionTemplate


class DayTenSolution(SolutionTemplate):

    def __init__(self, input_file_name):
        super().__init__(input_file_name)
        self.sorted_input = [0] # effective joltage of outlet
        for input in self.input_contents:
            self.sorted_input.append(int(input))
        self.sorted_input.sort()
        self.tree_memoization_map = {}

    def part_a(self):
        print("Day Ten, part A")
        one_skip_count = 0
        three_skip_count = 1 # Built in jump from chain to device

        for sort_index in range (1, len(self.sorted_input)):
            diff = self.sorted_input[sort_index] - self.sorted_input[sort_index - 1]
            if diff == 1:
                one_skip_count += 1
            elif diff == 3:
                three_skip_count += 1

        print(one_skip_count*three_skip_count)

    def part_b(self):
        print("Day Ten, part B")
        print(self.traverse_combinations(0))

    def traverse_combinations(self, current_index):
        # Get the current index and count value
        current_value = self.sorted_input[current_index]
        current_count = 0

        # Get the possible next hops
        next_hop_index = current_index + 1
        continuing_chain = False

        while next_hop_index < len(self.sorted_input) and self.sorted_input[next_hop_index] - current_value <= 3:
            # See if we've encountered the chain so far
            if next_hop_index in self.tree_memoization_map:
                # We've been at this point before, and have mapped out the value
                current_count += self.tree_memoization_map[next_hop_index]
            else:
                rest_of_chain_count = self.traverse_combinations(next_hop_index)

                # Map this to avoid re-doing work
                current_count += rest_of_chain_count
                self.tree_memoization_map[next_hop_index] = current_count

            next_hop_index += 1
            continuing_chain = True

        if not continuing_chain:
            current_count += 1

        return current_count
