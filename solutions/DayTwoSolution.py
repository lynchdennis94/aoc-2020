from solutions.SolutionTemplate import SolutionTemplate


class DayTwoSolution(SolutionTemplate):

    def __init__(self, input_file_name):
        super().__init__(input_file_name)
        self.password_tuples = self.get_all_password_tuples()

    def part_a(self):
        print("Day Two, part A")
        valid_count = 0
        for password_tuple in self.password_tuples:
            if self.validate_password_part_a(password_tuple):
                valid_count += 1
        print(valid_count)

    def part_b(self):
        print("Day Two, part B")
        valid_count = 0
        for password_tuple in self.password_tuples:
            if self.validate_password_part_b(password_tuple):
                valid_count += 1
        print(valid_count)

    def get_all_password_tuples(self):
        tuple_list = []
        for input_line in self.input_contents:
            tuple_list.append(self.get_password_tuple(input_line))
        return tuple_list

    def get_password_tuple(self, input_line):
        # Password policy is of format MIN-MAX LETTER: PASSWORD
        components = input_line.split(" ")
        total_policy_component = components[0]
        letter_component = components[1]
        password = components[2]

        min_times, max_times = total_policy_component.split("-")
        letter = letter_component.strip(":")

        return int(min_times), int(max_times), letter, password

    def validate_password_part_a(self, input_tuple):
        min_times, max_times, letter, password = input_tuple
        letter_count = 0
        for password_char in password:
            if password_char == letter:
                letter_count += 1
        return min_times <= letter_count <= max_times

    def validate_password_part_b(self, input_tuple):
        first_position, second_position, letter, password = input_tuple
        return (password[first_position-1] == letter) != (password[second_position-1] == letter)
