from solutions.SolutionTemplate import SolutionTemplate


class DayElevenSolution(SolutionTemplate):

    def __init__(self, input_file_name):
        super().__init__(input_file_name)

    def part_a(self):
        print("Day Eleven, part A")
        current_state = self.input_contents.copy()

        while(True):
            #print("")
            next_state = self.apply_seating_rules_a(current_state)
            if current_state == next_state:
                #print(next_state)
                break
            else:
                current_state = next_state
                #print(next_state)
        print(self.count_occupied_seats(current_state))


    def part_b(self):
        print("Day Eleven, part B")
        current_state = self.input_contents.copy()

        while (True):
            # print("")
            next_state = self.apply_seating_rules_b(current_state)
            if current_state == next_state:
                # print(next_state)
                break
            else:
                current_state = next_state
                # print(next_state)
        print(self.count_occupied_seats(current_state))

    def apply_seating_rules_a(self, current_state):
        next_state = []
        for _ in range(0, len(current_state)):
            next_state.append([])

        for rc in range(0, len(current_state)):
            for cc in range(0, len(current_state[rc])):
                seat = current_state[rc][cc]
                if seat == 'L' and self.count_adjacent_filled_seats(rc, cc, current_state) == 0:
                    next_state[rc].append('#')
                elif seat == '#' and self.count_adjacent_filled_seats(rc, cc, current_state) >= 4:
                    next_state[rc].append('L')
                else:
                    next_state[rc].append(current_state[rc][cc])

        return next_state

    def apply_seating_rules_b(self, current_state):
        next_state = []
        for _ in range(0, len(current_state)):
            next_state.append([])

        for rc in range(0, len(current_state)):
            for cc in range(0, len(current_state[rc])):
                seat = current_state[rc][cc]
                if seat == 'L' and self.count_visible_filled_seats(rc, cc, current_state) == 0:
                    next_state[rc].append('#')
                elif seat == '#' and self.count_visible_filled_seats(rc, cc, current_state) >= 5:
                    next_state[rc].append('L')
                else:
                    next_state[rc].append(current_state[rc][cc])

        return next_state

    def count_adjacent_filled_seats(self, rc, cc, layout):
        rc_changes = [-1, 0, 1]
        cc_changes = [-1, 0, 1]

        filled_seats = 0
        for rc_change in rc_changes:
            for cc_change in cc_changes:
                if rc_change == 0 and cc_change == 0:
                    continue #Don't need to check the seat itself
                next_rc = rc + rc_change
                next_cc = cc + cc_change
                if 0 <= next_rc < len(layout) and 0 <= next_cc < len(layout[rc]):
                    if layout[next_rc][next_cc] == '#':
                        filled_seats += 1

        return filled_seats

    def count_visible_filled_seats(self, rc, cc, layout):
        rc_changes = [-1, -1, -1, 0, 0, 1, 1, 1]
        cc_changes = [-1, 0, 1, -1, 1, -1, 0, 1]

        filled_seats = 0
        for change_index in range(0, len(rc_changes)):
            next_rc = rc
            next_cc = cc
            while True:
                # Apply the current change to find spot in direction
                next_rc += rc_changes[change_index]
                next_cc += cc_changes[change_index]
                if 0 <= next_rc < len(layout) and 0 <= next_cc < len(layout[rc]):
                    if layout[next_rc][next_cc] == '#':
                        filled_seats += 1
                        break
                    elif layout[next_rc][next_cc] == 'L':
                        # Empty, but visible - break anyway
                        break
                else:
                    # Reached the end of the direction, break
                    break

        return filled_seats



    def count_occupied_seats(self, layout):
        occupied_seat_count = 0
        for row in layout:
            for col in row:
                if col == '#':
                    occupied_seat_count += 1
        return occupied_seat_count
