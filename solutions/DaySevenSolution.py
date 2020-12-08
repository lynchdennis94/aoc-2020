from solutions.SolutionTemplate import SolutionTemplate


class DaySevenSolution(SolutionTemplate):

    def __init__(self, input_file_name):
        super().__init__(input_file_name)
        self.parent_child_map, self.child_parent_map = self.process_rules()
        print(self.parent_child_map)

    def part_a(self):
        print("Day Seven, part A")
        valid_container_bags = set()
        bags_to_check = self.child_parent_map["shiny gold"]
        current_bag_checker_index = 0
        while current_bag_checker_index < len(bags_to_check):
            bag_to_check = bags_to_check[current_bag_checker_index]
            if bag_to_check not in valid_container_bags:
                # Add the current bag to the valid container bags list
                valid_container_bags.add(bag_to_check)

                # Add the possible parents to the list
                if bag_to_check in self.child_parent_map:
                    bags_to_check.extend(self.child_parent_map[bag_to_check])

            current_bag_checker_index += 1

        print(len(valid_container_bags))

    def part_b(self):
        print("Day Seven, part B")
        print(self.get_current_bag_level('shiny gold', 1) - 1) # Don't count yourself
        '''bags_already_checked = set()
        total_count_map = {}
        bags_to_check = self.parent_child_map["shiny gold"]
        current_bag_checker_index = 0
        current_count = 1

        while current_bag_checker_index < len(bags_to_check):
            number, bag_to_check = bags_to_check[current_bag_checker_index]
            if bag_to_check != 'other' and bag_to_check not in bags_already_checked:
                current_number = int(number)

                bags_already_checked.add(bag_to_check)

                if bag_to_check in self.parent_child_map:
                    for child_number, child_description in self.parent_child_map[bag_to_check]:
                        if child_number != 'no':
                            child_number = int(child_number)*int(number)
                            bags_to_check.append((child_number, child_description))

            current_bag_checker_index += 1
        total_bag_count = 0
        print(total_bag_count)'''


    def process_rules(self):
        parent_to_child_mapping = {} # Maps parent to child (number and type)
        child_to_parent_mapping = {} # Maps child to parent mappings (type to types)
        for line in self.input_contents:
            # Split up the rules into their components
            # PARENT <contains> rule, rule ....
            parent, rule_string = line.split("contain")
            parent = self.sanitize_description(parent)
            content_rules = rule_string.strip().split(",")

            # Content rules are (number bag_type)
            for content_rule in content_rules:
                number, child = content_rule.strip().split(" ", 1)

                # The child string will end in bag or bags
                child = self.sanitize_description(child)

                # Add the content tuple (#, description) to parent mapping
                if parent not in parent_to_child_mapping:
                    parent_to_child_mapping[parent] = []
                parent_to_child_mapping[parent].append((number, child))

                # Add the mapping of valid parents for the child
                if child not in child_to_parent_mapping:
                    child_to_parent_mapping[child] = []
                child_to_parent_mapping[child].append(parent)
        return parent_to_child_mapping, child_to_parent_mapping

    def sanitize_description(self, description):
        description = description.strip()
        if description.endswith("."):
            description = description[:-1]
        if description.endswith("bag"):
            description = description[:-3]
        if description.endswith("bags"):
            description = description[:-4]
        return description.strip()

    # Default would be 'shiny gold', 0
    def get_current_bag_level(self, bag, current_count):
        # End recursion if no bags left
        if bag == 'other':
            return 0

        # Get the bag counts for all inner bags
        total_inner_bags = 0
        for inner_bag_count, inner_bag in self.parent_child_map[bag]:
            total_inner_bags += self.get_current_bag_level(inner_bag, inner_bag_count)

        return int(current_count) + int(current_count)*int(total_inner_bags)
