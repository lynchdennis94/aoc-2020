from solutions.SolutionTemplate import SolutionTemplate


class DayEightSolution(SolutionTemplate):

    def __init__(self, input_file_name):
        super().__init__(input_file_name)

    def part_a(self):
        print("Day Eight, Part A")
        executed_commands = set()
        acc = 0
        pc = 0

        while pc not in executed_commands:
            executed_commands.add(pc)
            acc, pc = self.get_acc_and_pc(acc, pc, self.input_contents)

        print(acc)

    def part_b(self):
        print("Day Eight, Part B")

        for possible_change_position in range(len(self.input_contents)):
            input_contents_copy = self.input_contents.copy()

            command, value = input_contents_copy[possible_change_position].split(" ")
            if command == 'nop':
                input_contents_copy[possible_change_position] = f"jmp {value}"
            elif command == 'jmp':
                input_contents_copy[possible_change_position] = f"nop {value}"

            # Change the instruction at the position if necessary, then run the program
            # If it terminates, print the acc; otherwise, continue
            found_fix = False
            executed_commands = set()
            acc = 0
            pc = 0
            while pc not in executed_commands:
                executed_commands.add(pc)
                if pc == len(input_contents_copy):
                    print(f"Terminated! {acc}")
                    found_fix = True
                    break

                acc, pc = self.get_acc_and_pc(acc, pc, input_contents_copy, False)

            if found_fix:
                break

        print("Done testing fixes")


    def get_acc_and_pc(self, acc, pc, input_contents, with_debug=False):
        command, value = input_contents[pc].split(" ")
        if with_debug:
            print(f"{pc}: {command} {value}")

        if command == 'nop':
            pc += 1
        elif command == 'acc':
            acc += int(value)
            pc += 1
        else:  # command == jmp
            pc += int(value)

        return acc, pc
