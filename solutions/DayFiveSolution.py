from solutions.SolutionTemplate import SolutionTemplate


class DayFiveSolution(SolutionTemplate):

    def __init__(self, input_file_name):
        super().__init__(input_file_name)

    def part_a(self):
        print("Day Five, Part A")
        highest_seat_value = -1
        for seat_string in self.input_contents:
            current_seat_value = self.interpret_seat_string(seat_string)
            if current_seat_value > highest_seat_value:
                highest_seat_value = current_seat_value
        print(highest_seat_value)

    def part_b(self):
        print("Day Five, Part B")
        seats_taken = set()
        for seat_string in self.input_contents:
            seats_taken.add(self.interpret_seat_string(seat_string))

        for seat in seats_taken:
            if seat + 1 not in seats_taken and seat + 2 in seats_taken:
                print(seat + 1)
                break

    def interpret_seat_string(self, seat_string):
        # each position of the leftmost seven characters represent
        # a row as a power of two in reverse
        #2^6 ... 2^0
        row_number = 0
        row_exponent = 6
        for seat_char in seat_string[0:7]:
            if seat_char == 'B':
                row_number += 2 ** row_exponent
            row_exponent -= 1

        # Remaining three characters represent 1 of 8 seats
        seat_number = 0
        seat_exponent = 2
        for seat_char in seat_string[7:]:
            if seat_char == 'R':
                seat_number += 2 ** seat_exponent
            seat_exponent -= 1

        seat_value = row_number*8 + seat_number
        return seat_value
