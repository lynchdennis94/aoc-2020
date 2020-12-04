import re
from solutions.SolutionTemplate import SolutionTemplate


class DayFourSolution(SolutionTemplate):

    def __init__(self, input_file_name):
        super().__init__(input_file_name)
        self.passport_batches = self.get_passport_batches()
        self.validation_rules_map = self.get_validation_rules()

    def part_a(self):
        print("Day Four, part A")
        valid_passport_count = 0
        for batch in self.passport_batches:
            passport_valid = True
            for key in self.validation_rules_map:
                if key not in batch:
                    passport_valid = False
                    break
            if passport_valid:
                valid_passport_count += 1

        print(valid_passport_count)

    def part_b(self):
        print("Day Four, part B")
        valid_passport_count = 0
        for batch in self.passport_batches:
            passport_valid = True
            for key in self.validation_rules_map:
                if key not in batch:
                    passport_valid = False
                    break
                elif not self.validation_rules_map[key](batch[key]):
                    passport_valid = False
                    break

            if passport_valid:
                valid_passport_count += 1

        print(valid_passport_count)

    def get_passport_batches(self):
        passport_batches = []
        current_batch = ""
        for line in self.input_contents:
            if line == '':
                passport_batches.append(self.get_batch_from_string(current_batch))
                current_batch = ""
            else:
                current_batch += line + ' '

        # File ends without a final break, do a final batch process
        passport_batches.append(self.get_batch_from_string(current_batch))

        return passport_batches

    def get_batch_from_string(self, current_batch):
        batch_map = {}
        components = current_batch.strip().split(" ")
        for component in components:
            key_val_pair = component.split(":")
            key = key_val_pair[0]
            value = key_val_pair[1]
            batch_map[key] = value
        return batch_map

    def get_validation_rules(self):
        return {'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
                'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
                'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
                'hgt': lambda x: (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76) or
                                 (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193),
                'hcl': lambda x: re.match('#[0-9a-f]{6}', x),
                'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                'pid': lambda x: re.match('[0-9]{9}', x)}

