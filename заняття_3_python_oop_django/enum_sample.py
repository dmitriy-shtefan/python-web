from enum import Enum

class TaskStatus(Enum):
    TODO = "to do"
    IN_PROGRESS = "in progress"
    DONE = "done"


class Task:
    def __init__(self, title, status: TaskStatus):
        self.title = title
        self.status = status

    def __str__(self):
        return f"{self.title} [{self.status.name}]"


# створюємо задачі
task1 = Task("Learn Python", TaskStatus.TODO)
task2 = Task("Do Homework", TaskStatus.IN_PROGRESS)

print(task1)
print(task2)

# зміна статусу
task1.status = TaskStatus.DONE
print(task1)

# порівняння enum
if task1.status == TaskStatus.DONE:
    print("Task is completed")

# перебір enum
print("\nAll possible statuses:")
for status in TaskStatus:
    print(f"{status.name} -> {status.value}")