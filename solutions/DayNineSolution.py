from solutions.SolutionTemplate import SolutionTemplate


class DayNineSolution(SolutionTemplate):

    def __init__(self, input_file_name):
        super().__init__(input_file_name)

    def part_a(self):
        print("Day Nine, part A")
        print(self.get_part_a_answer(25))

    def part_b(self):
        print("Day Nine, part B")
        target_number = self.get_part_a_answer(25)

        starting_index = 0
        while starting_index < len(self.input_contents):
            contiguous_values = set()
            temp_target = target_number
            current_index = starting_index

            # Keep adding up in contiguous range
            while temp_target > 0 and current_index < len(self.input_contents):
                next_value = int(self.input_contents[current_index])
                contiguous_values.add(next_value)
                temp_target -= next_value
                current_index += 1

            # We've broken out, see if we found our match
            if temp_target == 0:
                # Found our answer
                min_value, max_value = min(contiguous_values), max(contiguous_values)
                sum_value = min_value + max_value
                print(f"min: {min_value} max: {max_value}")
                print(f"sum: {sum_value}")
                break
            else:
                # Set starting index up by one
                starting_index += 1

    def get_part_a_answer(self, preamble_length):
        answer = -1
        preamble = self.get_preamble(preamble_length)
        valid_number_set = set()
        for number in preamble:
            valid_number_set.add(int(number))
        index = preamble_length
        while preamble_length < len(self.input_contents):
            current_number = int(self.input_contents[index])
            found_valid_combo = False
            for number in valid_number_set:
                if current_number - int(number) in valid_number_set:
                    # Found a valid combo
                    found_valid_combo = True
                    break
            if not found_valid_combo:
                answer = current_number
                break
            else:
                # Remove index - preamble_length from valid set
                valid_number_set.remove(int(self.input_contents[index - preamble_length]))

                # Add current value to valid set
                valid_number_set.add(int(self.input_contents[index]))
            index += 1

        return answer


    def get_preamble(self, preamble_length):
        return self.input_contents[0:preamble_length]