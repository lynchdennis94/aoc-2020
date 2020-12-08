from solutions.SolutionTemplate import SolutionTemplate


class DaySixSolution(SolutionTemplate):

    def __init__(self, input_file_name):
        super().__init__(input_file_name)

    def part_a(self):
        print("Day Six, part A")
        current_group_responses = []
        total_group_responses = 0
        for line in self.input_contents:
            if line.strip() == '':
                total_group_responses += len(self.process_group_answers(current_group_responses))
                current_group_responses = []
            else:
                current_group_responses.append(line.strip())
        # Catch the last element
        total_group_responses += len(self.process_group_answers(current_group_responses))
        print(total_group_responses)

    def part_b(self):
        print("Day Six, part B")
        current_group_responses = []
        total_group_responses = 0
        for line in self.input_contents:
            if line.strip() == '':
                group_responses_map = self.process_group_answers(current_group_responses)
                for current_response in group_responses_map:
                    if group_responses_map[current_response] == len(current_group_responses):
                        total_group_responses += 1
                current_group_responses = []
            else:
                current_group_responses.append(line.strip())
        # Catch the last element
        group_responses_map = self.process_group_answers(current_group_responses)
        for current_response in group_responses_map:
            if group_responses_map[current_response] == len(current_group_responses):
                total_group_responses += 1
        print(total_group_responses)


    def process_group_answers(self, group_responses):
        answer_map = {}
        for group_response in group_responses:
            for question in group_response:
                if question not in answer_map:
                    answer_map[question] = 0
                answer_map[question] += 1

        return answer_map


