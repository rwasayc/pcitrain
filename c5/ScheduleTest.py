import unittest, cProfile
from c5 import data, Schedule


class ScheduleTestCase(unittest.TestCase):
    def test_random_searching(self):
        score, result = Schedule.random_searching([(0, 9)] * (len(data.people) * 2))
        Schedule.print_schedule(result)
        print(
            "\nSchedule.random_searching([(0, 9)] * (len(data.people) * 2))  Result:%s" % result + " Score:%s " % score)

        sum_score = 0
        run_time = 10
        for i in range(run_time):
            score, result = Schedule.random_searching([(0, 9)] * (len(data.people) * 2))
            sum_score += score
        print("Avg Score ", sum_score / run_time)

    def test_random_searching_benchmark(self):
        cProfile.run(
            'from c5 import data, Schedule\nSchedule.random_searching([(0, 9)] * (len(data.people) * 2))')

    def test_hill_climbing(self):
        score, result = Schedule.hill_climbing([(0, 9)] * (len(data.people) * 2))
        Schedule.print_schedule(result)
        print(
            "\nSchedule.hill_climbing([(0, 9)] * (len(data.people) * 2))  Result:%s" % result + " Score:%s " % score)

        sum_score = 0
        run_time = 50
        for i in range(run_time):
            score, result = Schedule.hill_climbing([(0, 9)] * (len(data.people) * 2))
            sum_score += score
        print("Avg Score ", sum_score / run_time)

    def test_hill_climbing_benchmark(self):
        cProfile.run(
            'from c5 import data, Schedule\nSchedule.hill_climbing([(0, 9)] * (len(data.people) * 2))')

    def test_simulated_annealing(self):
        score, result = Schedule.simulated_annealing([(0, 9)] * (len(data.people) * 2))
        Schedule.print_schedule(result)
        print(
            "\nSchedule.simulated_annealing([(0, 9)] * (len(data.people) * 2))  Result:%s" % result + " Score:%s " % score)
        sum_score = 0
        run_time = 50
        for i in range(run_time):
            score, result = Schedule.simulated_annealing([(0, 9)] * (len(data.people) * 2))
            sum_score += score
        print("Avg Score ", sum_score / run_time)

    def test_simulated_annealing_benchmark(self):
        cProfile.run(
            'from c5 import data, Schedule\nSchedule.simulated_annealing([(0, 9)] * (len(data.people) * 2))')

    def test_genetic_algorithms(self):
        score, result = Schedule.genetic_algorithms([(0, 9)] * (len(data.people) * 2))
        # Schedule.print_schedule(result)
        print(
            "\nSchedule.genetic_algorithms([(0, 9)] * (len(data.people) * 2))  Result:%s" % result + " Score:%s " % score)
        sum_score = 0
        run_time = 20
        for i in range(run_time):
            score, result = Schedule.genetic_algorithms([(0, 9)] * (len(data.people) * 2))
            sum_score += score
        print("Avg Score ", sum_score / run_time)

    def test_genetic_algorithms_benchmark(self):
        cProfile.run(
            'from c5 import data, Schedule\nSchedule.genetic_algorithms([(0, 9)] * (len(data.people) * 2))')


if __name__ == '__main__':
    unittest.main()
