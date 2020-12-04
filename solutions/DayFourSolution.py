import re
from solutions.SolutionTemplate import SolutionTemplate


class DayFourSolution(SolutionTemplate):

    def __init__(self, input_file_name):
        super().__init__(input_file_name)
        self.passport_batches = self.get_passport_batches()

    def part_a(self):
        print("Day Four, part A")
        keys_to_check = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        valid_passport_count = 0
        for batch in self.passport_batches:
            missing_keys = []
            for key in keys_to_check:
                if key not in batch:
                    missing_keys.append(key)
            if len(missing_keys) == 0:

                valid_passport_count += 1

        print(valid_passport_count)

    def part_b(self):
        print("Day Four, part B")
        valid_passport_count = 0
        for batch in self.passport_batches:
            passport_valid = True
            keys_to_check = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
            for key in keys_to_check:
                if key not in batch:
                    passport_valid=False
                    break
                else:
                    value = batch[key]
                    if key == 'byr':
                        if not (1920 <= int(value) <= 2002):
                            passport_valid=False
                            break
                    elif key == 'iyr':
                        if not (2010 <= int(value) <= 2020):
                            passport_valid=False
                            break

                    elif key == 'eyr':
                        if not (2020 <= int(value) <= 2030):
                            passport_valid=False
                            break
                    elif key == 'hgt':
                        if value[-2:] == 'in':
                            if not (59 <= int(value[:-2]) <= 76):
                                passport_valid=False
                                break
                        elif value[-2:] == 'cm':
                            if not (150 <= int(value[:-2]) <= 193):
                                passport_valid=False
                                break
                        else:
                            passport_valid = False
                            break
                    elif key == 'hcl':
                        if not (re.match('#[0-9a-f]{6,6}', value)):
                            passport_valid=False
                            break
                    elif key == 'ecl':
                        if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                            passport_valid=False
                            break

                    elif key == 'pid':
                        if not (re.match('[0-9]{9,9}', str(value))):
                            passport_valid=False
                            break
                    else:
                        continue
            if passport_valid:
                valid_passport_count += 1

        print(valid_passport_count)

    def get_passport_batches(self):
        passport_batches = []
        current_batch = ""
        for line in self.input_contents:
            if line == '':
                batch_map = {}
                components = current_batch.strip().split(" ")
                for component in components:
                    key_val_pair = component.split(":")
                    key = key_val_pair[0]
                    value = key_val_pair[1]
                    batch_map[key] = value
                passport_batches.append(batch_map)
                current_batch = ""
            else:
                current_batch += line + ' '

        return passport_batches

