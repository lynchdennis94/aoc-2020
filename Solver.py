import os
from solutions.DayOneSolution import DayOneSolution
from solutions.DayTwoSolution import DayTwoSolution
from solutions.DayThreeSolution import DayThreeSolution
from solutions.DayFiveSolution import DayFiveSolution


class Solver:

    def __init__(self):
        self.solution_map = {'1': DayOneSolution("dayone.txt"),
                             '2': DayTwoSolution("daytwo.txt"),
                             '3': DayThreeSolution("daythree.txt"),
                             '5': DayFiveSolution("dayfive.txt")}

    def solve_problem(self, solution):
        solution.part_a()
        solution.part_b()

    def main(self):
        while(True):
            # Get the problem input
            problem_number = input('Solve problem (type q to quit):')
            if problem_number == 'q':
                break
            elif problem_number in self.solution_map:
                # Get the input and filename
                solution = self.solution_map[problem_number]

                # Solve the problem
                self.solve_problem(solution)
            else:
                print(f"Problem {problem_number} is not yet implemented")


if __name__ == '__main__':
    solver = Solver()
    solver.main()