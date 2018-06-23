import unittest, cProfile
from c5 import data, Schedule


class ScheduleTestCase(unittest.TestCase):
    def test_random_searching(self):

        score, result = Schedule.random_searching([(0, 9)] * (len(data.people) * 2))
        Schedule.print_schedule(result)
        print(
            "\nSchedule.random_searching([(0, 9)] * (len(data.people) * 2))  Result:%s" % result + " Score:%s " % score)

    def test_random_searching_benchmark(self):
        cProfile.run(
            'from c5 import data, Schedule\nSchedule.random_searching([(0, 9)] * (len(data.people) * 2))')


    def test_hill_climbing(self):

        score, result = Schedule.hill_climbing([(0, 9)] * (len(data.people) * 2))
        Schedule.print_schedule(result)
        print(
            "\nSchedule.hill_climbing([(0, 9)] * (len(data.people) * 2))  Result:%s" % result + " Score:%s " % score)

    def test_hill_climbing_benchmark(self):
        cProfile.run(
            'from c5 import data, Schedule\nSchedule.hill_climbing([(0, 9)] * (len(data.people) * 2))')


if __name__ == '__main__':
    unittest.main()
