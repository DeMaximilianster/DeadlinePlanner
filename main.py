class Deadline:

    def __init__(self, time, tasks):
        self.time = time
        self.tasks = tasks
        self.tasks_per_time_unit = tasks/time

    def __add__(self, other):
        new_time = self.time + other.time
        new_tasks = self.tasks + other.tasks
        return Deadline(new_time, new_tasks)

    def __ge__(self, other):
        return self.tasks_per_time_unit >= other.tasks_per_time_unit

    def __eq__(self, other):
        return self.tasks == other.tasks and self.time == other.time

    def __repr__(self):
        return f"Deadline: {self.tasks} in {self.time} time units"


def input_deadlines():
    deadlines_count = int(input("How many deadlines should be met? "))
    deadlines = []
    last_time_point = 1
    last_task_point = 0
    for i in range(deadlines_count):
        time_point, task_point = map(int, input(f"Deadline {i+1}. Enter how much time and how many tasks: ").split())
        deadlines.append(Deadline(time_point - last_time_point, task_point - last_task_point))
        last_time_point, last_task_point = time_point, task_point
    return deadlines


def calculate_deadlines(deadlines: list):

    index = len(deadlines) - 1
    while index > 0:
        if deadlines[index] >= deadlines[index - 1]:
            deadlines[index-1:index+1] = [deadlines[index] + deadlines[index - 1]]
        index -= 1

    print(deadlines)
    return deadlines


assert calculate_deadlines([Deadline(1, 1), Deadline(1, 2), Deadline(1, 3)]) == [Deadline(3, 6)]
assert calculate_deadlines([Deadline(1, 2), Deadline(1, 1), Deadline(1, 4)]) == [Deadline(3, 7)]
assert calculate_deadlines([Deadline(1, 5), Deadline(1, 1), Deadline(1, 1)]) == [Deadline(1, 5), Deadline(2, 2)]
assert calculate_deadlines([Deadline(1, 3), Deadline(1, 1), Deadline(1, 2), Deadline(1, 1)]) == \
    [Deadline(1, 3), Deadline(2, 3), Deadline(1, 1)]


if __name__ == "__main__":
    DEADLINES = input_deadlines()
    print(DEADLINES)
    calculate_deadlines(DEADLINES)

